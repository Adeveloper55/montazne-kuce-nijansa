# Inventar sajta — Montažne kuće Nijansa

**Tekst ↔ slike (glavni fajl za redizajn):** `TEKST-SLIKE-MAPA.md` + mašinski `sadrzaj-tekst-slike.json`

Izvor: https://montaznekuce-nijansa.rs/  
Datum prikupljanja: 2026-11-03  
Sve slike i HTML stranice su u folderu `site-assets/`.

---

## Kontakt i osnovne informacije

| Polje | Vrednost | Napomena |
|---|---|---|
| **Brend** | Montažne kuće Nijansa (Ivanjica) | Povezano sa W Projects / VV Projects |
| **Telefon** | 063/861-47-64 | Tel, Viber, WhatsApp · `+381 63 861 4764` |
| **Email** | prodaja@montaznekuce-nijansa.rs | |
| **Adresa** | Šume bb, 32250 Ivanjica, Srbija | Na sajtu se na mestima pojavljuje i PTT **23350** (greška — ispravno je 32250) |
| **Radno vreme** | Pon–Sub 08–16h | |
| **Domena** | montaznekuce-nijansa.rs | |
| **Razvoj sajta** | Infinium (infinium.agency) | Tema: Dustrix / Elementor |

### Društvene mreže
Ikonice postoje (Facebook, Twitter/X, Instagram, YouTube), ali linkovi trenutno vode na `#` — **nisu podešeni**. Za redizajn treba prikupiti stvarne profile.

---

## Mapa sajta (stranice)

| Stranica | URL |
|---|---|
| Početna | https://montaznekuce-nijansa.rs/ |
| Montažne kuće (katalog) | /montazne-kuce/ |
| Do 50 m² | /montazne-kuce-do-50-m2/ |
| 50–100 m² | /montazne-kuce-od-50-do-100-m2/ |
| Preko 100 m² | /montazne-kuce-preko-100-m2/ |
| Planinske Golija | /montazne-planinske-kuce-golija/ |
| A-frame kuće | /a-frame-kuce/ |
| O nama | /o-nama/ |
| FAQ | /faq/ |
| Kontakt | /kontakt/ |
| + 25 pojedinačnih modela | /montazna-kuca-tip-XX/ itd. |

HTML kopije svih stranica: `site-assets/pages/`

---

## Brend / logo slike

Folder: `site-assets/images/brand/`

| Fajl | Upotreba na sajtu |
|---|---|
| `montaznekuce-nijansa.jpg` | Glavni logo (header / footer banner stil) |
| `montaznekuce-nijansa-logot.png` | Logo kvadrat / favicon izvor |
| `cropped-montaznekuce-nijansa-logot.png` | Favicon cropped |
| `nijansamk.png` | Dodatni brend mark (kvadrat) |
| `nijasnatransparent.png` | Transparentni logo / watermark |
| `mknijansa.jpg` | Pozadina / brand strip |

---

## Hero / o nama / A-frame slike

Folder: `site-assets/images/hero-ostalo/`

| Fajl | Gde se koristi |
|---|---|
| `montazne-kuce-vv-projects-ivanjica.jpg` | Hero / pozadina početne |
| `construction.jpg` | Sekcija / pozadina |
| `vvprojects-kancelarija.jpg` | O nama |
| `wprojects-aframe2.jpg` | A-frame stranica (jedina veća A-frame slika) |
| `post2-min.jpg` | Tema / blog placeholder |

`site-assets/images/ui-theme/` — male ikonice teme (b1–b10.png), **ne koristiti** za redizajn.

---

## Katalog modela — kako čitati slike

Svaki tipski model tipično ima **3 slike**:

1. **Glavni render / fasada** — `montazna-kuca-tip-ivanjica-XX.jpg` (ili `…-golija-XX.jpg`)
2. **Drugi ugao / varijacija** — `…-XX-2.jpg`
3. **Šema / tlocrt** — `…-XX-sema.jpg` ili `.png`

Sve u: `site-assets/images/katalog/` (i kompletno u `images/all/`)  
Detaljan JSON sa rasporedom prostorija: `site-assets/katalog-modeli.json`

---

## Do 50 m² (7 modela)

| Model | Bruto | Neto | Sobe | URL | Slike |
|---|---|---|---|---|---|
| **Tip 27** | 31.03 m2 | 26.59 m2 | 2 | https://montaznekuce-nijansa.rs/montazna-kuca-tip-27/ | `montazna-kuca-tip-ivanjica-27.jpg, montazna-kuca-tip-ivanjica-27-2.jpg, montazna-kuca-tip-ivanjica-27-sema.jpg` |
| **Tip 30** | 34.93 m2 | 30.91 m2 | 3 | https://montaznekuce-nijansa.rs/montazna-kuca-tip-30/ | `montazna-kuca-tip-ivanjica-30.jpg, montazna-kuca-tip-ivanjica-30-2.jpg, montazna-kuca-tip-ivanjica-30-sema.png` |
| **Tip 35** | 39.74 m2 | 32.59 m2 | 3 | https://montaznekuce-nijansa.rs/montazna-kuca-tip-35/ | `montazna-kuca-tip-ivanjica-35.jpg, montazna-kuca-tip-ivanjica-35-2.jpg, montazna-kuca-tip-ivanjica-35-sema.png` |
| **Tip 36** | 40.66 m2 | 36.36 m2 | 2 | https://montaznekuce-nijansa.rs/montazna-kuca-tip-36/ | `montazna-kuca-tip-ivanjica-36.jpg, montazna-kuca-tip-ivanjica-36-2.jpg, montazna-kuca-tip-ivanjica-36-sema.png` |
| **Tip 40** | 44.24 m2 | 39.26 m2 | 3 | https://montaznekuce-nijansa.rs/montazna-kuca-tip-40/ | `montazna-kuca-tip-ivanjica-40.jpg, montazna-kuca-tip-ivanjica-40-2.jpg, montazna-kuca-tip-ivanjica-40-sema.jpg` |
| **Tip 44a** | 48.38 m2 | 43.03 m2 | 3 | https://montaznekuce-nijansa.rs/montazna-kuca-tip-44a/ | `montazna-kuca-tip-ivanjica-44a.jpg, montazna-kuca-tip-ivanjica-44a-2-1.jpg, montazna-kuca-tip-ivanjica-44a-sema.jpg` |
| **Tip 44b** | 50.38 m2 | 45.46 m2 | 3 | https://montaznekuce-nijansa.rs/montazna-kuca-tip-44b/ | `montazna-kuca-tip-ivanjica-44b.jpg, montazna-kuca-tip-ivanjica-44b-2.jpg, montazna-kuca-tip-ivanjica-44b-sema.png` |


---

## 50–100 m² (8 modela)

| Model | Bruto | Neto | Sobe | URL | Slike |
|---|---|---|---|---|---|
| **Tip 52** | 55.50 m2 | 49.44 m2 | 5 | https://montaznekuce-nijansa.rs/montazna-kuca-tip-52/ | `montazna-kuca-tip-ivanjica-52.jpg, montazna-kuca-tip-ivanjica-52-2.jpg, montazna-kuca-tip-ivanjica-52-sema.png` |
| **Tip 59** | 64.05 m2 | 57.53 m2 | 5 | https://montaznekuce-nijansa.rs/montazna-kuca-tip-59/ | `montazna-kuca-tip-ivanjica-59.jpg, montazna-kuca-tip-ivanjica-59-2.jpg, montazna-kuca-tip-ivanjica-59-sema.png` |
| **Tip 57** | 65.47 m2 | 57.30 m2 | 3 | https://montaznekuce-nijansa.rs/montazna-kuca-tip-57/ | `montazna-kuca-tip-ivanjica-57.jpg, montazna-kuca-tip-ivanjica-57-2.jpg, montazna-kuca-tip-ivanjica-57-sema.jpg` |
| **Tip 66** | 70.56 m2 | 62.02 m2 | 5 | https://montaznekuce-nijansa.rs/montazna-kuca-tip-66/ | `montazna-kuca-tip-ivanjica-66-1.jpg, montazna-kuca-tip-ivanjica-66-2.jpg, montazna-kuca-tip-ivanjica-66-sema.jpg` |
| **Tip 68** | 75.26 m2 | 68.32 m2 | 4 | https://montaznekuce-nijansa.rs/montazna-kuca-tip-68/ | `montazna-kuca-tip-ivanjica-68.jpg, montazna-kuca-tip-ivanjica-68-2.jpg, montazna-kuca-tip-ivanjica-68-sema.png` |
| **Tip 77** | 82.31 m2 | 74.64 m2 | 5 | https://montaznekuce-nijansa.rs/montazna-kuca-tip-77/ | `montazna-kuca-tip-ivanjica-77.jpg, montazna-kuca-tip-ivanjica-77-2.jpg, montazna-kuca-tip-ivanjica-77-sema.png` |
| **Tip 81** | 90.61 m2 | 81.88 m2 | 6 | https://montaznekuce-nijansa.rs/montazna-kuca-tip-81/ | `montazna-kuca-tip-ivanjica-81.jpg, montazna-kuca-tip-ivanjica-81-2.jpg, montazna-kuca-tip-ivanjica-81-sema.jpg` |
| **Tip 86** | 96.65 m2 | 87.7 m2 | 6 | https://montaznekuce-nijansa.rs/montazna-kuca-tip-86/ | `montazna-kuca-tip-ivanjica-86-1.jpg, montazna-kuca-tip-ivanjica-86-2.jpg, montazna-kuca-tip-ivanjica-86-sema.png` |


---

## Preko 100 m² (7 modela)

| Model | Bruto | Neto | Sobe | URL | Slike |
|---|---|---|---|---|---|
| **Tip 90** | 101.72 m2 | 92.93 m2 | 7 | https://montaznekuce-nijansa.rs/montazna-kuca-tip-90/ | `montazna-kuca-tip-ivanjica-90.jpg, montazna-kuca-tip-ivanjica-90-2.jpg, montazna-kuca-tip-ivanjica-90-sema.jpg` |
| **Tip 101** | 110.22 m2 | 98.76 m2 | 7 | https://montaznekuce-nijansa.rs/montazna-kuca-tip-101/ | `montazna-kuca-tip-ivanjica-101.jpg, montazna-kuca-tip-ivanjica-101-2.jpg, montazna-kuca-tip-ivanjica-101-sema.jpg` |
| **Tip 105** | 121.30 m2 | 111.57 m2 | 7 | https://montaznekuce-nijansa.rs/montazna-kuca-tip-105/ | `montazna-kuca-tip-ivanjica-105.jpg, montazna-kuca-tip-ivanjica-105-2.jpg, montazna-kuca-tip-ivanjica-105-sema.png` |
| **Tip 110** | 125.89 m2 | 115.81 m2 | 7 | https://montaznekuce-nijansa.rs/montazna-kuca-tip-110/ | `montazna-kuca-tip-ivanjica-110.jpg, montazna-kuca-tip-ivanjica-110-2.jpg, montazna-kuca-tip-ivanjica-110-sema.png` |
| **Tip 117** | 133.86 m2 | 123.20 m2 | 8 | https://montaznekuce-nijansa.rs/montazna-kuca-tip-117/ | `montazna-kuca-tip-ivanjica-117.jpg, montazna-kuca-tip-ivanjica-117-2.jpg, montazna-kuca-tip-ivanjica-117-sema.png` |
| **Tip 127** | 139.14 m2 | 126.84 m2 | 8 | https://montaznekuce-nijansa.rs/montazna-kuca-tip-127/ | `montazna-kuca-tip-ivanjica-127.jpg, montazna-kuca-tip-ivanjica-127-2.jpg, montazna-kuca-tip-ivanjica-127-sema.png` |
| **Tip 135** | 146.90 m2 | 134.39 m2 | 8 | https://montaznekuce-nijansa.rs/montazna-kuca-tip-135/ | `montazna-kuca-tip-ivanjica-135.jpg, montazna-kuca-tip-ivanjica-135-2.jpg, montazna-kuca-tip-ivanjica-135-sema.png` |


---

## Planinske kuće Golija (3 modela)

Napomena: URL za Golija 64 na sajtu ima tipfeler: `/montazna-planinska-kuca-goliha-64/` (goli**h**a).

| Model | Bruto | Neto | Sobe | URL | Slike |
|---|---|---|---|---|---|
| **Tip Golija 30** | 55.12 m2 | 47.77 m2 | 4 | https://montaznekuce-nijansa.rs/montazna-planinska-kuca-golija-30/ | `montazna-kuca-tip-golija-30.jpg, montazna-kuca-tip-golija-30-2.jpg, montazna-kuca-tip-golija-30-sema.png` |
| **Tip Golija 40** | 64.56 m2 | 58.87 m2 | 4 | https://montaznekuce-nijansa.rs/montazna-planinska-kuca-golija-40/ | `montazna-kuca-tip-golija-40-1.jpg, montazna-kuca-tip-golija-40-2.jpg, montazna-kuca-tip-golija-40-sema.png` |
| **Tip Golija 64** | 103.56 m2 | 92.80 m2 | 4 | https://montaznekuce-nijansa.rs/montazna-planinska-kuca-goliha-64/ | `montazna-kuca-tip-golija-64.jpg, montazna-kuca-tip-golija-64-2.jpg, montazna-kuca-tip-golija-64-sema.png` |


---

## A-frame

- Stranica postoji, tekst je generički (čak pominje „Vezoom“ — ostatak starog/template teksta).
- Vizuelno: uglavnom `wprojects-aframe2.jpg` — **nema kataloga modela sa šemama** kao kod tipskih kuća.
- Za redizajn: ili izbaciti A-frame dok nema pravog sadržaja, ili dopuniti pravim modelima/slikama.

---

## Tekstovi — ključni copy za redizajn

### Početna — hero
- H1: **Montažne kuće Nijansa Ivanjica**
- CTA: Katalog / Kontaktirajte nas / Pogledajte katalog
- Podnaslov kataloga: tipski modeli, maksimalna funkcionalnost; kvadrature **30 do 150+ m²**; prizemne + planinske vikendice.

### Zašto baš mi?
1. **Iskustvo** — dve decenije, realizovani projekti
2. **Kontrola proizvodnje** — kompletan proces u sopstvenom sistemu
3. **Inovativna rešenja** — moderne tehnologije
4. **Kvalitet koji traje** — materijali, partneri, garancija kvaliteta

### O nama
- Porodična firma **W Projects**, 25+ godina u građevinarstvu
- Početak: završni radovi → montažne i A-frame kuće
- Slogan: *„W Projects – kada iskustvo gradi kvalitet.“*
- Tagline: *„Više od 25 godina stvaramo umetnička dela od vaših montažnih objekata!“*

### Proces izgradnje (4 koraka)
1. Projektovanje i planiranje  
2. Izrada elemenata  
3. Transport i montaža  
4. Završni radovi i useljenje (ključ u ruke)

### FAQ (kratko)
- Cena zavisi od kvadrature/modela/materijala/završnih radova  
- Rok zavisi od veličine i pripreme terena (brže od klasične gradnje)  
- Dostupne kategorije: do 50 / 50–100 / 100+  
- Izmene modela moguće po dogovoru  
- Dozvola zavisi od parcele/propisa  
- Izolacija zavisi od konstrukcije i izvođenja  
- A-frame jeste u ponudi  
- Ponuda preko telefona/forme uz kvadraturu i zahteve  

---

## Struktura foldera

```
site-assets/
  INVENTAR.md              ← ovaj fajl
  katalog-modeli.json      ← svi modeli + raspored prostorija + lista slika
  products.json
  image-urls.txt
  pages/                   ← HTML snimci svih stranica
  images/
    all/                   ← SVE skinute slike (~99 fajlova)
    brand/                 ← logo / brend
    hero-ostalo/           ← hero, o nama, a-frame
    katalog/
      eksterijer/          ← renderi kuća
      sema/                ← tlocrti / šeme
    ui-theme/              ← male ikonice teme (zanemariti)
```

---

## Napomene za redizajn

1. **Brendiranje na sajtu je mešano**: Nijansa / W Projects / VV Projects / „Vezoom“ u A-frame tekstu — uskladiti jedan brend glas.
2. **PTT broj**: 32250 vs 23350 — ispraviti na 32250.
3. **Social linkovi** prazni — dodati prave.
4. **A-frame** i deo O nama teksta izgledaju template/nedovršeno.
5. Listing kartice na kategorijama ponekad imaju zaokružene brojeve (npr. „31m2“); **tačni brojevi** su na stranici modela (bruto/neto) — koristiti JSON.
6. Tip 44b je u kategoriji „do 50 m²“ na sajtu iako bruto ≈ 50.38 m².
7. Ukupno **25 tipskih/planinskih modela** + A-frame stranica bez kataloga.


