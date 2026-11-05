"""Exercise actual Nginx responses locally or after deployment (stdlib only)."""
import concurrent.futures
import hashlib
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / 'homely'
BASE = (sys.argv[1] if len(sys.argv) > 1 else 'http://127.0.0.1:18087').rstrip('/')
REDIRECTS = json.loads((ROOT / 'scripts/legacy-redirects.json').read_text(encoding='utf-8'))
QUERY = '?gad_source=1&gclid=nijansa-migration-check&utm_source=google&utm_medium=cpc'

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

def fetch(path, *, follow=True):
    opener = urllib.request.build_opener() if follow else urllib.request.build_opener(NoRedirect())
    try:
        r = opener.open(urllib.request.Request(BASE + path, headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 14) AppleWebKit/537.36 Chrome/130.0 Mobile Safari/537.36'}), timeout=25)
    except urllib.error.HTTPError as e:
        r = e
    return r.code, r.headers, r.read(), r.url

def redirect_check(pair):
    source, target = pair
    status, headers, _, _ = fetch(source + QUERY, follow=False)
    location = urllib.parse.urlsplit(headers.get('Location', ''))
    assert status == 301, f'{source}: expected 301, got {status}'
    assert location.path == target, f'{source}: wrong target {location.path}, expected {target}'
    assert location.query == QUERY[1:], f'{source}: lost/changed Google Ads query'
    if location.scheme:
        assert location.scheme == urllib.parse.urlsplit(BASE).scheme, f'{source}: scheme changed'
    return source

class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.refs=[]; self.phones=[]; self.base=None; self.ids=set(); self.visible=[]; self.skip=0
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if tag in ('script','style'): self.skip+=1
        if tag=='base': self.base=a.get('href')
        if a.get('id'): self.ids.add(a['id'])
        if tag=='a' and a.get('href','').startswith('tel:'): self.phones.append(a['href'])
        if tag=='a' and 'href' in a: self.refs.append(a['href'])
        if tag in ('script','img','iframe') and a.get('src'): self.refs.append(a['src'])
        if tag=='img' and a.get('srcset'):
            self.refs.extend(x.strip().split()[0] for x in a['srcset'].split(','))
        if tag=='link' and a.get('rel') in ('stylesheet','icon'): self.refs.append(a.get('href',''))
    def handle_endtag(self, tag):
        if tag in ('script','style'): self.skip=max(0,self.skip-1)
    def handle_data(self, text):
        if not self.skip: self.visible.append(text)

def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
        count=len(list(ex.map(redirect_check, REDIRECTS.items())))
    excluded={'404','news','news-single','gallery'}
    pages=[p for p in SITE.glob('*.html') if p.stem not in excluded and not p.stem.startswith(('homepage-','onepage-'))]
    refs=set(); anchors=[]; ids={}; phones=set()
    for p in pages:
        path='/' if p.name=='index.html' else '/'+p.name
        status, headers, body, final=fetch(path+QUERY)
        assert status==200 and 'text/html' in headers.get('Content-Type',''), (path,status)
        assert hashlib.sha256(body).digest()==hashlib.sha256(p.read_bytes()).digest(), f'{path}: deployed content differs from checkout'
        parsed=Links(); parsed.feed(body.decode('utf-8'))
        ids[path]=parsed.ids
        assert '(+1) 234-5678' not in ''.join(parsed.visible), path
        assert parsed.phones and set(parsed.phones)=={'tel:+381638614764'}, (path,parsed.phones)
        phones.update(parsed.phones)
        for h in parsed.refs:
            if not h or h=='#' or h.startswith(('tel:','mailto:','javascript:','data:')): continue
            full=urllib.parse.urljoin(BASE+path,h)
            if urllib.parse.urlsplit(full).netloc!=urllib.parse.urlsplit(BASE).netloc: continue
            part=urllib.parse.urlsplit(full)
            if part.fragment: anchors.append((path,part.path,part.fragment))
            refs.add(part.path)
    refs.update(REDIRECTS.values())
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
        for path,result in zip(sorted(refs),ex.map(fetch,sorted(refs))):
            status,headers,body,_=result
            assert status==200, (path,status)
            if Path(path).suffix in ('.jpg','.jpeg','.png','.webp','.svg','.css','.js'):
                assert 'text/html' not in headers.get('Content-Type',''), f'{path}: HTML fallback for asset'
    for source,target,anchor in anchors:
        if target in ids: assert anchor in ids[target], (source,target,anchor)
    for path in ('/missing-migration-check/','/missing-migration-check.html','/model-tip-999.html','/images/missing-migration-check.jpg','/news.html','/news-single.html'):
        status,_,body,_=fetch(path)
        assert status==404, (path,status)
        if not path.endswith('.jpg'):
            assert 'Stranica nije pronađena'.encode() in body, path
    # Error content must load root-relative resources even for deeply nested missing pages.
    status,_,body,_=fetch('/missing/deep/page/')
    assert status==404 and b'<base href="/">' in body
    result={'base':BASE,'redirects':count,'active_pages':len(pages),'resources_and_targets':len(refs),'phone_links':sorted(phones),'query_preserved':True,'unknown_urls_return_404':True}
    out=ROOT/'audit-results';out.mkdir(exist_ok=True)
    (out/('migration-production.json' if BASE.startswith('https:') else 'migration-local.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__': main()
