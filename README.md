# Sito tymex.it

Sito statico di **Tymex** (Servizi Informatici Srl): HTML, CSS e JS, senza framework.
Netlify pubblica la cartella `public/` così com'è: **nessun comando di build sul server**.

## Struttura

```
public/                 ← il sito pubblicato (generato + immagini e font)
  index.html, en/…      ← pagine IT e EN
  assets/site.css|js    ← stile e script (copiati da src/assets a ogni build)
  img/                  ← immagini ottimizzate (webp), favicon, og-tymex.png
  fonts/                ← Montserrat variabile, ospitato in locale (licenza OFL)
  sitemap.xml, robots.txt, llms.txt, site.webmanifest
src/
  build.py              ← generatore: python3 src/build.py
  pages_marketing.py    ← home, settori, chi siamo, supporto, grazie, 404 (testi IT + EN)
  pages_content.py      ← FAQ, glossario, blog, storico versioni
  legal.py              ← privacy, cookie, sicurezza, condizioni generali
  icons.py              ← icone e illustrazioni SVG
  assets/               ← site.css, site.js (sorgenti)
  legacy/old-site.json  ← testi originali del vecchio sito Wix (base per legali, FAQ, blog…)
netlify.toml            ← redirect 301 dal vecchio sito, intestazioni di sicurezza, cache
```

## Modificare il sito

1. Cambia i testi in `src/*.py` o lo stile in `src/assets/`.
2. Lancia `python3 src/build.py` (Python 3.9+, nessuna dipendenza).
3. Fai commit di `src/` **e** `public/`, poi push: Netlify pubblica da solo.

I riferimenti a CSS e JS hanno un numero di versione (`?v=hash`) che cambia a ogni modifica, così i browser
non tengono versioni vecchie. Le pagine legali partono dai testi originali: `legal.py` applica solo le
sostituzioni elencate e si ferma se un testo originale non viene trovato.

## Pagine

| IT | EN |
|---|---|
| `/` | `/en/` |
| `/software-assistenza-tecnica/` | `/en/field-service-time-tracking-software/` |
| `/software-per-studi-di-progettazione/` | `/en/timesheet-software-engineering-architecture-firms/` |
| `/software-timesheet-agenzie-pubblicitarie/` | `/en/timesheet-software-agencies/` |
| `/software-timesheet-software-house/` | `/en/timesheet-software-it-companies-consultants/` |
| `/faq-timesheet/` | `/en/faq/` |
| `/chi-siamo/` | `/en/about/` |
| `/supporto/` | `/en/support/` |
| `/privacy/`, `/cookie-policy/`, `/sicurezza/` | `/en/privacy/`, `/en/cookie-policy/`, `/en/security/` |
| `/grazie/` | `/en/thank-you/` |
| `/glossario-timesheet/`, `/blog/…`, `/storico-versioni/`, `/condizioni-generali/` | solo italiano |

## Modulo "Richiedi una demo"

Netlify Forms, modulo `demo` (stessi nomi dei campi in IT e EN): `nome`, `azienda`, `email`, `telefono`,
`utenti`, `messaggio`, `privacy`, più i campi nascosti `lingua` e `selettore` (risposte al quiz
"Tymex fa per te?"). Antispam con campo honeypot `bot-field`.
**Notifica email:** su Netlify → *Site configuration → Forms → Form notifications → Add notification → Email*,
destinatario `info@tymex.it`.

## Video

Il video in evidenza si imposta in `src/pages_marketing.py` → `FEATURED_VIDEO = "ID_YOUTUBE"`.
I video si caricano solo al clic, da `youtube-nocookie.com` (Vimeo con `dnt=1`, oppure mp4 locali con
`data-video-type="mp4"`). Finché non c'è un ID, la sezione porta al canale YouTube.

## Statistiche, cookie, privacy

Il sito non usa cookie né script di tracciamento: nessun banner. Le statistiche si attivano con
**Netlify Analytics** (dai log del server). La cookie policy lo spiega. Testi legali da far verificare a un consulente.

## Pubblicazione

Netlify → *Add new project → Import an existing project → GitHub* → `paoloserviziparma/tymex`,
branch `main`, publish directory `public` (già in `netlify.toml`). Poi dominio `www.tymex.it`.
Ogni push su `main` pubblica il sito e consuma crediti Netlify: raggruppare le modifiche.

## Crediti

- Font Montserrat (SIL Open Font License), da Fontsource.
- Screenshot (app, cruscotto generale, dettaglio commesse) e mockup: Servizi Informatici Srl. Illustrazioni SVG originali nei colori del logo.
- Immagini di copertina del blog: riprese dal vecchio sito.
