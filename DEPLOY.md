# Deploy — montaznekuce-nijansa.rs (Dokploy)

Sajt je **statički HTML** u folderu `homely/`. Docker + Nginx služe sajt na portu **80**.

## 1. GitHub

Repo: `https://github.com/Adeveloper55/montazne-kuce-nijansa.git`  
Branch: `master`

Ako već nije pushovano, lokalno:

```bash
git push origin master
```

## 2. DNS (domen)

Kod registrar-a / Cloudflare za `montaznekuce-nijansa.rs`:

| Tip | Ime | Vrednost |
|-----|-----|----------|
| A   | `@` | IP adresa Dokploy servera |
| A   | `www` | ista IP adresa |

Sačekaj propagaciju DNS (često 5–30 min).

## 3. Dokploy — nova aplikacija

1. Otvori Dokploy → **Projects** → Create / izaberi projekat.
2. **Create Service** → **Application** (Docker).
3. **Source**: GitHub  
   - Repository: `Adeveloper55/montazne-kuce-nijansa`  
   - Branch: `master`  
   - Build type: **Dockerfile**  
   - Dockerfile path: `Dockerfile` (u root-u repoa)  
   - Docker build context: `.` (root)
4. **Ports**:  
   - Container port: `80`  
   - (Dokploy proxy će mapirati 80/443 spolja)
5. **Domains**:  
   - `montaznekuce-nijansa.rs`  
   - `www.montaznekuce-nijansa.rs` (opciono redirect na bez www)
6. Uključi **HTTPS / Let's Encrypt** (TLS) u Dokploy domain podešavanjima.
7. **Deploy**.

## 4. Provera posle deploy-a

- https://montaznekuce-nijansa.rs/  
- https://montaznekuce-nijansa.rs/montazne-kuce.html  
- https://montaznekuce-nijansa.rs/contact.html  
- Klik na telefon `tel:+381638614764` na mobilnom

## 5. Lokalni test Dockera (opciono)

```bash
docker compose up --build -d
# otvori http://localhost:8080
```

## Napomene

- Nema Node build koraka — samo Nginx + statički fajlovi.
- Forma kontakta trenutno šalje ka `visit.php` / lokalnoj formi — za produkciju poveži backend ili Formspree/Email ako treba slanje mailova.
- Social ikonice i dalje vode na `#` dok klijent ne da prave URL-ove.
