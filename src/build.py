#!/usr/bin/env python3
"""Genera il sito statico di Tymex in public/.

Uso:  python3 src/build.py
Non serve nessuna dipendenza esterna: solo Python 3.9+.
I contenuti stanno in src/content_it.py, src/content_en.py, src/legal.py e src/legacy/.
Netlify pubblica la cartella public/ così com'è (nessun comando di build).
"""
import hashlib, html, json, os, re, shutil, sys
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "src")
OUT = os.path.join(ROOT, "public")
SITE = "https://www.tymex.it"
sys.path.insert(0, SRC)

import icons as I  # noqa: E402

PAGES = []  # (path, html)
SITEMAP = []  # dict(path, alts, lastmod)
TODAY = date.today().isoformat()

def esc(s):
    return html.escape(s, quote=True)

def asset_version():
    h = hashlib.sha1()
    for f in ("site.css", "site.js"):
        with open(os.path.join(SRC, "assets", f), "rb") as fh:
            h.update(fh.read())
    return h.hexdigest()[:10]

VER = None

ORG = {
    "@type": "Organization",
    "@id": SITE + "/#org",
    "name": "Servizi Informatici Srl",
    "url": "https://www.serviziparma.com",
    "logo": SITE + "/img/tymex-logo.png",
    "email": "info@tymex.it",
    "telephone": "+39 0521 252824",
    "vatID": "IT01721620340",
    "address": {"@type": "PostalAddress", "streetAddress": "Via Sicuri 42/a", "postalCode": "43124",
                "addressLocality": "Parma", "addressRegion": "PR", "addressCountry": "IT"},
    "sameAs": ["https://www.linkedin.com/showcase/79054773"],
}

T = {
    "it": {
        "home": "/", "skip": "Vai al contenuto", "menu_open": "Apri il menu", "menu_close": "Chiudi il menu",
        "nav": [("Funzionalità", "/#funzionalita"), ("Settori", "/#settori"), ("Integrazioni", "/#integrazioni"),
                ("FAQ", "/faq-timesheet/"), ("Supporto", "/supporto/"), ("Contatti", "/#contatti")],
        "login": "Accedi", "cta": "Richiedi una demo", "cta_href": "/#contatti",
        "lang_label": "EN", "lang_aria": "English version", "home_name": "Home",
        "footer": {
            "about": "Tymex è un prodotto di Servizi Informatici Srl",
            "cols": [
                ("Prodotto", [("Funzionalità", "/#funzionalita"), ("Integrazioni", "/#integrazioni"),
                              ("Tymex fa per te?", "/#selettore"), ("Accedi via web", "https://web.tymex.it")]),
                ("Settori", [("Assistenza tecnica", "/software-assistenza-tecnica/"),
                             ("Studi di progettazione", "/software-per-studi-di-progettazione/"),
                             ("Agenzie di comunicazione", "/software-timesheet-agenzie-pubblicitarie/"),
                             ("Software house e consulenti", "/software-timesheet-software-house/")]),
                ("Risorse", [("Blog", "/blog/"), ("FAQ", "/faq-timesheet/"), ("Glossario timesheet", "/glossario-timesheet/"),
                             ("Supporto", "/supporto/"), ("Chi siamo", "/chi-siamo/")]),
            ],
            "legal": [("Privacy", "/privacy/"), ("Cookie", "/cookie-policy/"), ("Sicurezza", "/sicurezza/"),
                      ("Condizioni generali", "/condizioni-generali/")],
        },
    },
    "en": {
        "home": "/en/", "skip": "Skip to content", "menu_open": "Open menu", "menu_close": "Close menu",
        "nav": [("Features", "/en/#features"), ("Industries", "/en/#industries"), ("Integrations", "/en/#integrations"),
                ("FAQ", "/en/faq/"), ("Support", "/en/support/"), ("Contact", "/en/#contact")],
        "login": "Log in", "cta": "Book a demo", "cta_href": "/en/#contact",
        "lang_label": "IT", "lang_aria": "Versione italiana", "home_name": "Home",
        "footer": {
            "about": "Tymex is a product of Servizi Informatici Srl",
            "cols": [
                ("Product", [("Features", "/en/#features"), ("Integrations", "/en/#integrations"),
                             ("Is Tymex right for you?", "/en/#selector"), ("Web app login", "https://web.tymex.it")]),
                ("Industries", [("Field service", "/en/field-service-time-tracking-software/"),
                                ("Engineering & architecture firms", "/en/timesheet-software-engineering-architecture-firms/"),
                                ("Marketing agencies", "/en/timesheet-software-agencies/"),
                                ("IT companies & consultants", "/en/timesheet-software-it-companies-consultants/")]),
                ("Resources", [("FAQ", "/en/faq/"), ("Support", "/en/support/"), ("About us", "/en/about/"),
                               ("Blog (Italian)", "/blog/")]),
            ],
            "legal": [("Privacy", "/en/privacy/"), ("Cookies", "/en/cookie-policy/"), ("Security", "/en/security/"),
                      ("Terms (Italian)", "/condizioni-generali/")],
        },
    },
}

def header(lang, alt_path, current):
    t = T[lang]
    cur = ' aria-current="page"'
    nav = "".join(
        f'<a href="{h}"{cur if h == current else ""}>{esc(n)}</a>' for n, h in t["nav"])
    other = alt_path or ("/en/" if lang == "it" else "/")
    other_lang = "en" if lang == "it" else "it"
    mob = "".join(f'<a href="{h}">{esc(n)}</a>' for n, h in t["nav"])
    return f'''<a class="skip" href="#main">{t["skip"]}</a>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="{t["home"]}"><img src="/img/tymex-logo.png" width="720" height="173" alt="Tymex – Rilevazione ore"></a>
    <nav class="nav" aria-label="{'Menu principale' if lang == 'it' else 'Main menu'}">{nav}</nav>
    <div class="header-actions">
      <a class="lang" href="{other}" hreflang="{other_lang}" lang="{other_lang}" aria-label="{t["lang_aria"]}">{t["lang_label"]}</a>
      <a class="login" href="https://web.tymex.it">{t["login"]}</a>
      <a class="btn btn--primary" href="{t["cta_href"]}">{t["cta"]}</a>
      <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="mobile-menu" aria-label="{t["menu_open"]}" data-open="{t["menu_open"]}" data-close="{t["menu_close"]}">{I.MENU}</button>
    </div>
  </div>
  <div class="mobile-menu" id="mobile-menu">
    <nav aria-label="{'Menu mobile' if lang == 'it' else 'Mobile menu'}">{mob}<a href="https://web.tymex.it">{t["login"]}</a><a class="btn btn--primary" href="{t["cta_href"]}">{t["cta"]}</a></nav>
  </div>
</header>'''

def footer(lang):
    f = T[lang]["footer"]
    cols = "".join(
        f'<div><h2>{esc(h)}</h2><ul>' + "".join(f'<li><a href="{u}">{esc(n)}</a></li>' for n, u in items) + "</ul></div>"
        for h, items in f["cols"])
    legal = "".join(f'<a href="{u}">{esc(n)}</a>' for n, u in f["legal"])
    vat = "P.IVA" if lang == "it" else "VAT"
    return f'''<footer class="site-footer">
  <div class="wrap footer-grid">
    <div>
      <img src="/img/tymex-logo.png" width="720" height="173" alt="Tymex – Rilevazione ore" loading="lazy">
      <p>{esc(f["about"])}<br>Via Sicuri 42/a, 43124 Parma (PR)<br>{vat} 01721620340<br>
      <a href="tel:+390521252824">0521 252824</a> · <a href="mailto:info@tymex.it">info@tymex.it</a></p>
    </div>
    {cols}
  </div>
  <div class="wrap footer-bottom">
    <span>© <span data-year>{date.today().year}</span> Servizi Informatici Srl</span>{legal}
    <a href="https://www.linkedin.com/showcase/79054773" rel="noopener">LinkedIn</a>
  </div>
</footer>'''

def breadcrumbs_html(lang, crumbs):
    if not crumbs:
        return ""
    items = [(T[lang]["home_name"], T[lang]["home"])] + crumbs
    lis = []
    for i, (n, u) in enumerate(items):
        if i == len(items) - 1:
            lis.append(f'<li aria-current="page">{esc(n)}</li>')
        else:
            lis.append(f'<li><a href="{u}">{esc(n)}</a></li>')
    label = "Percorso" if lang == "it" else "Breadcrumb"
    return f'<nav class="crumbs" aria-label="{label}"><ol>{"".join(lis)}</ol></nav>'

def breadcrumbs_ld(lang, crumbs):
    items = [(T[lang]["home_name"], T[lang]["home"])] + crumbs
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + u} for i, (n, u) in enumerate(items)]}

def page(path, lang, title, desc, body, alts=None, crumbs=None, ld=None, og_image="/img/og-tymex.png",
         noindex=False, current=None, og_type="website", sitemap=True):
    """alts: {'it': '/x/', 'en': '/en/x/'} incluse la pagina stessa."""
    alts = alts or {lang: path}
    alt_other = alts.get("en" if lang == "it" else "it")
    head_alt = ""
    if len(alts) > 1:
        for l, p in alts.items():
            head_alt += f'<link rel="alternate" hreflang="{l}" href="{SITE}{p}">\n'
        head_alt += f'<link rel="alternate" hreflang="x-default" href="{SITE}{alts.get("it", path)}">\n'
    graph = [ORG]
    if crumbs:
        graph.append(breadcrumbs_ld(lang, crumbs))
    graph += (ld or [])
    ldjson = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False)
    robots = '<meta name="robots" content="noindex, follow">\n' if noindex else ""
    locale = "it_IT" if lang == "it" else "en_GB"
    doc = f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
{robots}<link rel="canonical" href="{SITE}{path}">
{head_alt}<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="Tymex">
<meta property="og:locale" content="{locale}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{SITE}{path}">
<meta property="og:image" content="{SITE}{og_image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#4654A3">
<link rel="icon" type="image/png" sizes="32x32" href="/img/favicon-32.png">
<link rel="apple-touch-icon" href="/img/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preload" href="/fonts/montserrat-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/site.css?v={VER}">
<script type="application/ld+json">{ldjson}</script>
</head>
<body>
{header(lang, alt_other, current)}
<main id="main">
{body}
</main>
{footer(lang)}
<script src="/assets/site.js?v={VER}" defer></script>
</body>
</html>
'''
    PAGES.append((path, doc))
    if sitemap and not noindex:
        SITEMAP.append({"path": path, "alts": alts if len(alts) > 1 else None})

def write_all():
    for path, doc in PAGES:
        if path.endswith(".html"):
            fp = os.path.join(OUT, path.lstrip("/"))
        else:
            fp = os.path.join(OUT, path.strip("/"), "index.html")
        os.makedirs(os.path.dirname(fp), exist_ok=True)
        with open(fp, "w", encoding="utf-8") as fh:
            fh.write(doc)
    # sitemap
    rows = []
    for s in SITEMAP:
        alt = ""
        if s["alts"]:
            alt = "".join(f'\n    <xhtml:link rel="alternate" hreflang="{l}" href="{SITE}{p}"/>' for l, p in s["alts"].items())
            alt += f'\n    <xhtml:link rel="alternate" hreflang="x-default" href="{SITE}{s["alts"].get("it", s["path"])}"/>'
        rows.append(f'  <url>\n    <loc>{SITE}{s["path"]}</loc>\n    <lastmod>{TODAY}</lastmod>{alt}\n  </url>')
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as fh:
        fh.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
                 'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(rows) + "\n</urlset>\n")
    with open(os.path.join(OUT, "robots.txt"), "w") as fh:
        fh.write(f"User-agent: *\nAllow: /\nDisallow: /grazie/\nDisallow: /en/thank-you/\n\nSitemap: {SITE}/sitemap.xml\n")
    with open(os.path.join(OUT, "site.webmanifest"), "w") as fh:
        json.dump({"name": "Tymex", "short_name": "Tymex", "start_url": "/", "display": "browser",
                   "background_color": "#ffffff", "theme_color": "#4654A3",
                   "icons": [{"src": "/img/icon-192.png", "sizes": "192x192", "type": "image/png"},
                             {"src": "/img/icon-512.png", "sizes": "512x512", "type": "image/png"}]}, fh)

def main():
    global VER
    VER = asset_version()
    # pulizia delle pagine generate (immagini e font restano)
    for name in os.listdir(OUT):
        p = os.path.join(OUT, name)
        if name in ("img", "fonts", "llms.txt", "_redirects"):
            continue
        if os.path.isdir(p):
            shutil.rmtree(p)
        else:
            os.remove(p)
    os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)
    for f in ("site.css", "site.js"):
        shutil.copy(os.path.join(SRC, "assets", f), os.path.join(OUT, "assets", f))
    import pages_marketing, pages_content, legal
    pages_marketing.build(page)
    pages_content.build(page)
    legal.build(page)
    write_all()
    print(f"{len(PAGES)} pagine generate · versione asset {VER}")

if __name__ == "__main__":
    main()
