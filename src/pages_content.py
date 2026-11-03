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
def glossary(page):
    terms, cur = [], None
    for b in LEG["/glossario-timesheet"]["blocks"]:
        if b["t"] == "h6":
            cur = [b["txt"], ""]; terms.append(cur)
        elif b["t"] == "p" and cur and b["txt"].strip("​ ").strip():
            cur[1] = (cur[1] + " " + b["txt"]).strip()
    terms = [(t, d) for t, d in terms if d and "Power BI" not in t + d]
    dl = "".join(f'<div id="{re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")}"><dt>{esc(t)}</dt><dd>{esc(fix_it(d))}</dd></div>' for t, d in terms)
    body = hero("it", [("Glossario timesheet", "/glossario-timesheet/")], "Glossario", "Glossario timesheet e gestione commesse.",
                "Le definizioni dei principali termini della rilevazione delle ore lavorate, della gestione delle commesse e del controllo dei costi aziendali.")
    body += f'<section class="section" style="padding-top:24px"><div class="wrap"><dl class="gloss" style="margin:0">{dl}</dl></div></section>' + cta_band("it")
    ld = {"@type": "DefinedTermSet", "name": "Glossario timesheet e gestione commesse", "inLanguage": "it",
          "hasDefinedTerm": [{"@type": "DefinedTerm", "name": t, "description": d} for t, d in terms]}
    page("/glossario-timesheet/", "it", "Glossario timesheet e gestione commesse: definizioni | Tymex",
         "Cos'è un timesheet, la consuntivazione, la marginalità, il costo orario, il centro di costo: tutte le definizioni della rilevazione ore e gestione commesse.",
         body, crumbs=[("Glossario timesheet", "/glossario-timesheet/")], ld=[ld])

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

def blog(page):
    cards = ""
    for P in POSTS:
        url = f"/blog/{P['slug']}/"
        d = P["date"]; dd = f"{int(d[8:])} {['gennaio','febbraio','marzo','aprile','maggio','giugno','luglio','agosto','settembre','ottobre','novembre','dicembre'][int(d[5:7])-1]} {d[:4]}"
        crumbs = [("Blog", "/blog/"), (P["title"], url)]
        content = render_blocks(LEG[P["key"]]["blocks"], P["stop"])
        body = f'''<section class="page-hero"><div class="wrap" style="max-width:860px">{crumbs_html("it", crumbs)}
<h1 class="intro">{esc(P["title"])}</h1><p class="post-meta intro" style="--d:1"><time datetime="{d}">{dd}</time> · Tymex</p></div></section>
<article class="section" style="padding-top:12px"><div class="wrap"><div class="prose">
<figure class="reveal"><img src="{P["img"]}" width="1200" height="800" alt="{esc(P["alt"])}"></figure>
{content}
<div class="callout"><strong>Approfondisci:</strong> <a href="/faq-timesheet/">FAQ timesheet</a> · <a href="/glossario-timesheet/">Glossario timesheet</a> · <a href="/">Tymex, rilevazione ore su commessa</a></div>
</div></div></article>''' + cta_band("it")
        ld = {"@type": "BlogPosting", "headline": P["title"], "datePublished": d, "dateModified": d, "image": SITE + P["img"],
              "inLanguage": "it", "author": {"@id": SITE + "/#org"}, "publisher": {"@id": SITE + "/#org"},
              "mainEntityOfPage": SITE + url, "description": P["desc"]}
        page(url, "it", P["seo"], P["desc"], body, crumbs=crumbs, ld=[ld], og_type="article")
        excerpt = P["desc"]
        cards += f'''<a class="post-card reveal" href="{url}"><img src="{P["img"]}" width="1200" height="800" alt="" loading="lazy">
<div><p class="note"><time datetime="{d}">{dd}</time></p><h2 class="mt-s">{esc(P["title"])}</h2><p>{esc(excerpt)}</p></div></a>'''
    body = hero("it", [("Blog", "/blog/")], "Blog", "Approfondimenti su rilevazione ore e gestione commesse.",
                "Guide pratiche per controllare tempi, costi e marginalità delle commesse.")
    body += f'<section class="section" style="padding-top:24px"><div class="wrap"><div class="post-cards">{cards}</div></div></section>' + cta_band("it")
    page("/blog/", "it", "Blog su timesheet, rilevazione ore e marginalità delle commesse | Tymex",
         "Articoli e guide su timesheet, rilevazione delle ore lavorate, controllo dei costi e marginalità delle commesse.",
         body, crumbs=[("Blog", "/blog/")], ld=[{"@type": "Blog", "name": "Blog Tymex", "inLanguage": "it"}])

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
    versions(page)
