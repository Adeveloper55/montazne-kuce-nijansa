"""Restore the missing A-frame landing page and a useful real 404 page."""
from pathlib import Path
import re
import shutil

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / 'homely'

def page(title, description, body, *, base=False):
    template = (SITE / 'about.html').read_text(encoding='utf-8')
    template = re.sub(r'<title>.*?</title>', f'<title>{title} | Nijansa Montažne kuće</title>', template, count=1)
    template = re.sub(r'<meta content="[^"]*" name="description">', f'<meta content="{description}" name="description">', template, count=1)
    if base:
        template = template.replace('<head>', '<head>\n    <base href="/">\n    <meta name="robots" content="noindex">', 1)
    result = re.sub(r'<main>.*?</main>', '<main>\n' + body + '\n    </main>', template, count=1, flags=re.S)
    return '\n'.join(line.rstrip() for line in result.splitlines()) + '\n'

def main():
    shutil.copyfile(ROOT / 'site-assets/images/hero-ostalo/wprojects-aframe2.jpg', SITE / 'images/hero/wprojects-aframe2.jpg')
    (SITE / 'a-frame-kuce.html').write_text(page(
        'A-frame kuće',
        'A-frame montažne kuće Nijansa iz Ivanjice. Projektovanje prema vašim zahtevima. Pozovite +381 63 861 47 64.',
        '''        <a href="#" id="back-to-top"></a>
        <section class="mt-80 mt-sm-50">
            <div class="container">
                <div class="row g-4 align-items-center">
                    <div class="col-lg-6">
                        <div class="subtitle">Nijansa Ivanjica</div>
                        <h1>A-frame montažne kuće</h1>
                        <p>A-frame kuće spajaju savremen dizajn i funkcionalan prostor za život ili odmor. Prepoznatljiv oblik krova daje im poseban karakter.</p>
                        <p>Svaka kuća se projektuje prema zahtevima i željama kupca. Kvadraturu, raspored prostorija i završnu obradu usklađujemo sa vašim potrebama i uslovima konkretnog projekta.</p>
                        <p>Za više informacija i ponudu pozovite nas na <a href="tel:+381638614764">+381 63 861 47 64</a>.</p>
                        <div class="d-flex flex-wrap gap-2 mt-4">
                            <a href="tel:+381638614764" class="btn-main fx-slide"><span>Zatražite ponudu</span></a>
                            <a href="contact.html" class="btn-main fx-slide"><span>Kontakt</span></a>
                        </div>
                    </div>
                    <div class="col-lg-6">
                        <img src="images/hero/wprojects-aframe2.jpg" class="w-100 rounded-1" alt="A-frame montažna kuća Nijansa" width="1500" height="1125" style="height:auto">
                    </div>
                </div>
                <div class="mt-5"><a href="montazne-kuce.html">Pogledajte i ostale montažne kuće →</a></div>
            </div>
        </section>'''), encoding='utf-8')
    (SITE / '404.html').write_text(page(
        'Stranica nije pronađena',
        'Tražena stranica nije pronađena. Pogledajte katalog montažnih kuća Nijansa ili nas pozovite.',
        '''        <section class="mt-80 mt-sm-50">
            <div class="container text-center">
                <div class="subtitle">Greška 404</div>
                <h1>Stranica nije pronađena</h1>
                <p>Proverite adresu ili pronađite kuću u našem katalogu.</p>
                <div class="d-flex justify-content-center flex-wrap gap-2 mt-4">
                    <a href="/" class="btn-main fx-slide"><span>Početna</span></a>
                    <a href="/montazne-kuce.html" class="btn-main fx-slide"><span>Katalog kuća</span></a>
                    <a href="tel:+381638614764" class="btn-main fx-slide"><span>Pozovi +381 63 861 47 64</span></a>
                </div>
            </div>
        </section>''', base=True), encoding='utf-8')

    # Correct visible template phone numbers, including copies that will be redirected.
    corrected = []
    for path in SITE.glob('*.html'):
        old = path.read_text(encoding='utf-8')
        new = old.replace('(+1) 234-5678', '+381 63 861 47 64')
        # The shared footer's logo tag was missing its closing bracket.
        new = new.replace('class="w-150px" alt="Nijansa"\n', 'class="w-150px" alt="Nijansa">\n')
        if new != old:
            path.write_text(new, encoding='utf-8')
            corrected.append(path.name)
    print(f'Restored A-frame and 404 pages; corrected {len(corrected)} existing HTML files.')

if __name__ == '__main__':
    main()
