"""FAQ, glossario, blog, storico versioni. I testi arrivano dal vecchio sito (src/legacy/old-site.json)."""
import json, os, re
from html import escape as esc
import icons as I
from pages_marketing import faq_block, faq_ld, SITE

LEG = json.load(open(os.path.join(os.path.dirname(__file__), "legacy", "old-site.json"), encoding="utf-8"))

def fix_it(s):
    """Refusi tipici del vecchio sito (accenti con apostrofo, errori di battitura)."""
    reps = [("Possibilita'", "Possibilità"), ("possibilita'", "possibilità"), ("puo'", "può"), ("Puo'", "Può"),
            ("opertaori", "operatori"), ("filto ", "filtro "), ("possibileaccedere", "possibile accedere"),
            ("Validità", "validità"), ("’", "'"), ("anzichè", "anziché")]
    for a, b in reps:
        s = s.replace(a, b)
    return s

def crumbs_html(lang, crumbs):
    import build
    return build.breadcrumbs_html(lang, crumbs)

def hero(lang, crumbs, kw, h1, lead=""):
    lead_html = f'<p class="lead intro" style="--d:2">{lead}</p>' if lead else ""
    return f'''<section class="page-hero"><div class="wrap">{crumbs_html(lang, crumbs)}
<h1><span class="kw intro" style="--d:0">{esc(kw)}</span><span class="intro" style="--d:1;display:block">{esc(h1)}</span></h1>{lead_html}</div></section>'''

def cta_band(lang):
    if lang == "it":
        return '''<section class="section" style="padding-top:0"><div class="wrap"><div class="cta-band reveal"><div><h2 class="h-lg">Vuoi vedere Tymex in azione?</h2>
<p>Una demo gratuita di 30 minuti sui tuoi casi reali.</p></div><a class="btn btn--light" href="/#contatti">Richiedi una demo</a></div></div></section>'''
    return '''<section class="section" style="padding-top:0"><div class="wrap"><div class="cta-band reveal"><div><h2 class="h-lg">Want to see Tymex in action?</h2>
<p>A free 30-minute demo based on your real cases.</p></div><a class="btn btn--light" href="/en/#contact">Book a demo</a></div></div></section>'''

# ------------------------------------------------------------------ FAQ
FAQ_EN = [
 ("What is Tymex?", "Tymex is timesheet software designed to track hours worked on jobs and projects. Technicians, employees and contractors log activities, hours, customers and jobs from a smartphone or the web app. The data helps the company monitor costs, progress and job margins, reducing the use of spreadsheets and manual processes."),
 ("Which companies use Tymex?", "Tymex is used by companies that work by the job and need to monitor hours, activities and costs. It is especially suited to technical service companies, software houses, installers, maintenance companies, consultants and organisations that want to replace spreadsheets with a more structured system."),
 ("What is timesheet software for?", "It records hours worked accurately, reduces manual errors, eliminates spreadsheets and improves control over company costs."),
 ("Is Tymex useful for companies that work by the job?", "Yes. Tymex is designed for companies that need to control the time, activities and margins of jobs, projects or service calls. If you use eSOLVER by Sistemi Spa, you can connect it to sync: <ul><li>customers</li><li>jobs</li><li>staff</li><li>cost-accounting entries</li></ul>"),
 ("Does Tymex replace spreadsheets?", "Yes. Tymex reduces the use of spreadsheets for collecting hours, making the process more controlled, faster and easier to integrate."),
 ("Can external technicians use Tymex?", "Yes. Technicians can log hours straight from their smartphone, even when working off-site."),
 ("How do you control a job's costs?", "To control a job's costs you need to know the hours worked, the activities carried out and the people involved. Tymex collects this data centrally and keeps it up to date."),
 ("How do you calculate a job's margin?", "A job's margin is obtained by comparing costs and revenue. Accurate tracking of hours worked shows which activities generate profit and which reduce profitability."),
 ("Is Tymex suitable for software houses?", "Yes. Software houses and IT companies can use Tymex to log hours spent on clients, projects and development work."),
 ("Is Tymex suitable for installers?", "Yes. Installers can log hours and activities straight from their smartphone during visits to customers."),
 ("Is Tymex suitable for maintenance companies?", "Yes. Tymex lets maintenance technicians quickly log activities, hours and jobs while working in the field."),
 ("Does Tymex integrate with eSOLVER?", "Yes. Tymex can integrate with eSOLVER to make it easier to manage data on customers, jobs and operations."),
 ("Does Tymex work on a smartphone?", "Yes. The app is designed for smartphones and tablets, so activities can be logged immediately wherever you are."),
]

def faq_it():
    items, q, buf, lst = [], None, [], []
    def flush():
        if q is None:
            return
        a = "".join(f"<p>{esc(fix_it(x))}</p>" for x in buf)
        if lst:
            a += "<ul>" + "".join(f"<li>{esc(x)}</li>" for x in lst) + "</ul>"
        items.append((fix_it(q), a))
    started = False
    for b in LEG["/faq-timesheet"]["blocks"]:
        if b["t"] == "h3":
            flush(); q, buf, lst = b["txt"], [], []; started = True
        elif b["t"] == "h2" and started:
            flush(); q = None; break
        elif started and b["t"] == "p":
            t = b["txt"]
            if t.startswith("- "):
                lst.append(t[2:])
            else:
                buf.append(t)
    flush()
    return items

def faq_pages(page):
    it = faq_it()
    body = hero("it", [("FAQ", "/faq-timesheet/")], "FAQ software timesheet", "Domande frequenti su Tymex e sulla rilevazione ore su commessa.",
                "Come registrare le attività, monitorare i costi delle commesse, sostituire Excel e controllare le ore lavorate da tecnici, dipendenti e collaboratori.")
    body += f'<section class="section" style="padding-top:24px"><div class="wrap">{faq_block(it, True)}</div></section>' + cta_band("it")
    page("/faq-timesheet/", "it", "FAQ software timesheet e rilevazione ore su commessa | Tymex",
         "Risposte alle domande frequenti su Tymex: cos'è un software timesheet, come controllare costi e marginalità delle commesse, uso da smartphone, integrazione con eSOLVER.",
         body, alts={"it": "/faq-timesheet/", "en": "/en/faq/"}, crumbs=[("FAQ", "/faq-timesheet/")], ld=[faq_ld(it)])
    en = [(q, a if a.startswith("<") or "<ul>" in a else f"<p>{esc(a)}</p>") for q, a in FAQ_EN]
    en = [(q, a.replace("Sistemi Spa, you can connect it to sync: ", "Sistemi Spa, you can connect it to sync:</p>").replace("<p>Yes. Tymex is designed", "<p>Yes. Tymex is designed")) for q, a in en]
    en[3] = (FAQ_EN[3][0], "<p>Yes. Tymex is designed for companies that need to control the time, activities and margins of jobs, projects or service calls. If you use eSOLVER by Sistemi Spa, you can connect it to sync:</p><ul><li>customers</li><li>jobs</li><li>staff</li><li>cost-accounting entries</li></ul>")
    body = hero("en", [("FAQ", "/en/faq/")], "Timesheet software FAQ", "Frequently asked questions about Tymex and job time tracking.",
                "How to log activities, monitor job costs, replace spreadsheets and control the hours worked by technicians, employees and contractors.")
    body += f'<section class="section" style="padding-top:24px"><div class="wrap">{faq_block(en, True)}</div></section>' + cta_band("en")
    page("/en/faq/", "en", "Timesheet software FAQ: job time tracking questions | Tymex",
         "Answers to common questions about Tymex: what timesheet software is for, how to control job costs and margins, smartphone use and eSOLVER integration.",
         body, alts={"it": "/faq-timesheet/", "en": "/en/faq/"}, crumbs=[("FAQ", "/en/faq/")], ld=[faq_ld(en)])

# ------------------------------------------------------------------ GLOSSARIO
GLOSS = {"it": "/glossario-timesheet/", "en": "/en/timesheet-glossary/"}

def slugify(t):
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")

def glossary(page):
    from content_en_blog import GLOSSARY_EN
    terms, cur = [], None
    for b in LEG["/glossario-timesheet"]["blocks"]:
        if b["t"] == "h6":
            cur = [b["txt"], ""]; terms.append(cur)
        elif b["t"] == "p" and cur and b["txt"].strip("\u200b ").strip():
            cur[1] = (cur[1] + " " + b["txt"]).strip()
    terms = [(t, d) for t, d in terms if d and "Power BI" not in t + d]
    missing = [t for t, _ in terms if t not in GLOSSARY_EN]
    if missing:
        raise SystemExit(f"Glossario: manca la traduzione inglese di {missing}")
    for lang in ("it", "en"):
        items = [(t, fix_it(d)) for t, d in terms] if lang == "it" else [GLOSSARY_EN[t] for t, _ in terms]
        dl = "".join(f'<div id="{slugify(t)}"><dt>{esc(t)}</dt><dd>{esc(d)}</dd></div>' for t, d in items)
        if lang == "it":
            crumbs = [("Glossario timesheet", GLOSS["it"])]
            body = hero("it", crumbs, "Glossario", "Glossario timesheet e gestione commesse.",
                        "Le definizioni dei principali termini della rilevazione delle ore lavorate, della gestione delle commesse e del controllo dei costi aziendali.")
            title = "Glossario timesheet e gestione commesse: definizioni | Tymex"
            desc = "Cos'è un timesheet, la consuntivazione, la marginalità, il costo orario, il centro di costo: tutte le definizioni della rilevazione ore e gestione commesse."
            name = "Glossario timesheet e gestione commesse"
        else:
            crumbs = [("Timesheet glossary", GLOSS["en"])]
            body = hero("en", crumbs, "Glossary", "Timesheet and job management glossary.",
                        "Definitions of the key terms in tracking hours worked, managing jobs and controlling company costs.")
            title = "Timesheet and job management glossary: definitions | Tymex"
            desc = "What a timesheet is, actual reporting, profit margin, hourly cost, cost centre: all the definitions for time tracking and job management."
            name = "Timesheet and job management glossary"
        body += f'<section class="section" style="padding-top:24px"><div class="wrap"><dl class="gloss" style="margin:0">{dl}</dl></div></section>' + cta_band(lang)
        ld = {"@type": "DefinedTermSet", "name": name, "inLanguage": lang,
              "hasDefinedTerm": [{"@type": "DefinedTerm", "name": t, "description": d} for t, d in items]}
        page(GLOSS[lang], lang, title, desc, body, alts=GLOSS, crumbs=crumbs, ld=[ld])

# ------------------------------------------------------------------ BLOG
POSTS = [
 dict(key="/post/timesheet-excel-vantaggi-limiti-alternative", slug="timesheet-excel-vantaggi-limiti-alternative",
      title="Timesheet Excel: vantaggi, limiti e alternative per la gestione delle ore lavorate",
      seo="Timesheet Excel: vantaggi, limiti e alternative | Tymex",
      desc="Vantaggi e limiti dei timesheet Excel e perché sempre più aziende scelgono un software dedicato per rilevare le ore, controllare le commesse e migliorarne la redditività.",
      date="2026-06-16", img="/img/blog-timesheet-excel.webp", stop="Vuoi eliminare Excel",
      alt="Illustrazione: foglio Excel per il timesheet confrontato con un'app per la rilevazione ore"),
 dict(key="/post/come-calcolare-la-marginalita-di-una-commessa", slug="come-calcolare-la-marginalita-di-una-commessa",
      title="Come calcolare la marginalità di una commessa: guida completa",
      seo="Come calcolare la marginalità di una commessa: guida completa | Tymex",
      desc="Come si calcola la marginalità di una commessa, con formula ed esempio pratico: controllare costi e ore lavorate per migliorare la redditività dei progetti.",
      date="2026-06-09", img="/img/blog-marginalita-commessa.webp", stop="Vuoi migliorare il controllo",
      alt="Illustrazione: grafico della marginalità di una commessa tra costi e ricavi"),
]

def render_blocks(blocks, stop):
    out, mode, rows = [], None, []
    def close():
        nonlocal mode, rows
        if mode == "ul":
            out.append("</ul>")
        elif mode == "table":
            head, *rest = rows
            t = "<table><thead><tr>" + "".join(f"<th scope=\"col\">{esc(c)}</th>" for c in head) + "</tr></thead><tbody>"
            t += "".join("<tr>" + "".join(f"<td>{esc(c)}</td>" for c in r) + "</tr>" for r in rest) + "</tbody></table>"
            out.append(t); rows = []
        mode = None
    for b in blocks:
        t = b["t"]
        if t in ("img", "video"):
            continue
        txt = fix_it(b.get("txt", ""))
        if stop and txt.startswith(stop):
            break
        if t == "li":
            if mode != "ul":
                close(); out.append("<ul>"); mode = "ul"
            out.append(f"<li>{esc(txt.rstrip(';').rstrip('.'))}</li>")
            continue
        if t == "tr":
            if mode != "table":
                close(); mode = "table"
            rows.append(b["cells"]); continue
        close()
        if t in ("h1", "h2"):
            out.append(f"<h2>{esc(txt)}</h2>")
        elif t in ("h3", "h4"):
            out.append(f"<h3>{esc(txt)}</h3>")
        elif t == "p":
            if txt.startswith("Marginalità = "):
                out.append(f'<p class="formula">{esc(txt)}</p>')
            else:
                out.append(f"<p>{esc(txt)}</p>")
    close()
    return "\n".join(out)

def render_markup(text):
    """Testo nel formato di content_en_blog.py -> HTML."""
    out, mode, rows = [], None, []
    def close():
        nonlocal mode, rows
        if mode == "ul":
            out.append("</ul>")
        elif mode == "table":
            head, *rest = rows
            out.append("<table><thead><tr>" + "".join(f'<th scope="col">{esc(c)}</th>' for c in head) + "</tr></thead><tbody>"
                       + "".join("<tr>" + "".join(f"<td>{esc(c)}</td>" for c in r) + "</tr>" for r in rest) + "</tbody></table>")
            rows = []
        mode = None
    for line in text.strip().splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith("- "):
            if mode != "ul":
                close(); out.append("<ul>"); mode = "ul"
            out.append(f"<li>{esc(line[2:])}</li>"); continue
        if line.startswith("|"):
            if mode != "table":
                close(); mode = "table"
            rows.append([c.strip() for c in line.strip("|").split("|")]); continue
        close()
        if line.startswith("### "):
            out.append(f"<h3>{esc(line[4:])}</h3>")
        elif line.startswith("## "):
            out.append(f"<h2>{esc(line[3:])}</h2>")
        elif line.startswith("= "):
            out.append(f'<p class="formula">{esc(line[2:])}</p>')
        else:
            out.append(f"<p>{esc(line)}</p>")
    close()
    return "\n".join(out)

MONTHS = {"it": ["gennaio","febbraio","marzo","aprile","maggio","giugno","luglio","agosto","settembre","ottobre","novembre","dicembre"],
          "en": ["January","February","March","April","May","June","July","August","September","October","November","December"]}

def share_block(url, title, lang):
    """Pulsanti di condivisione: semplici link, nessuno script o cookie di terze parti."""
    from urllib.parse import quote
    u = quote(SITE + url, safe="")
    fb = f"https://www.facebook.com/sharer/sharer.php?u={u}"
    li = f"https://www.linkedin.com/sharing/share-offsite/?url={u}"
    lab = "Condividi l'articolo" if lang == "it" else "Share this article"
    on = "su" if lang == "it" else "on"
    nw = " (si apre in una nuova finestra)" if lang == "it" else " (opens in a new window)"
    fb_ico = '<svg class="ico" width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M13.5 21v-7.5h2.6l.4-3h-3V8.6c0-.9.3-1.5 1.5-1.5h1.6V4.4c-.3 0-1.2-.1-2.3-.1-2.3 0-3.9 1.4-3.9 4v2.2H7.8v3h2.6V21z"/></svg>'
    li_ico = '<svg class="ico" width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.9 8.8H3.6V20h3.3zM5.2 3.5a1.9 1.9 0 1 0 0 3.8 1.9 1.9 0 0 0 0-3.8zM20.4 13.6c0-3-1.6-5-4.4-5-1.4 0-2.4.8-2.8 1.5V8.8H10V20h3.3v-5.6c0-1.5.3-2.9 2.1-2.9s1.8 1.7 1.8 3V20h3.3z"/></svg>'
    return (f'<div class="share"><p class="share-title">{lab}</p><div class="btn-row">'
            f'<a class="btn btn--share" href="{fb}" target="_blank" rel="noopener" aria-label="{lab} {on} Facebook{nw}">{fb_ico}Facebook</a>'
            f'<a class="btn btn--share" href="{li}" target="_blank" rel="noopener" aria-label="{lab} {on} LinkedIn{nw}">{li_ico}LinkedIn</a>'
            f'</div></div>')

def reading_time(html_text, lang):
    words = len(re.findall(r"\w+", re.sub(r"<[^>]+>", " ", html_text)))
    m = max(1, -(-words // 220))
    return f"{m} min di lettura" if lang == "it" else f"{m} min read"

def fmt_date(d, lang):
    m = MONTHS[lang][int(d[5:7]) - 1]
    return f"{int(d[8:])} {m} {d[:4]}"

def blog_en(page):
    from content_en_blog import POSTS_EN
    cards = ""
    for P in sorted(POSTS_EN, key=lambda x: x["date"], reverse=True):
        url = f"/en/blog/{P['slug']}/"
        alts = {"it": f"/blog/{P['it_slug']}/", "en": url}
        d = P["date"]; dd = fmt_date(d, "en")
        crumbs = [("Blog", "/en/blog/"), (P["title"], url)]
        body = f'''<section class="page-hero"><div class="wrap" style="max-width:860px">{crumbs_html("en", crumbs)}
<h1 class="intro">{esc(P["title"])}</h1><p class="post-meta intro" style="--d:1"><time datetime="{d}">{dd}</time> · {reading_time(render_markup(P["body"]), "en")} · Tymex</p></div></section>
<article class="section" style="padding-top:12px"><div class="wrap"><div class="prose">
<figure class="reveal"><img src="{P["img"]}" width="1200" height="800" alt="{esc(P["alt"])}"></figure>
{render_markup(P["body"])}
{share_block(url, P["title"], "en")}
<div class="callout"><strong>Read more:</strong> <a href="/en/faq/">Timesheet FAQ</a> · <a href="/en/timesheet-glossary/">Timesheet glossary</a> · <a href="/en/">Tymex, job time tracking</a></div>
</div></div></article>''' + cta_band("en")
        ld = {"@type": "BlogPosting", "headline": P["title"], "datePublished": d, "dateModified": d, "image": SITE + P["img"],
              "inLanguage": "en", "author": {"@id": SITE + "/#org"}, "publisher": {"@id": SITE + "/#org"},
              "mainEntityOfPage": SITE + url, "description": P["desc"]}
        page(url, "en", P["seo"], P["desc"], body, alts=alts, crumbs=crumbs, ld=[ld], og_type="article")
        cards += f'''<a class="post-card reveal" href="{url}"><img src="{P["img"]}" width="1200" height="800" alt="" loading="lazy">
<div><p class="note"><time datetime="{d}">{dd}</time></p><h2 class="mt-s">{esc(P["title"])}</h2><p>{esc(P["desc"])}</p></div></a>'''
    body = hero("en", [("Blog", "/en/blog/")], "Blog", "Insights on time tracking and job management.",
                "Practical guides to controlling time, costs and margins on your jobs.")
    body += f'<section class="section" style="padding-top:24px"><div class="wrap"><div class="post-cards">{cards}</div></div></section>' + cta_band("en")
    page("/en/blog/", "en", "Blog on timesheets, time tracking and job margins | Tymex",
         "Articles and guides on timesheets, tracking hours worked, cost control and job profit margins.",
         body, alts={"it": "/blog/", "en": "/en/blog/"}, crumbs=[("Blog", "/en/blog/")], ld=[{"@type": "Blog", "name": "Tymex blog", "inLanguage": "en"}])

def blog(page):
    from content_en_blog import POSTS_EN
    from content_blog import POSTS_IT_NEW
    en_by_it = {P["it_slug"]: P["slug"] for P in POSTS_EN}
    cards = ""
    for P in sorted(POSTS + POSTS_IT_NEW, key=lambda x: x["date"], reverse=True):
        url = f"/blog/{P['slug']}/"
        d = P["date"]; dd = fmt_date(d, "it")
        alts = {"it": url, "en": f"/en/blog/{en_by_it[P['slug']]}/"}
        crumbs = [("Blog", "/blog/"), (P["title"], url)]
        content = render_markup(P["body"]) if "body" in P else render_blocks(LEG[P["key"]]["blocks"], P["stop"])
        body = f'''<section class="page-hero"><div class="wrap" style="max-width:860px">{crumbs_html("it", crumbs)}
<h1 class="intro">{esc(P["title"])}</h1><p class="post-meta intro" style="--d:1"><time datetime="{d}">{dd}</time> · {reading_time(content, "it")} · Tymex</p></div></section>
<article class="section" style="padding-top:12px"><div class="wrap"><div class="prose">
<figure class="reveal"><img src="{P["img"]}" width="1200" height="800" alt="{esc(P["alt"])}"></figure>
{content}
{share_block(url, P["title"], "it")}
<div class="callout"><strong>Approfondisci:</strong> <a href="/faq-timesheet/">FAQ timesheet</a> · <a href="/glossario-timesheet/">Glossario timesheet</a> · <a href="/">Tymex, rilevazione ore su commessa</a></div>
</div></div></article>''' + cta_band("it")
        ld = {"@type": "BlogPosting", "headline": P["title"], "datePublished": d, "dateModified": d, "image": SITE + P["img"],
              "inLanguage": "it", "author": {"@id": SITE + "/#org"}, "publisher": {"@id": SITE + "/#org"},
              "mainEntityOfPage": SITE + url, "description": P["desc"]}
        page(url, "it", P["seo"], P["desc"], body, alts=alts, crumbs=crumbs, ld=[ld], og_type="article")
        excerpt = P["desc"]
        cards += f'''<a class="post-card reveal" href="{url}"><img src="{P["img"]}" width="1200" height="800" alt="" loading="lazy">
<div><p class="note"><time datetime="{d}">{dd}</time></p><h2 class="mt-s">{esc(P["title"])}</h2><p>{esc(excerpt)}</p></div></a>'''
    body = hero("it", [("Blog", "/blog/")], "Blog", "Approfondimenti su rilevazione ore e gestione commesse.",
                "Guide pratiche per controllare tempi, costi e marginalità delle commesse.")
    body += f'<section class="section" style="padding-top:24px"><div class="wrap"><div class="post-cards">{cards}</div></div></section>' + cta_band("it")
    page("/blog/", "it", "Blog su timesheet, rilevazione ore e marginalità delle commesse | Tymex",
         "Articoli e guide su timesheet, rilevazione delle ore lavorate, controllo dei costi e marginalità delle commesse.",
         body, alts={"it": "/blog/", "en": "/en/blog/"}, crumbs=[("Blog", "/blog/")], ld=[{"@type": "Blog", "name": "Blog Tymex", "inLanguage": "it"}])

# ------------------------------------------------------------------ STORICO VERSIONI
def versions(page):
    vs, cur = [], None
    for b in LEG["/storico-versioni"]["blocks"]:
        if b["t"] == "h3":
            cur = {"v": b["txt"], "date": "", "items": []}; vs.append(cur)
        elif cur and b["t"] in ("p", "li"):
            t = b["txt"].strip("​ ").strip()
            if not t:
                continue
            if re.fullmatch(r"\d{2}/\d{2}/\d{4}", t):
                cur["date"] = t
            else:
                if "Power BI" not in t:
                    cur["items"].append(fix_it(t.lstrip("- ").strip()))
    arts = ""
    vs = [v for v in vs if v["items"]]
    for v in vs:
        dd, mm, yy = v["date"].split("/")
        arts += f'''<article class="reveal"><h2>Versione {esc(v["v"])}</h2><time datetime="{yy}-{mm}-{dd}">{v["date"]}</time>
<ul>{"".join(f"<li>{esc(i)}</li>" for i in v["items"])}</ul></article>'''
    body = hero("it", [("Supporto", "/supporto/"), ("Storico versioni", "/storico-versioni/")], "Storico versioni", "Le novità di Tymex, versione per versione.")
    body += f'<section class="section" style="padding-top:24px"><div class="wrap"><div class="versions">{arts}</div></div></section>'
    page("/storico-versioni/", "it", "Storico versioni dell'app Tymex | Tymex",
         "Il dettaglio delle novità introdotte in ogni rilascio di Tymex, l'app per la rilevazione delle ore su commessa.",
         body, crumbs=[("Supporto", "/supporto/"), ("Storico versioni", "/storico-versioni/")])

def build(page):
    faq_pages(page)
    glossary(page)
    blog(page)
    blog_en(page)
    versions(page)
