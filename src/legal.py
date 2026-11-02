"""Privacy, cookie policy, sicurezza, condizioni generali.

Si parte dai TESTI ORIGINALI del vecchio sito (src/legacy/old-site.json) e si applicano solo le
modifiche necessarie, elencate qui sotto (ogni sostituzione è verificata: se il testo originale cambia,
la build si ferma). Testi da far verificare a un consulente privacy.
"""
import json, os, re
from html import escape as esc
from pages_content import hero, LEG

ZW = "​"

def clean(t):
    return t.replace(ZW, "").replace("ﬁ", "fi").replace("ﬂ", "fl").strip()

def sub(text, old, new, count=1, regex=False):
    if regex:
        out, n = re.subn(old, new, text, count=count, flags=re.S)
    else:
        n = text.count(old)
        out = text.replace(old, new, count if count else -1)
    if n == 0:
        raise SystemExit(f"legal.py: testo originale non trovato: {old[:80]!r}")
    return out

def linkify(t):
    t = esc(t)
    t = re.sub(r"(https?://[^\s<]+[^\s<.,;:)])", r'<a href="\1" rel="noopener">\1</a>', t)
    t = re.sub(r"([\w.]+@[\w.]+\.(?:it|com))", r'<a href="mailto:\1">\1</a>', t)
    return t

def render(paras, heads2=(), heads3=()):
    """paras: lista di stringhe. Le intestazioni in maiuscolo dentro un paragrafo diventano titoli."""
    out = []
    pat2 = "|".join(re.escape(h) for h in sorted(heads2, key=len, reverse=True))
    pat3 = "|".join(re.escape(h) for h in sorted(heads3, key=len, reverse=True))
    for p in paras:
        p = clean(p)
        if not p:
            continue
        if p.startswith("<"):
            out.append(p); continue
        # spezza sulle intestazioni
        tokens = []
        rx = "|".join(x for x in (f"(?P<h2>{pat2})" if pat2 else "", f"(?P<h3>{pat3})" if pat3 else "") if x)
        pos = 0
        if rx:
            for m in re.finditer(rx, p):
                if m.start() > pos:
                    tokens.append(("p", p[pos:m.start()]))
                tokens.append(("h2" if m.lastgroup == "h2" else "h3", m.group(0)))
                pos = m.end()
        tokens.append(("p", p[pos:]))
        for kind, txt in tokens:
            txt = txt.strip()
            if not txt:
                continue
            if kind == "p":
                if " • " in f" {txt}" and "•" in txt:
                    parts = [x.strip() for x in txt.split("•")]
                    if parts[0]:
                        out.append(f"<p>{linkify(parts[0])}</p>")
                    out.append("<ul>" + "".join(f"<li>{linkify(x)}</li>" for x in parts[1:] if x) + "</ul>")
                else:
                    out.append(f"<p>{linkify(txt)}</p>")
            else:
                out.append(f"<{kind}>{esc(sentence_case(txt))}</{kind}>")
    return "\n".join(out)

def sentence_case(t):
    if not any(c.islower() for c in t):
        t = t.lower()
        t = re.sub(r"[a-zà-ü]", lambda m: m.group(0).upper(), t, count=1)
        t = re.sub(r"\bunione europea\b", "Unione Europea", t)
    return t

def blocks(key):
    return [clean(b["txt"]) for b in LEG[key]["blocks"]]

# ------------------------------------------------------------------ PRIVACY
NETLIFY_IT = ("Il sito è ospitato su Netlify (Netlify, Inc., Stati Uniti), che tratta i dati come responsabile del trattamento "
    "per l'hosting del sito, la conservazione dei dati di navigazione (log del server) e la ricezione delle richieste inviate "
    "con il modulo di contatto (Netlify Forms). Le statistiche di visita sono elaborate da Netlify Analytics a partire dai log "
    "del server, in forma aggregata e senza l'uso di cookie. I server web possono essere posizionati sia all'interno sia al di "
    "fuori dell'Unione Europea (ad esempio Stati Uniti); i trasferimenti di dati al di fuori dell'Unione Europea vengono "
    "effettuati garantendo un adeguato livello di protezione secondo la Commissione Europea, in conformità alle Clausole "
    "Contrattuali Standard. A questo link è possibile consultare l'Accordo sul trattamento dei dati: "
    "https://www.netlify.com/pdf/netlify-dpa.pdf")
NETLIFY_IT_2 = "A questo link è invece possibile consultare la policy sui dati personali: https://www.netlify.com/privacy/"
EXT_IT = ("SERVIZI ESTERNI I pulsanti e i link verso App Store, Google Play, YouTube, LinkedIn, Google Maps e la web app "
    "web.tymex.it aprono servizi di terze parti, soggetti alle rispettive informative. I video presenti nel sito vengono "
    "caricati da YouTube in modalità privacy avanzata (youtube-nocookie.com) solo dopo il clic dell'utente sull'anteprima.")

NETLIFY_EN = ("The site is hosted on Netlify (Netlify, Inc., United States), which processes data as a data processor for "
    "hosting the site, storing navigation data (server logs) and receiving requests sent through the contact form (Netlify "
    "Forms). Visit statistics are produced by Netlify Analytics from the server logs, in aggregate form and without cookies. "
    "The web servers can be located both within and outside the European Union (for example the United States); data "
    "transfers outside the European Union are carried out guaranteeing an adequate level of protection according to the "
    "European Commission, in compliance with the Standard Contractual Clauses. At this link you can consult the Agreement "
    "on data processing: https://www.netlify.com/pdf/netlify-dpa.pdf")
NETLIFY_EN_2 = "At this link it is possible to consult the personal data policy: https://www.netlify.com/privacy/"
EXT_EN = ("EXTERNAL SERVICES Buttons and links to the App Store, Google Play, YouTube, LinkedIn, Google Maps and the web app "
    "web.tymex.it open third-party services, which are subject to their own privacy notices. Videos on the site are loaded "
    "from YouTube in privacy-enhanced mode (youtube-nocookie.com) only after the user clicks the preview.")

def privacy_it():
    b = blocks("/privacy")
    b[1] = sub(b[1], "2016/67", "2016/679")
    b[3] = sub(b[3], "https://www.tymex.com/", "https://www.tymex.it/")
    b[4] = sub(b[4], "info@serviziparma.com", "info@tymex.it")
    b[4] = sub(b[4], " e di gestire gli eventuali ordini di QR code effettuati mediante l’apposita pagina.", ".")
    b[7] = sub(b[7], r"Documenti digitali .*?(?=DESTINATARI DEI DATI)", "", regex=True)
    b[7] = sub(b[7], " e tramite la sezione e-commerce", "")
    b[7] = sub(b[7], "I circuiti di pagamento abilitati, tramite gateway di pagamento che si attiva alla conferma dell’ordine, ricevono i dati relativi alla carta di credito dell’acquirente. ", "")
    b[7] = sub(b[7], r"Il sito è sviluppando con la piattaforma.*$", NETLIFY_IT, regex=True)
    b[8] = NETLIFY_IT_2
    b[9] = EXT_IT
    b[10] = sub(b[10], "https://www.wix.com/about/privacy ", "")
    b[13] = sub(b[13], "nostra istituzione scolastica", "nostra azienda")
    b[3] = "<ul><li>" + linkify(b[3]) + "</li></ul>"
    b[0] = ""
    h2 = ["INFORMAZIONI SUL TRATTAMENTO DEI DATI PERSONALI", "TITOLARE DEL TRATTAMENTO", "BASE GIURIDICA DEL TRATTAMENTO",
          "TIPI DI DATI TRATTATI E FINALITÀ DEL TRATTAMENTO", "DESTINATARI DEI DATI", "SERVIZI ESTERNI",
          "DIRITTI DEGLI INTERESSATI E DIRITTO DI RECLAMO", "NOTE LEGALI"]
    h3 = ["Dati di navigazione", "Dati comunicati dall'utente", "Form di contatto", "A) DISCLAIMER",
          "B) LIMITAZIONE DI RESPONSABILITA'", "C) COPYRIGHT"]
    return render(b, h2, h3)

def privacy_en():
    b = blocks("/en/privacy")
    b[1] = sub(b[1], "2016/67", "2016/679")
    b[3] = sub(b[3], "https://www.tymex.com/", "https://www.tymex.it/")
    b[4] = sub(b[4], "info@serviziparma.com", "info@tymex.it")
    b[4] = sub(b[4], r" and to manage any QR code orders placed through the appropriate page\.", ".", regex=True)
    b[7] = sub(b[7], r"Digital documents .*?(?=RECIPIENTS OF THE DATA)", "", regex=True)
    b[7] = sub(b[7], r" and through the e-commerce section", "", regex=True)
    b[7] = sub(b[7], r"The payment circuits enabled, .*?credit card\. ", "", regex=True)
    b[7] = sub(b[7], r"The site is developed with the do-it-yourself platform.*$", NETLIFY_EN, regex=True)
    b[8] = NETLIFY_EN_2
    b[9] = EXT_EN
    b[10] = sub(b[10], "https://www.wix.com/about/privacy ", "")
    b[13] = sub(b[13], "our school", "our company")
    b[3] = "<ul><li>" + linkify(b[3]) + "</li></ul>"
    b[0] = ""
    h2 = ["INFORMATION ON THE PROCESSING OF PERSONAL DATA", "HOLDER OF THE TREATMENT", "LEGAL BASIS OF THE PROCESSING",
          "TYPES OF DATA PROCESSED AND PURPOSE OF THE TREATMENT", "RECIPIENTS OF THE DATA", "EXTERNAL SERVICES",
          "RIGHTS OF THE INTERESTED PARTIES AND RIGHT OF COMPLAINT", "LEGAL NOTICES"]
    h3 = ["Navigation data", "Data communicated by the user", "Contact form", "A) DISCLAIMER", "B) LIMITATION OF LIABILITY", "C) COPYRIGHT"]
    return render(b, h2, h3)

# ------------------------------------------------------------------ COOKIE
NOCOOKIE_IT = [
    "Questo sito non utilizza cookie, né tecnici né statistici né di profilazione, e non usa altri strumenti di tracciamento. "
    "Per questo motivo non viene mostrato alcun banner per il consenso.",
    "Le statistiche di visita sono ottenute con Netlify Analytics, che elabora in forma aggregata i log del server "
    "(vedi la privacy policy) senza installare nulla sul dispositivo dell'utente.",
    "Servizi esterni: i video vengono caricati da YouTube in modalità privacy avanzata (youtube-nocookie.com) solo se l'utente "
    "fa clic sull'anteprima; da quel momento YouTube può utilizzare cookie o tecnologie simili secondo la propria informativa "
    "(https://policies.google.com/privacy). I link verso App Store, Google Play, LinkedIn, Google Maps e la web app "
    "web.tymex.it portano a servizi di terzi, soggetti alle rispettive cookie policy."]
NOCOOKIE_EN = [
    "This site does not use cookies, whether technical, statistical or profiling, and does not use any other tracking tools. "
    "For this reason no consent banner is shown.",
    "Visit statistics are obtained with Netlify Analytics, which processes the server logs in aggregate form "
    "(see the privacy policy) without installing anything on the user's device.",
    "External services: videos are loaded from YouTube in privacy-enhanced mode (youtube-nocookie.com) only if the user "
    "clicks the preview; from that moment YouTube may use cookies or similar technologies under its own policy "
    "(https://policies.google.com/privacy). Links to the App Store, Google Play, LinkedIn, Google Maps and the web app "
    "web.tymex.it lead to third-party services, which are subject to their own cookie policies."]

def cookie(lang):
    key = "/copia-di-privacy" if lang == "it" else "/en/copia-di-privacy"
    b = blocks(key)
    if len(b) != 39:
        raise SystemExit(f"legal.py: la cookie policy {lang} ha cambiato struttura ({len(b)} blocchi)")
    b[2] = sub(b[2], "info@serviziparma.com", "info@tymex.it")
    nc = NOCOOKIE_IT if lang == "it" else NOCOOKIE_EN
    b[21], b[22] = nc[0], nc[1] + " " + nc[2]
    b[24] = ("Poiché il sito non installa cookie, non ci sono tempi di conservazione da indicare." if lang == "it"
             else "Since the site does not set cookies, there are no retention periods to state.")
    b[25] = ""
    if lang == "it":
        b[32] = sub(b[32], r"; così facendo e rientrando nel sito il banner sarà riproposto e sarà così possibile rinnovare o esprimere di nuovo il consenso\.", ".", regex=True)
    else:
        b[32] = sub(b[32], r"; by doing so and returning to the site, the banner will be repeated and it will be possible to renew or express consent again\.", ".", regex=True)
    # titoli
    heads = {6, 9, 20, 23, 26, 35}
    out = []
    lst = []
    for i, t in enumerate(b):
        if i == 0 or not t:
            continue
        if 28 <= i <= 31:
            lst.append(f"<li>{linkify(t)}</li>")
            if i == 31:
                out.append("<ul>" + "".join(lst) + "</ul>")
            continue
        if i in heads:
            out.append(f"<h2>{esc(sentence_case(t))}</h2>")
        else:
            out.append(f"<p>{linkify(t)}</p>")
    return "\n".join(out)

# ------------------------------------------------------------------ SICUREZZA
def security(lang):
    b = blocks("/sicurezza" if lang == "it" else "/en/sicurezza")
    b[0] = ""
    if lang == "it":
        h2 = ["Cos’è Ground’81", "Integrazione con librerie esterne", "API Connect", "Calcolo dell’Hash", "Servizio in Cloud"]
        b = [x.replace("HMTL", "HTML") for x in b]
    else:
        h2 = ["What is Ground'81", "Integration with external libraries", "API Connect", "Hash calculation", "Cloud service"]
        b = [x.replace("byWeb'81", "by Web'81").replace("applicationsWeb 81", "applications Web 81") for x in b]
    # una voce elenco isolata va unita al paragrafo precedente
    merged = []
    for x in b:
        if x.startswith("•") and merged:
            merged[-1] += " " + x
        else:
            merged.append(x)
    return render(merged, [h for h in h2], [])

# ------------------------------------------------------------------ CONDIZIONI
def terms():
    out, in_list = [], False
    for t in blocks("/copia-di-manuale-utente")[1:]:
        if not t:
            continue
        if re.match(r"^-\s*", t):
            if not in_list:
                out.append("<ul>"); in_list = True
            out.append(f"<li>{linkify(re.sub(r'^-\s*', '', t))}</li>")
            continue
        if in_list:
            out.append("</ul>"); in_list = False
        if re.match(r"^SEZIONE \d+", t):
            out.append(f'<h2 id="{re.sub(r"[^a-z0-9]+", "-", t.lower())[:40].strip("-")}">{esc(t)}</h2>')
        elif re.match(r"^\d+\.\d+(\.\d+)? [A-ZÀ-Ü' ,/()-]+$", t):
            out.append(f"<h3>{esc(t)}</h3>")
        else:
            out.append(f"<p>{linkify(t)}</p>")
    if in_list:
        out.append("</ul>")
    toc = "".join(f'<li><a href="#{m.group(1)}">{m.group(2)}</a></li>' for m in re.finditer(r'<h2 id="([^"]+)">([^<]+)</h2>', "\n".join(out)))
    return f'<ol class="toc">{toc}</ol>' + "\n".join(out)

# ------------------------------------------------------------------ PAGINE
def legal_page(page, lang, path, alts, kw, h1, title, desc, content, note=None):
    note_html = f'<div class="callout">{note}</div>' if note else ""
    body = hero(lang, [(kw, path)], kw, h1)
    body += f'<section class="section" style="padding-top:24px"><div class="wrap"><div class="prose legal">{note_html}{content}</div></div></section>'
    page(path, lang, title, desc, body, alts=alts, crumbs=[(kw, path)])

def build(page):
    pa = {"it": "/privacy/", "en": "/en/privacy/"}
    ca = {"it": "/cookie-policy/", "en": "/en/cookie-policy/"}
    sa = {"it": "/sicurezza/", "en": "/en/security/"}
    en_note = "This is a translation provided for convenience. In case of any discrepancy, the Italian version prevails."
    legal_page(page, "it", "/privacy/", pa, "Privacy", "Privacy policy",
               "Privacy policy | Tymex", "Informativa sul trattamento dei dati personali degli utenti del sito Tymex (Servizi Informatici Srl), ai sensi del Regolamento (UE) 2016/679.",
               privacy_it())
    legal_page(page, "en", "/en/privacy/", pa, "Privacy", "Privacy policy",
               "Privacy policy | Tymex", "Information on the processing of personal data of users of the Tymex website (Servizi Informatici Srl), under Regulation (EU) 2016/679.",
               privacy_en(), note=en_note + ' <a href="/privacy/">Italian version</a>.')
    legal_page(page, "it", "/cookie-policy/", ca, "Cookie", "Cookie policy",
               "Cookie policy | Tymex", "Il sito Tymex non usa cookie né strumenti di tracciamento: statistiche anonime dai log del server con Netlify Analytics.",
               cookie("it"))
    legal_page(page, "en", "/en/cookie-policy/", ca, "Cookies", "Cookie policy",
               "Cookie policy | Tymex", "The Tymex website uses no cookies or tracking tools: anonymous statistics from server logs with Netlify Analytics.",
               cookie("en"), note=en_note + ' <a href="/cookie-policy/">Italian version</a>.')
    legal_page(page, "it", "/sicurezza/", sa, "Sicurezza", "Sicurezza della piattaforma Tymex",
               "Sicurezza: framework, API e servizio cloud | Tymex", "Come è costruita e protetta la piattaforma Tymex: framework Ground'81, ruoli e permessi, API con firma hash, servizio in cloud.",
               security("it"))
    legal_page(page, "en", "/en/security/", sa, "Security", "Tymex platform security",
               "Security: framework, API and cloud service | Tymex", "How the Tymex platform is built and protected: the Ground'81 framework, roles and permissions, hash-signed API, cloud service.",
               security("en"))
    legal_page(page, "it", "/condizioni-generali/", {"it": "/condizioni-generali/"}, "Condizioni generali", "Condizioni generali di contratto",
               "Condizioni generali di contratto | Tymex", "Le condizioni generali di contratto dei prodotti software e dei servizi cloud di Servizi Informatici Srl, tra cui Tymex.",
               terms())
