# Montažne kuće Nijansa — redesign

Baza: **Homely** (Designesia) HTML tema, lokalno kopirana 1:1 sa demo sajta.

## Pokretanje

```bash
cd homely
npm start
```

Otvara se na **http://localhost:3000**

## Struktura

- `homely/` — Homely tema (HTML/CSS/JS/images) — radni sajt
- `site-assets/` — inventar sa starog sajta (slike, tekstovi, kontakt, katalog modela)

## Inventar starog sajta

- `site-assets/TEKST-SLIKE-MAPA.md` — tekst ↔ slike
- `site-assets/katalog-modeli.json` — 25 modela + specifikacije
- `site-assets/INVENTAR.md` — pregled

## Produkcija (Dokploy)

Domen: **https://montaznekuce-nijansa.rs**  

Uputstvo: vidi **[DEPLOY.md](DEPLOY.md)**  
Docker: `Dockerfile` u root-u (Nginx, port 80).

## Izvor teme

https://madebydesignesia.com/themes/homely/
