"""Home, pagine di settore, chi siamo, supporto, grazie, 404 (IT + EN)."""
import json
from html import escape as esc
import icons as I

SITE = "https://www.tymex.it"
APPSTORE = "https://apps.apple.com/it/app/tymex/id1613057170"
PLAY = "https://play.google.com/store/apps/details?id=com.tymex.tymex"
WEBAPP = "https://web.tymex.it"
# Video della serie (YouTube Shorts, verticali), in ordine: (ID, titolo)
VIDEOS = [
    ("lhO6xD6vwys", "Quante ore perdi con i rapportini cartacei? (1/3)"),
    ("VMUY96AAFzM", "Rapportini di lavoro in 3 gesti (2/3)"),
    ("9-0HO5Zl2gU", "84 ore risparmiate sui rapportini? Ecco il calcolo (3/3)"),
]
CHANNEL = "https://www.youtube.com/channel/UC5re37uedr1K2q0xdvCOGiQ"

SECTOR_PATHS = {
    "assistenza": {"it": "/software-assistenza-tecnica/", "en": "/en/field-service-time-tracking-software/"},
    "progettazione": {"it": "/software-per-studi-di-progettazione/", "en": "/en/timesheet-software-engineering-architecture-firms/"},
    "agenzie": {"it": "/software-timesheet-agenzie-pubblicitarie/", "en": "/en/timesheet-software-agencies/"},
    "software": {"it": "/software-timesheet-software-house/", "en": "/en/timesheet-software-it-companies-consultants/"},
}

def lis(items):
    return "".join(f"<li>{x}</li>" for x in items)

def faq_block(items, open_first=False):
    out = []
    for i, (q, a) in enumerate(items):
        op = " open" if (open_first and i == 0) else ""
        out.append(f'<details{op}><summary>{esc(q)}<span class="plus" aria-hidden="true">+</span></summary>'
                   f'<div class="answer">{a}</div></details>')
    return '<div class="faq">' + "".join(out) + "</div>"

def faq_ld(items):
    import re
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", " ", a).replace("  ", " ").strip()}}
        for q, a in items]}

def app_ld(lang):
    return {
        "@type": "SoftwareApplication", "@id": SITE + "/#app", "name": "Tymex",
        "applicationCategory": "BusinessApplication", "operatingSystem": "iOS, Android, Web",
        "url": SITE + ("/" if lang == "it" else "/en/"),
        "description": ("App timesheet per la rilevazione delle ore lavorate su commessa, per iOS, Android e web." if lang == "it"
                        else "Timesheet app to track hours worked on jobs and projects, for iOS, Android and web."),
        "image": SITE + "/img/app-nuovo-rapportino.webp",
        "downloadUrl": [APPSTORE, PLAY], "publisher": {"@id": SITE + "/#org"}, "inLanguage": lang,
    }

# ---------------------------------------------------------------- COPY HOME
HOME = {
 "it": dict(
  path="/", alt="/en/",
  title="Tymex – Software timesheet e rilevazione ore su commessa",
  desc="Tymex è l'app timesheet per rilevare le ore lavorate su commessa da smartphone e web. Controlla costi, avanzamento e marginalità delle commesse senza Excel. Demo gratuita.",
  kw="Software timesheet · Rilevazione ore su commessa",
  claim='Le ore sulle commesse, registrate in <em>pochi secondi</em>.',
  lead="Tecnici, consulenti e collaboratori inseriscono le ore dallo smartphone in pochi tap. Tu controlli costi, avanzamento e marginalità delle commesse in tempo reale, senza fogli Excel.",
  cta1="Richiedi una demo gratuita", cta2="Guarda come funziona",
  checks=["App iOS e Android", "Web app da PC", "Attivo in 3 giorni dall'ordine"],
  badge=("fino al 70%", "di tempo in meno per raccogliere le ore"),
  alt_a="App Tymex: calendario dei rapportini con lo stato di ogni giornata",
  alt_b="App Tymex: schermata Nuovo rapportino con cliente, commessa, servizio e ore lavorate",
  values=[("Veloce", I.BOLT, "Un rapportino si compila in pochi tap: cliente, commessa, servizio, ore. Il giorno dopo lo duplichi con un tocco."),
          ("Semplice", I.CAL, "Il calendario mostra a colpo d'occhio quali giornate sono complete e quali mancano. Nessun corso: si usa come un'app qualsiasi."),
          ("Ovunque", I.PHONE, "App per iPhone e Android per chi lavora fuori sede, web app da PC per l'ufficio. I dati arrivano subito a chi li deve controllare.")],
  how_eyebrow="Come funziona", how_title="Dall'attivazione al controllo delle commesse, in quattro passi.",
  steps=[("Attiva la piattaforma", "Configuriamo Tymex per la tua azienda: è operativo entro 3 giorni dall'ordine."),
         ("Registra le persone", "Inserisci operatori, clienti, commesse e servizi, oppure importali dal gestionale."),
         ("Raccogli le ore", "Ognuno registra le proprie attività da app o web, con controlli che evitano errori e giornate incomplete."),
         ("Controlla le commesse", "Valida i rapportini, esporta i dati e segui avanzamento e marginalità sui cruscotti.")],
  feat_eyebrow="Funzionalità", feat_title="Tutto quello che serve per rilevare le ore. Niente di più.",
  feat_lead="Tymex fa una cosa sola e la fa bene: raccoglie ore e attività in modo ordinato, così chi controlla le commesse ha dati affidabili e aggiornati.",
  feats=[("Ore interne e su commessa", "Inserimento a consuntivo con cliente, commessa e tipo di attività svolta."),
         ("Quadratura con il calendario", "Controlli di coerenza tra ore lavorate e ore previste, giorno per giorno."),
         ("Duplica rapportino", "Le attività ricorrenti si copiano con un tocco, anche dall'app."),
         ("Validazione e blocco", "Stato delle validazioni sempre visibile e modifiche bloccabili fino a una data."),
         ("Ruoli e permessi", "Admin, manager, responsabili che caricano anche per il team, operatori."),
         ("Export CSV", "Rapportini, clienti e commesse esportabili per il gestionale o per Excel.")],
  web_eyebrow="Dall'ufficio e dal campo", web_title="Stessi dati, da telefono e da PC.",
  web_lead="Chi è fuori sede usa l'app per iPhone o Android. In ufficio si lavora dalla web app su web.tymex.it: nessuna installazione, funziona su qualsiasi PC Windows.",
  web_alt="Tymex sul computer (web app) e sullo smartphone (app)",
  data_eyebrow="Leggi i dati", data_title="Cruscotti web, anche su Power BI.",
  data_lead="Ore per cliente, per operatore, per commessa: i cruscotti mostrano dove va il tempo e dove si perde margine. Le giornate non caricate saltano subito all'occhio. Chi usa Microsoft Power BI trova i cruscotti già pronti.",
  data_note="L'uso dei cruscotti su Power BI richiede Microsoft Power BI Pro.",
  data_alt="Cruscotto di Tymex: calendario mensile delle ore per operatore ed elenco dei rapportini",
  sect_eyebrow="Per chi è", sect_title="Pensato per chi lavora su commessa.",
  sectors=[("assistenza", "Assistenza tecnica, impiantisti e manutentori", "Rapportini di intervento digitali, tecnici sul campo, ore per cliente."),
           ("progettazione", "Studi di progettazione", "Ore preventivate e consuntivate, per progetto e per fase."),
           ("agenzie", "Agenzie di comunicazione e marketing", "Tempo per cliente e per attività, anche su forfait e pacchetti ore."),
           ("software", "Software house e consulenti", "Ore su clienti, progetti e attività di sviluppo o consulenza.")],
  more="Scopri di più",
  cmp_title="Excel o Tymex?", cmp_lead="Excel va bene per iniziare. Quando crescono commesse e persone, mostra i suoi limiti.",
  cmp_cols=("Foglio Excel", "Tymex"),
  cmp_rows=[("Inserimento", "Manuale", "Guidato, da app"), ("Dati", "Sparsi in più file", "Archivio unico"),
            ("Errori", "Frequenti", "Controlli automatici"), ("Aggiornamento", "Non immediato", "In tempo reale"),
            ("Analisi", "Manuali", "Cruscotti e report"), ("Da fuori sede", "Scomodo", "App nativa")],
  int_eyebrow="Integrazioni", int_title="Funziona da solo. E, se vuoi, parla con il tuo gestionale.",
  int_lead="Tymex è completo anche usato da solo, via web e app. Quando serve si collega al software gestionale tramite API, per sincronizzare clienti, commesse e operatori e inviare le ore alla contabilità analitica. È già disponibile l'integrazione con eSOLVER di Sistemi Spa.",
  integr=[("Stand-alone", "Web app e app mobile, nessuna installazione sul PC."), ("API", "Lettura e scrittura verso il gestionale aziendale."),
          ("CSV", "Export di rapportini, clienti e commesse."), ("Power BI", "Cruscotti pronti per analizzare le ore.")],
  video_eyebrow="Video", video_title="Guarda Tymex al lavoro.",
  video_lead="Tre video brevi: quanto tempo si perde con i rapportini di carta, come se ne compila uno in tre gesti e quante ore si risparmiano.",
  video_cta="Apri il canale YouTube",
  faq_eyebrow="Domande frequenti", faq_title="Le risposte che cerchi.", faq_all="Tutte le domande frequenti",
  faq=[("Cos'è Tymex?", "Tymex è un software timesheet per la rilevazione delle ore lavorate su commessa. Tecnici, dipendenti e collaboratori registrano attività, ore, clienti e commesse da smartphone o web app; l'azienda monitora costi, avanzamento e marginalità senza fogli Excel."),
       ("Quanto tempo serve per partire?", "Tymex si attiva entro 3 giorni dall'ordine. Dopo l'attivazione basta collegarsi dal browser per creare gli operatori e dare loro l'accesso da app o web."),
       ("Può essere usato da tecnici fuori sede?", "Sì. I tecnici registrano le ore direttamente da smartphone, anche quando lavorano presso i clienti."),
       ("Serve un gestionale per usarlo?", "No. Tymex funziona in modalità stand-alone via web e app. Se usi eSOLVER di Sistemi Spa puoi collegarlo per sincronizzare clienti, commesse, operatori e movimenti di contabilità analitica."),
       ("Su quali dispositivi funziona?", "Su iPhone e smartphone Android tramite app, e su qualsiasi PC tramite la web app su web.tymex.it."),
       ("Come si calcola la marginalità di una commessa?", "Confrontando ricavi e costi della commessa. Con la rilevazione puntuale delle ore lavorate si capisce quali attività generano profitto e quali riducono la redditività. <a href=\"/blog/come-calcolare-la-marginalita-di-una-commessa/\">Leggi la guida completa</a>.")],
 ),
 "en": dict(
  path="/en/", alt="/",
  title="Tymex – Timesheet app for job and project time tracking",
  desc="Tymex is the timesheet app to track hours worked on jobs and projects from smartphone and web. Control job costs, progress and margins without spreadsheets. Free demo.",
  kw="Timesheet software · Job time tracking",
  claim='Hours on every job, logged in <em>seconds</em>.',
  lead="Technicians, consultants and staff log their hours from their phone in a few taps. You see job costs, progress and margins in real time, without spreadsheets.",
  cta1="Book a free demo", cta2="See how it works",
  checks=["iOS and Android apps", "Web app for desktop", "Up and running in 3 days"],
  badge=("up to 70%", "less time spent collecting hours"),
  alt_a="Tymex app: timesheet calendar showing the status of each day",
  alt_b="Tymex app: New timesheet screen with customer, job, service and hours worked",
  values=[("Fast", I.BOLT, "A timesheet entry takes a few taps: customer, job, service, hours. Next day, duplicate it with one tap."),
          ("Simple", I.CAL, "The calendar shows at a glance which days are complete and which are missing. No training needed: it works like any other app."),
          ("Anywhere", I.PHONE, "iPhone and Android apps for people in the field, a web app for the office. Data reaches the people who check it straight away.")],
  how_eyebrow="How it works", how_title="From set-up to job control, in four steps.",
  steps=[("Activate the platform", "We configure Tymex for your company: it's up and running within 3 days of your order."),
         ("Add your people", "Enter staff, customers, jobs and services, or import them from your ERP."),
         ("Collect hours", "Everyone logs their own work from the app or the web, with checks that prevent errors and incomplete days."),
         ("Control your jobs", "Approve timesheets, export data and follow progress and margins on the dashboards.")],
  feat_eyebrow="Features", feat_title="Everything you need to track time. Nothing more.",
  feat_lead="Tymex does one thing and does it well: it collects hours and activities in an orderly way, so whoever controls the jobs has reliable, up-to-date data.",
  feats=[("Internal and job hours", "Log actual hours with customer, job and type of activity."),
         ("Calendar reconciliation", "Consistency checks between hours worked and scheduled hours, day by day."),
         ("Duplicate entries", "Copy recurring activities with one tap, even from the app."),
         ("Approval and locking", "Approval status always visible, and edits can be locked up to a date."),
         ("Roles and permissions", "Admins, managers, team leads who log time for their team, staff."),
         ("CSV export", "Export timesheets, customers and jobs to your ERP or to Excel.")],
  web_eyebrow="Office and field", web_title="Same data, on phone and desktop.",
  web_lead="People in the field use the iPhone or Android app. In the office, the web app at web.tymex.it needs no installation and runs on any Windows PC.",
  web_alt="Tymex on a laptop (web app) and on a smartphone (app)",
  data_eyebrow="Read the data", data_title="Web dashboards, also in Power BI.",
  data_lead="Hours by customer, by person, by job: the dashboards show where time goes and where margin is lost. Days without entries stand out immediately. If you use Microsoft Power BI, the dashboards are ready to go.",
  data_note="Using the dashboards in Power BI requires Microsoft Power BI Pro.",
  data_alt="Tymex dashboard: monthly calendar of hours per person and list of timesheet entries",
  sect_eyebrow="Who it's for", sect_title="Built for businesses that work by the job.",
  sectors=[("assistenza", "Field service, installers and maintenance", "Digital service reports, technicians on the road, hours per customer."),
           ("progettazione", "Engineering and architecture firms", "Budgeted versus actual hours, by project and phase."),
           ("agenzie", "Marketing and communication agencies", "Time per client and activity, including retainers and hour packages."),
           ("software", "IT companies and consultants", "Hours on clients, projects, development and consulting work.")],
  more="Learn more",
  cmp_title="Spreadsheet or Tymex?", cmp_lead="A spreadsheet is fine to start with. As jobs and people grow, its limits show.",
  cmp_cols=("Spreadsheet", "Tymex"),
  cmp_rows=[("Data entry", "Manual", "Guided, from the app"), ("Data", "Spread across files", "One central database"),
            ("Errors", "Frequent", "Automatic checks"), ("Updates", "Delayed", "Real time"),
            ("Analysis", "Manual", "Dashboards and reports"), ("In the field", "Awkward", "Native app")],
  int_eyebrow="Integrations", int_title="Works on its own. And, if you like, talks to your ERP.",
  int_lead="Tymex is complete on its own, on web and app. When needed, it connects to your business software via API to sync customers, jobs and staff and send hours to cost accounting. An integration with eSOLVER by Sistemi Spa is already available.",
  integr=[("Stand-alone", "Web app and mobile app, nothing to install on the PC."), ("API", "Read and write to your business software."),
          ("CSV", "Export timesheets, customers and jobs."), ("Power BI", "Ready-made dashboards to analyse hours.")],
  video_eyebrow="Videos", video_title="See Tymex at work.",
  video_lead="Three short videos (in Italian): how much time paper timesheets cost, how to fill one in with three taps, and how many hours you save.",
  video_cta="Open the YouTube channel",
  faq_eyebrow="FAQ", faq_title="The answers you're looking for.", faq_all="All frequently asked questions",
  faq=[("What is Tymex?", "Tymex is timesheet software for tracking hours worked on jobs and projects. Technicians, employees and contractors log activities, hours, customers and jobs from a smartphone or the web app; the company monitors costs, progress and margins without spreadsheets."),
       ("How long does it take to get started?", "Tymex is activated within 3 days of your order. After that, you simply log in from a browser to create users and give them access via app or web."),
       ("Can technicians in the field use it?", "Yes. Technicians log hours straight from their smartphone, even while working at customer sites."),
       ("Do I need an ERP to use it?", "No. Tymex works stand-alone on web and app. If you use eSOLVER by Sistemi Spa, you can connect it to sync customers, jobs, staff and cost-accounting entries."),
       ("Which devices does it run on?", "On iPhone and Android smartphones via the app, and on any PC via the web app at web.tymex.it."),
       ("How do you calculate a job's margin?", "By comparing a job's revenue with its costs. Tracking hours accurately shows which activities make a profit and which erode it.")],
 ),
}

QUIZ = {
 "it": dict(
  eyebrow="3 domande, 30 secondi", title="Tymex fa per te?",
  q=[("oggi", "Come raccogliete le ore oggi?", [("excel", "Fogli Excel"), ("carta", "Rapportini su carta"), ("software", "Con un altro software"), ("niente", "Non le raccogliamo")]),
     ("chi", "Chi registra le ore?", [("campo", "Tecnici fuori sede"), ("ufficio", "Personale in ufficio"), ("entrambi", "Entrambi")]),
     ("gest", "Usate un gestionale?", [("esolver", "Sì, eSOLVER"), ("altro", "Sì, un altro gestionale"), ("no", "No")])],
  persone="Quante persone registrano le ore? (facoltativo)", back="Indietro", restart="Ricomincia",
  result_title="Ecco cosa può fare Tymex per voi", apply="Richiedi la demo con queste risposte",
  json=dict(intro="In base alle tue risposte:",
            summary="Risposte al selettore «Tymex fa per te?»:",
            q={"oggi": "Raccolta ore oggi:", "chi": "Chi registra:", "gest": "Gestionale:", "persone": "Persone:"},
            oggi={"excel": "Addio file Excel sparsi: le ore finiscono in un unico archivio, già controllate.",
                  "carta": "Niente più rapportini da ricopiare: si compilano dal telefono e arrivano subito in ufficio.",
                  "software": "Tymex è più snello: fa solo la rilevazione ore, così chi la usa non ha niente da imparare.",
                  "niente": "Partire è semplice: in 3 giorni dall'ordine siete operativi e iniziate a vedere dove va il tempo."},
            chi={"campo": "I tecnici usano l'app per iPhone o Android anche presso i clienti.",
                 "ufficio": "In ufficio si usa la web app, senza installare nulla sul PC.",
                 "entrambi": "App per chi è fuori sede e web app per l'ufficio, con gli stessi dati."},
            gest={"esolver": "Con eSOLVER c'è già l'integrazione per clienti, commesse, operatori e contabilità analitica.",
                  "altro": "Tymex si collega ad altri gestionali tramite API o con l'export CSV: ne parliamo nella demo.",
                  "no": "Tymex funziona da solo: clienti e commesse si inseriscono direttamente."}),
 ),
 "en": dict(
  eyebrow="3 questions, 30 seconds", title="Is Tymex right for you?",
  q=[("oggi", "How do you collect hours today?", [("excel", "Spreadsheets"), ("carta", "Paper timesheets"), ("software", "Another software"), ("niente", "We don't")]),
     ("chi", "Who logs the hours?", [("campo", "Field technicians"), ("ufficio", "Office staff"), ("entrambi", "Both")]),
     ("gest", "Do you use an ERP?", [("esolver", "Yes, eSOLVER"), ("altro", "Yes, another one"), ("no", "No")])],
  persone="How many people log hours? (optional)", back="Back", restart="Start over",
  result_title="Here's what Tymex can do for you", apply="Book a demo with these answers",
  json=dict(intro="Based on your answers:",
            summary="Answers to the “Is Tymex right for you?” selector:",
            q={"oggi": "Collecting hours today:", "chi": "Who logs:", "gest": "ERP:", "persone": "People:"},
            oggi={"excel": "No more scattered spreadsheets: hours go into one database, already checked.",
                  "carta": "No more retyping paper sheets: entries are made on the phone and reach the office straight away.",
                  "software": "Tymex is leaner: it only does time tracking, so there's nothing complicated to learn.",
                  "niente": "Getting started is easy: you're up and running 3 days after ordering and can see where time goes."},
            chi={"campo": "Technicians use the iPhone or Android app, even at customer sites.",
                 "ufficio": "Office staff use the web app, with nothing to install.",
                 "entrambi": "An app for the field and a web app for the office, sharing the same data."},
            gest={"esolver": "With eSOLVER there's a ready-made integration for customers, jobs, staff and cost accounting.",
                  "altro": "Tymex connects to other ERPs via API or CSV export: we'll discuss it in the demo.",
                  "no": "Tymex works on its own: customers and jobs are entered directly."}),
 ),
}

CONTACT = {
 "it": dict(id="contatti", title="Vedi Tymex in azione.",
            lead="Una demo gratuita di 30 minuti, sui tuoi casi reali. Compila il modulo: ti ricontattiamo per fissare giorno e ora.",
            name="Nome e cognome", company="Azienda", email="Email", phone="Telefono", users="Quante persone registrano le ore?",
            users_opts=[("1-10", "1–10"), ("11-50", "11–50"), ("50+", "Più di 50")], msg="Messaggio (facoltativo)",
            consent='Ho letto l\'<a href="/privacy/">informativa privacy</a> e acconsento al trattamento dei dati per ricevere una risposta.',
            send="Richiedi la demo", action="/grazie/", req="obbligatorio", addr="Via Sicuri 42/a, 43124 Parma"),
 "en": dict(id="contact", title="See Tymex in action.",
            lead="A free 30-minute demo based on your real cases. Fill in the form and we'll get back to you to set a date and time.",
            name="Full name", company="Company", email="Email", phone="Phone", users="How many people log hours?",
            users_opts=[("1-10", "1–10"), ("11-50", "11–50"), ("50+", "More than 50")], msg="Message (optional)",
            consent='I have read the <a href="/en/privacy/">privacy notice</a> and agree to my data being processed to receive a reply.',
            send="Book the demo", action="/en/thank-you/", req="required", addr="Via Sicuri 42/a, 43124 Parma, Italy"),
}

def contact_section(lang, heading_tag="h2"):
    c = CONTACT[lang]
    opts = "".join(f'<option value="{v}">{esc(t)}</option>' for v, t in c["users_opts"])
    star = f'<span class="req" aria-hidden="true">*</span>'
    return f'''<section class="section" id="{c["id"]}" aria-labelledby="{c["id"]}-title">
<div class="wrap"><div class="contact reveal">
  <div>
    <{heading_tag} class="h-lg" id="{c["id"]}-title" data-split>{esc(c["title"])}</{heading_tag}>
    <p class="lead mt-m">{esc(c["lead"])}</p>
    <ul class="contact-list">
      <li><a href="tel:+390521252824">{I.TEL}0521 252824</a></li>
      <li><a href="mailto:info@tymex.it">{I.MAIL}info@tymex.it</a></li>
      <li><a href="https://www.google.com/maps/search/?api=1&amp;query=Via+Sicuri+42%2Fa+43124+Parma" rel="noopener">{I.PIN}{esc(c["addr"])}</a></li>
    </ul>
  </div>
  <form class="form" id="demo-form" name="demo" method="POST" action="{c["action"]}" data-netlify="true" netlify-honeypot="bot-field">
    <input type="hidden" name="form-name" value="demo">
    <input type="hidden" name="lingua" value="{lang}">
    <input type="hidden" name="selettore" value="">
    <p class="hp"><label>Non compilare <input name="bot-field" tabindex="-1" autocomplete="off"></label></p>
    <label><span>{c["name"]} {star}</span><input type="text" name="nome" autocomplete="name" required></label>
    <label><span>{c["company"]} {star}</span><input type="text" name="azienda" autocomplete="organization" required></label>
    <label><span>{c["email"]} {star}</span><input type="email" name="email" autocomplete="email" required></label>
    <label>{c["phone"]}<input type="tel" name="telefono" autocomplete="tel"></label>
    <label class="full">{c["users"]}<select name="utenti">{opts}</select></label>
    <label class="full">{c["msg"]}<textarea name="messaggio" rows="4"></textarea></label>
    <label class="full consent"><input type="checkbox" name="privacy" value="si" required><span>{c["consent"]} {star}</span></label>
    <button class="btn btn--primary full" type="submit">{c["send"]}</button>
  </form>
</div></div>
</section>'''

def quiz_section(lang):
    q = QUIZ[lang]
    steps = []
    for k, legend, opts in q["q"]:
        b = "".join(f'<button type="button" class="opt" data-value="{v}" aria-pressed="false">{esc(t)}</button>' for v, t in opts)
        back = f'<button type="button" class="back" data-back>{q["back"]}</button>' if k != "oggi" else ""
        steps.append(f'<fieldset data-step="{k}"><legend>{esc(legend)}</legend><div class="opts">{b}</div>{back}</fieldset>')
    steps.append(f'''<div data-step="fine" aria-live="polite">
<h3 class="h-md mt-m" style="color:#fff">{esc(q["result_title"])}</h3>
<div class="result" data-result></div>
<label>{esc(q["persone"])}<input type="number" name="quiz_persone" min="1" inputmode="numeric"></label>
<div class="nav-row"><button type="button" class="btn btn--light" data-apply>{esc(q["apply"])}</button>
<button type="button" class="back" data-restart>{q["restart"]}</button></div></div>''')
    data = json.dumps(q["json"], ensure_ascii=False)
    sid = "selettore" if lang == "it" else "selector"
    return f'''<div class="quiz reveal reveal-d1" id="quiz">
<span class="eyebrow" id="{sid}">{esc(q["eyebrow"])}</span>
<h2 class="h-md">{esc(q["title"])}</h2>
{"".join(steps)}
<div class="progress" aria-hidden="true"><span></span><span></span><span></span><span></span></div>
<script type="application/json">{data}</script>
</div>'''

def home(page, lang):
    L = HOME[lang]
    ids = {"it": ("come-funziona", "funzionalita", "settori", "integrazioni", "faq"),
           "en": ("how-it-works", "features", "industries", "integrations", "faq")}[lang]
    checks = "".join(f"<span>{I.CHECK}{esc(c)}</span>" for c in L["checks"])
    values = "".join(
        f'<div class="card reveal reveal-d{i+1}"><div class="tile-ico">{ic}</div><h3>{esc(h)}</h3><p>{esc(p)}</p></div>'
        for i, (h, ic, p) in enumerate(L["values"]))
    steps = "".join(
        f'<div class="step reveal reveal-d{i % 4}"><div class="num">0{i+1}</div><h3>{esc(h)}</h3><p>{esc(p)}</p></div>'
        for i, (h, p) in enumerate(L["steps"]))
    feats = "".join(f'<div class="card--line reveal"><h3>{esc(h)}</h3><p>{esc(p)}</p></div>' for h, p in L["feats"])
    sectors = "".join(
        f'<a class="sector-card sc-{i+1} reveal reveal-d{i % 4}" href="{SECTOR_PATHS[k][lang]}"><span class="n">0{i+1}</span>'
        f'<span class="t">{esc(t)}</span><span class="d">{esc(d)}</span><span class="more">{L["more"]} →</span></a>'
        for i, (k, t, d) in enumerate(L["sectors"]))
    c1, c2 = L["cmp_cols"]
    rows = "".join(
        f'<tr><th scope="row">{esc(a)}</th><td data-label="{esc(c1)}">{esc(b)}</td><td class="us" data-label="{esc(c2)}">{esc(c)}</td></tr>'
        for a, b, c in L["cmp_rows"])
    integr = "".join(f"<div><strong>{esc(h)}</strong><span>{esc(p)}</span></div>" for h, p in L["integr"])
    cards = []
    for i, (vid, title) in enumerate(VIDEOS):
        cards.append(f'<li class="reveal reveal-d{i}"><button class="video-card video-card--v" type="button" data-video="{vid}" data-video-format="vertical" data-video-title="{esc(title)}">'
                     f'<img src="/img/video-{i+1}.webp" width="540" height="960" alt="" loading="lazy"><span class="play">{I.PLAY}</span></button>'
                     f'<p class="video-title">{esc(title)}</p></li>')
    video_html = '<ul class="video-row">' + "".join(cards) + "</ul>"
    faq_link = "/faq-timesheet/" if lang == "it" else "/en/faq/"
    body = f'''
<section class="hero">
  {I.DECO_BARS}
  <div class="wrap hero-grid">
    <div>
      <h1 class="h-xl"><span class="kw intro" style="--d:0">{esc(L["kw"])}</span><span class="claim intro" style="--d:1">{L["claim"]}</span></h1>
      <p class="lead intro" style="--d:2">{esc(L["lead"])}</p>
      <div class="btn-row intro" style="--d:3">
        <a class="btn btn--primary" href="#{CONTACT[lang]["id"]}">{esc(L["cta1"])}</a>
        <a class="btn btn--ghost" href="#{ids[0]}">{esc(L["cta2"])}</a>
      </div>
      <div class="check-row intro" style="--d:4">{checks}</div>
    </div>
    <div class="hero-visual intro" style="--d:2">
      <div class="phone phone--a" data-parallax="0.05"><img src="/img/app-calendario.webp" width="600" height="1233" alt="{esc(L["alt_a"])}" fetchpriority="high"></div>
      <div class="phone phone--b" data-parallax="0.1"><img src="/img/app-nuovo-rapportino.webp" width="600" height="1298" alt="{esc(L["alt_b"])}" fetchpriority="high"></div>
      <div class="hero-badge"><div class="tile" style="color:#fff">{I.CLOCK}</div><div><strong>{esc(L["badge"][0])}</strong><span>{esc(L["badge"][1])}</span></div></div>
    </div>
  </div>
</section>

<section class="section" style="padding-top:24px" aria-label="{'Punti di forza' if lang == 'it' else 'Key benefits'}">
  <div class="wrap grid grid--3">{values}</div>
</section>

<section class="section section--dark" id="{ids[0]}">
  <div class="wrap">
    <span class="eyebrow">{esc(L["how_eyebrow"])}</span>
    <h2 class="h-lg" style="max-width:760px" data-split>{esc(L["how_title"])}</h2>
    <div class="steps">{steps}</div>
  </div>
</section>

<section class="section" id="{ids[1]}">
  <div class="wrap split split--top">
    <div>
      <span class="eyebrow">{esc(L["feat_eyebrow"])}</span>
      <h2 class="h-lg" data-split>{esc(L["feat_title"])}</h2>
      <p class="lead mt-m">{esc(L["feat_lead"])}</p>
      <div class="btn-row mt-m"><a class="btn btn--primary" href="#{CONTACT[lang]["id"]}">{esc(L["cta1"])}</a></div>
    </div>
    <div class="grid grid--2">{feats}</div>
  </div>
</section>

<section class="section section--tint">
  <div class="wrap split split--rev">
    <div class="media reveal"><img src="/img/tymex-web-e-app.webp" width="1200" height="800" alt="{esc(L["web_alt"])}" loading="lazy" data-parallax="0.04"></div>
    <div>
      <span class="eyebrow">{esc(L["web_eyebrow"])}</span>
      <h2 class="h-lg" data-split>{esc(L["web_title"])}</h2>
      <p class="lead mt-m">{esc(L["web_lead"])}</p>
      <div class="btn-row mt-m">
        <a class="btn btn--ghost" href="{APPSTORE}" rel="noopener">{I.APPLE} App Store</a>
        <a class="btn btn--ghost" href="{PLAY}" rel="noopener">{I.ANDROID} Google Play</a>
        <a class="btn btn--ghost" href="{WEBAPP}">{I.GLOBE} web.tymex.it</a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div>
      <span class="eyebrow">{esc(L["data_eyebrow"])}</span>
      <h2 class="h-lg" data-split>{esc(L["data_title"])}</h2>
      <p class="lead mt-m">{esc(L["data_lead"])}</p>
      <p class="note mt-m">{esc(L["data_note"])}</p>
    </div>
    <div class="frame reveal"><img src="/img/cruscotto-ore-operatore.webp" width="1400" height="629" alt="{esc(L["data_alt"])}" loading="lazy"></div>
  </div>
</section>

<section class="section" id="{ids[2]}" style="padding-top:0">
  <div class="wrap">
    <span class="eyebrow">{esc(L["sect_eyebrow"])}</span>
    <h2 class="h-lg" data-split>{esc(L["sect_title"])}</h2>
    <div class="grid grid--4 mt-l">{sectors}</div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap split split--wl">
    <div class="box reveal">
      <h2 class="h-md">{esc(L["cmp_title"])}</h2>
      <p class="mt-s" style="color:var(--muted)">{esc(L["cmp_lead"])}</p>
      <table class="compare mt-m">
        <thead><tr><th scope="col"><span hidden>—</span></th><th scope="col">{esc(c1)}</th><th scope="col" class="us">{esc(c2)}</th></tr></thead>
        <tbody>{rows}</tbody>
      </table>
    </div>
    {quiz_section(lang)}
  </div>
</section>

<section class="section section--dark" id="{ids[3]}">
  <div class="wrap split">
    <div>
      <span class="eyebrow">{esc(L["int_eyebrow"])}</span>
      <h2 class="h-lg" data-split>{esc(L["int_title"])}</h2>
      <p class="lead mt-m">{esc(L["int_lead"])}</p>
    </div>
    <div class="integr reveal">{integr}</div>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div>
      <span class="eyebrow">{esc(L["video_eyebrow"])}</span>
      <h2 class="h-lg" data-split>{esc(L["video_title"])}</h2>
      <p class="lead mt-m">{esc(L["video_lead"])}</p>
      <div class="btn-row mt-m"><a class="btn btn--ghost" href="{CHANNEL}" rel="noopener">{esc(L["video_cta"])}</a></div>
    </div>
    <div>{video_html}</div>
  </div>
</section>

<section class="section section--tint" id="{ids[4]}">
  <div class="wrap">
    <div class="center"><span class="eyebrow">{esc(L["faq_eyebrow"])}</span><h2 class="h-lg" data-split>{esc(L["faq_title"])}</h2></div>
    <div class="mt-l">{faq_block(L["faq"], True)}</div>
    <p class="center mt-m"><a href="{faq_link}" style="font-weight:700">{esc(L["faq_all"])} →</a></p>
  </div>
</section>

{contact_section(lang)}
'''
    page(L["path"], lang, L["title"], L["desc"], body, alts={"it": "/", "en": "/en/"},
         ld=[app_ld(lang), faq_ld(L["faq"]),
             {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": "Tymex", "publisher": {"@id": SITE + "/#org"}, "inLanguage": ["it", "en"]}])

# ---------------------------------------------------------------- SETTORI
SECTORS = {
"assistenza": {
 "illu": I.ILLU_FIELD,
 "it": dict(crumb="Assistenza tecnica",
  title="Software assistenza tecnica: rapportini, interventi e ore lavorate | Tymex",
  desc="Tymex è il software per aziende di assistenza tecnica, impiantisti e manutentori: rapportini di intervento digitali, ore dei tecnici e controllo delle commesse da smartphone.",
  kw="Software per assistenza tecnica", h1="Interventi, tecnici e ore lavorate sotto controllo.",
  lead="Le aziende di assistenza tecnica coordinano ogni giorno tecnici, interventi, clienti e commesse. Con fogli Excel, email o rapportini cartacei diventa difficile controllare le attività svolte e la redditività degli interventi. Tymex registra attività, ore e commesse in modo semplice e immediato.",
  illu_label="Illustrazione: un tecnico compila il rapportino dallo smartphone presso il cliente",
  prob_title="I problemi più comuni", prob=["rapportini compilati in ritardo", "ore lavorate non registrate correttamente", "difficoltà nel controllo delle commesse", "poca visibilità sugli interventi", "troppo lavoro amministrativo", "fogli Excel non aggiornati"],
  prob_out="Queste criticità rendono più complesso il controllo dei costi e la pianificazione delle attività.",
  how_title="Come funziona Tymex", how_lead="Il tecnico registra rapidamente le informazioni dell'intervento. Ogni attività è associata a:",
  how=["cliente", "commessa", "attività svolta", "data", "ore lavorate"], how_out="I dati vengono raccolti in tempo reale e sono subito disponibili ai responsabili.",
  blocks=[("Gestione delle ore lavorate", ["registrare le ore direttamente da smartphone", "associare le ore agli interventi", "monitorare il tempo dedicato ai clienti", "controllare il carico di lavoro delle risorse"]),
          ("Rapportini di intervento digitali", ["attività svolte", "tempo impiegato", "commessa e cliente", "note operative", "spese aggiuntive"]),
          ("Tecnici sul campo", ["monitorare attività e interventi", "raccogliere informazioni in tempo reale", "ridurre gli errori di comunicazione", "pianificare meglio le risorse"]),
          ("Controllo di commesse e marginalità", ["conoscere il tempo dedicato a ogni cliente", "calcolare il costo reale degli interventi", "confrontare costi e ricavi", "individuare gli interventi poco redditizi"])],
  who_title="Per chi è", who=["manutenzione impianti", "assistenza tecnica", "installazione impianti", "facility management", "manutenzione industriale", "servizi tecnici sul campo"],
  cmp=True,
  faq=[("Cos'è un software per assistenza tecnica?", "È una soluzione che permette di gestire interventi, attività, tecnici e ore lavorate in modo centralizzato."),
       ("Tymex è adatto ai tecnici che lavorano fuori sede?", "Sì. L'app si usa direttamente da smartphone durante gli interventi presso i clienti."),
       ("Tymex sostituisce i rapportini cartacei?", "Sì. Le attività si registrano in digitale, riducendo errori e tempi amministrativi."),
       ("Tymex è utile per i manutentori?", "Sì. Permette di monitorare interventi, ore lavorate e commesse in modo semplice e strutturato."),
       ("È possibile controllare la marginalità degli interventi?", "Sì. Le informazioni raccolte aiutano a valutare costi, tempi e redditività delle attività svolte.")],
  cta_title="Vuoi migliorare la gestione degli interventi tecnici?", cta_lead="Scopri in una demo come Tymex aiuta a monitorare attività, ore lavorate e commesse."),
 "en": dict(crumb="Field service",
  title="Field service time tracking software: service reports and technician hours | Tymex",
  desc="Tymex is time tracking software for field service, installation and maintenance companies: digital service reports, technician hours and job control from a smartphone.",
  kw="Field service time tracking software", h1="Service calls, technicians and hours under control.",
  lead="Field service companies coordinate technicians, service calls, customers and jobs every day. With spreadsheets, emails or paper reports it's hard to know what was done and whether each call was profitable. Tymex records activities, hours and jobs simply and instantly.",
  illu_label="Illustration: a technician fills in a service report on a smartphone at the customer's site",
  prob_title="The most common problems", prob=["service reports filled in late", "hours worked not recorded properly", "hard-to-control job costs", "little visibility on service calls", "too much admin work", "out-of-date spreadsheets"],
  prob_out="These issues make cost control and planning harder.",
  how_title="How Tymex works", how_lead="Technicians quickly log the details of each call. Every activity is linked to:",
  how=["customer", "job", "activity", "date", "hours worked"], how_out="Data is collected in real time and is immediately available to managers.",
  blocks=[("Hours worked", ["log hours straight from a smartphone", "link hours to service calls", "track time spent per customer", "keep an eye on each person's workload"]),
          ("Digital service reports", ["work carried out", "time spent", "job and customer", "operational notes", "additional expenses"]),
          ("Technicians in the field", ["monitor activities and calls", "collect information in real time", "reduce miscommunication", "plan resources better"]),
          ("Job and margin control", ["know the time spent on each customer", "work out the real cost of each call", "compare costs and revenue", "spot unprofitable calls"])],
  who_title="Who it's for", who=["plant maintenance", "technical support", "installation", "facility management", "industrial maintenance", "field services"],
  cmp=True,
  faq=[("What is field service software?", "It's a tool to manage service calls, activities, technicians and hours worked in one place."),
       ("Is Tymex suitable for technicians working off-site?", "Yes. The app is used directly on a smartphone during visits to customers."),
       ("Does Tymex replace paper service reports?", "Yes. Activities are recorded digitally, cutting errors and admin time."),
       ("Is Tymex useful for maintenance companies?", "Yes. It lets you monitor service calls, hours worked and jobs in a simple, structured way."),
       ("Can I check the margin on each service call?", "Yes. The data collected helps you assess the costs, time and profitability of the work done.")],
  cta_title="Want to manage service calls better?", cta_lead="See in a demo how Tymex helps you track activities, hours and jobs."),
},
"progettazione": {
 "illu": I.ILLU_PROJECT,
 "it": dict(crumb="Studi di progettazione",
  title="Software per studi di progettazione: rilevazione ore e controllo commesse | Tymex",
  desc="Tymex aiuta studi di architettura, ingegneria e progettazione a registrare le ore per progetto, confrontare ore preventivate e consuntivate e controllare la marginalità.",
  kw="Software per studi di progettazione", h1="Sai quanto ti costa davvero ogni progetto?",
  lead="Negli studi di progettazione il tempo è la risorsa principale. Progetti, revisioni, incontri con i clienti e attività tecniche vanno monitorati con precisione. Con Tymex progettisti, architetti e ingegneri registrano le ore dedicate a ogni progetto in modo semplice e strutturato.",
  illu_label="Illustrazione: barre di avanzamento delle ore di tre progetti rispetto al budget",
  prob_title="Problemi tipici degli studi", prob=["scarsa visibilità sui costi", "difficoltà nel controllo delle commesse", "errori di rendicontazione", "impossibilità di valutare la redditività dei progetti"],
  prob_out="Molti studi usano ancora fogli Excel o registrazioni manuali per monitorare le ore lavorate.",
  how_title="Ore preventivate e ore consuntivate", how_lead="Il problema più comune è la differenza tra il tempo stimato nel preventivo e quello realmente impiegato. Con Tymex puoi confrontare:",
  how=["ore preventivate", "ore consuntivate", "costi stimati", "costi reali"], how_out="Così individui subito gli scostamenti e rendi più precisi i preventivi futuri.",
  blocks=[("Registrazione ore per progetto", ["cliente", "progetto", "fase progettuale", "attività"]),
          ("Monitoraggio del budget", ["ore preventivate", "ore consuntivate", "costi effettivi"]),
          ("Analisi della redditività", ["quali commesse sono profittevoli", "quali attività assorbono più risorse", "quali clienti generano più redditività"])],
  who_title="Quali studi usano Tymex", who=["studi di architettura", "studi di ingegneria", "progettazione impiantistica", "progettazione meccanica", "progettazione civile", "progettazione industriale", "studi tecnici multidisciplinari"],
  cmp=False,
  faq=[("Perché uno studio dovrebbe rilevare le ore?", "Perché il tempo di architetti, ingegneri e collaboratori è la principale voce di costo: senza una rilevazione accurata non si conosce il costo reale dei progetti."),
       ("Posso registrare le ore per fase progettuale?", "Sì. Ogni collaboratore associa le ore a cliente, progetto, fase e attività."),
       ("Tymex aiuta a fare preventivi più precisi?", "Sì. Il confronto tra ore preventivate e consuntivate mostra gli scostamenti e aiuta a stimare meglio i progetti futuri.")],
  cta_title="Vuoi sapere quali progetti sono davvero profittevoli?", cta_lead="Scopri come Tymex aiuta studi di architettura, ingegneria e progettazione a controllare ore, costi e marginalità."),
 "en": dict(crumb="Engineering & architecture firms",
  title="Timesheet software for engineering and architecture firms | Tymex",
  desc="Tymex helps architecture, engineering and design firms log hours per project, compare budgeted and actual hours and keep project margins under control.",
  kw="Timesheet software for design firms", h1="Do you know what each project really costs you?",
  lead="In design firms, time is the main resource. Projects, revisions, client meetings and technical work all need to be tracked accurately. With Tymex, designers, architects and engineers log the hours spent on each project simply and consistently.",
  illu_label="Illustration: progress bars of hours on three projects compared with budget",
  prob_title="Typical problems in design firms", prob=["poor visibility on costs", "hard-to-control projects", "reporting errors", "no way to assess project profitability"],
  prob_out="Many firms still use spreadsheets or manual records to track hours worked.",
  how_title="Budgeted versus actual hours", how_lead="The most common problem is the gap between the time estimated in the quote and the time actually spent. With Tymex you can compare:",
  how=["budgeted hours", "actual hours", "estimated costs", "actual costs"], how_out="So you spot overruns immediately and make future quotes more accurate.",
  blocks=[("Hours per project", ["client", "project", "design phase", "activity"]),
          ("Budget tracking", ["budgeted hours", "actual hours", "actual costs"]),
          ("Profitability analysis", ["which projects are profitable", "which activities use the most resources", "which clients are most profitable"])],
  who_title="Which firms use Tymex", who=["architecture firms", "engineering firms", "MEP design", "mechanical design", "civil engineering", "industrial design", "multidisciplinary practices"],
  cmp=False,
  faq=[("Why should a design firm track hours?", "Because the time of architects, engineers and staff is the main cost: without accurate tracking you can't know what projects really cost."),
       ("Can I log hours by design phase?", "Yes. Each person links their hours to client, project, phase and activity."),
       ("Does Tymex help make quotes more accurate?", "Yes. Comparing budgeted and actual hours shows the gaps and helps you estimate future projects better.")],
  cta_title="Want to know which projects really pay?", cta_lead="See how Tymex helps architecture, engineering and design firms control hours, costs and margins."),
},
"agenzie": {
 "illu": I.ILLU_AGENCY,
 "it": dict(crumb="Agenzie di comunicazione",
  title="Software timesheet per agenzie pubblicitarie e di marketing | Tymex",
  desc="Tymex aiuta agenzie pubblicitarie, di marketing e web agency a registrare il tempo per cliente e attività e a capire quali clienti e progetti sono davvero profittevoli.",
  kw="Software timesheet per agenzie", h1="Quali clienti ti fanno guadagnare davvero?",
  lead="Le agenzie pubblicitarie e di marketing lavorano su decine di clienti, campagne e progetti insieme. Senza una rilevazione delle ore è difficile capire quali attività rendono e quali assorbono più risorse del previsto. Con Tymex account, creativi, grafici, consulenti e project manager registrano il tempo dedicato a ogni cliente.",
  illu_label="Illustrazione: grafico a torta del tempo dedicato ai diversi clienti",
  prob_title="Perché le agenzie perdono marginalità", prob=["si lavora a progetto, a forfait, a canone o a pacchetto ore", "le ore non registrate non si vedono", "le attività extra non vengono conteggiate", "manca visibilità sui progetti"],
  prob_out="La rilevazione delle ore permette di confrontare tempo impiegato, budget e ricavi in modo oggettivo.",
  how_title="Attività che puoi monitorare", how_lead="Ogni ora si associa al cliente e all'attività svolta, ad esempio:",
  how=["SEO", "Google Ads", "social media management", "content marketing", "copywriting", "graphic design", "web design", "sviluppo siti web", "email marketing", "riunioni con il cliente", "project management"], how_out="",
  blocks=[("Redditività dei clienti", ["capire quali clienti generano margine", "confrontare ore e budget dei contratti"]),
          ("Tempo dedicato", ["conoscere il tempo reale di ogni attività", "vedere dove si concentra il lavoro"]),
          ("Gestione del team", ["monitorare il carico di lavoro delle persone", "distribuire meglio le attività"]),
          ("Addio Excel", ["informazioni centralizzate in un unico sistema", "dati aggiornati, senza file da unire"])],
  who_title="Chi può usare Tymex", who=["agenzie pubblicitarie", "agenzie di marketing", "agenzie digitali", "web agency", "agenzie SEO", "studi grafici", "società di comunicazione"],
  cmp=False,
  faq=[("Perché un'agenzia dovrebbe rilevare le ore?", "Perché molte agenzie fatturano a progetto, a forfait, a canone o a pacchetto ore: senza dati precisi è impossibile sapere se un cliente è davvero profittevole."),
       ("Posso vedere il tempo per cliente e per attività?", "Sì. Ogni registrazione è legata a cliente, progetto e attività, e i cruscotti mostrano dove va il tempo."),
       ("È utile anche per i contratti a forfait?", "Sì. Confrontando ore impiegate e importo del contratto capisci se il forfait è sostenibile.")],
  cta_title="Vuoi sapere quali progetti sono davvero profittevoli?", cta_lead="Scopri come Tymex può aiutare la tua agenzia a monitorare ore, clienti e progetti."),
 "en": dict(crumb="Marketing agencies",
  title="Timesheet software for advertising and marketing agencies | Tymex",
  desc="Tymex helps advertising, marketing and web agencies log time per client and activity and see which clients and projects are really profitable.",
  kw="Timesheet software for agencies", h1="Which clients really make you money?",
  lead="Advertising and marketing agencies work on dozens of clients, campaigns and projects at once. Without time tracking it's hard to see which activities pay and which take more resources than planned. With Tymex, account managers, creatives, designers, consultants and project managers log the time they spend on each client.",
  illu_label="Illustration: pie chart of time spent on different clients",
  prob_title="Why agencies lose margin", prob=["work billed per project, fixed fee, retainer or hour package", "unlogged hours stay invisible", "extra work isn't counted", "little visibility on projects"],
  prob_out="Tracking hours lets you compare time spent, budget and revenue objectively.",
  how_title="Activities you can track", how_lead="Every hour is linked to the client and the activity, for example:",
  how=["SEO", "Google Ads", "social media management", "content marketing", "copywriting", "graphic design", "web design", "website development", "email marketing", "client meetings", "project management"], how_out="",
  blocks=[("Client profitability", ["see which clients generate margin", "compare hours with contract budgets"]),
          ("Time spent", ["know the real time of each activity", "see where the work piles up"]),
          ("Team management", ["monitor each person's workload", "share out work more evenly"]),
          ("Goodbye spreadsheets", ["all information in one system", "up-to-date data, no files to merge"])],
  who_title="Who can use Tymex", who=["advertising agencies", "marketing agencies", "digital agencies", "web agencies", "SEO agencies", "graphic design studios", "communication companies"],
  cmp=False,
  faq=[("Why should an agency track hours?", "Because many agencies bill per project, fixed fee, retainer or hour package: without precise data you can't tell whether a client is really profitable."),
       ("Can I see time per client and per activity?", "Yes. Each entry is linked to client, project and activity, and the dashboards show where time goes."),
       ("Is it useful for fixed-fee contracts?", "Yes. Comparing hours spent with the contract value shows whether the fee is sustainable.")],
  cta_title="Want to know which projects really pay?", cta_lead="See how Tymex can help your agency track hours, clients and projects."),
},
"software": {
 "illu": I.ILLU_CODE,
 "it": dict(crumb="Software house e consulenti",
  title="Software timesheet per software house, aziende IT e consulenti | Tymex",
  desc="Tymex aiuta software house, aziende IT e consulenti a registrare le ore dedicate a clienti, progetti, sviluppo e assistenza, e a controllare la marginalità delle commesse.",
  kw="Timesheet per software house e consulenti", h1="Ogni ora di sviluppo e consulenza, al suo posto.",
  lead="Software house, aziende IT e consulenti vendono tempo: progetti di sviluppo, assistenza, formazione, consulenza. Tymex permette a sviluppatori e consulenti di registrare le ore dedicate a clienti, progetti e attività, anche quando lavorano fuori sede.",
  illu_label="Illustrazione: finestra di codice con un cronometro",
  prob_title="Quando servono dati sulle ore", prob=["progetti a corpo che sforano il budget", "assistenza e supporto non conteggiati", "ore interne mescolate a ore sui clienti", "rendicontazione a fine mese fatta a memoria"],
  prob_out="Senza una rilevazione puntuale è difficile capire quali commesse rendono davvero.",
  how_title="Come funziona", how_lead="Ogni registrazione è associata a:",
  how=["cliente", "commessa o progetto", "servizio (sviluppo, assistenza, formazione…)", "ore lavorate", "note"], how_out="I dati sono subito disponibili per la fatturazione e il controllo di gestione.",
  blocks=[("Ore su clienti e progetti", ["registrazione da app o da web", "ore interne e ore su commessa separate", "duplica rapportino per le attività ricorrenti"]),
          ("Controllo delle commesse", ["ore consuntivate per commessa", "confronto tra costi e ricavi", "export CSV per la fatturazione"]),
          ("Team e consulenti esterni", ["ruoli e permessi", "validazione dei rapportini", "blocco delle modifiche fino a una data"])],
  who_title="Per chi è", who=["software house", "aziende IT", "system integrator", "consulenti", "società di consulenza", "supporto software"],
  cmp=False,
  faq=[("Tymex è adatto alle software house?", "Sì. Tymex può essere usato da software house e aziende IT per registrare le ore dedicate a clienti, progetti e attività di sviluppo."),
       ("Posso separare ore interne e ore sui clienti?", "Sì. L'inserimento a consuntivo distingue ore interne e ore su commessa."),
       ("Posso esportare le ore per la fatturazione?", "Sì. Rapportini, clienti e commesse si esportano in CSV.")],
  cta_title="Vuoi vedere dove va il tempo del tuo team?", cta_lead="In una demo di 30 minuti ti mostriamo Tymex sui tuoi progetti."),
 "en": dict(crumb="IT companies & consultants",
  title="Timesheet software for IT companies, software houses and consultants | Tymex",
  desc="Tymex helps software houses, IT companies and consultants log hours spent on clients, projects, development and support, and keep job margins under control.",
  kw="Timesheet software for IT and consultants", h1="Every hour of development and consulting, in its place.",
  lead="Software houses, IT companies and consultants sell time: development projects, support, training, consulting. Tymex lets developers and consultants log the hours they spend on clients, projects and activities, even when they work off-site.",
  illu_label="Illustration: code window with a stopwatch",
  prob_title="When you need data on hours", prob=["fixed-price projects running over budget", "support work not counted", "internal hours mixed with client hours", "month-end reporting done from memory"],
  prob_out="Without accurate tracking it's hard to know which jobs really pay.",
  how_title="How it works", how_lead="Each entry is linked to:",
  how=["client", "job or project", "service (development, support, training…)", "hours worked", "notes"], how_out="Data is immediately available for invoicing and management control.",
  blocks=[("Hours on clients and projects", ["log from the app or the web", "internal and job hours kept separate", "duplicate entries for recurring work"]),
          ("Job control", ["actual hours per job", "cost versus revenue comparison", "CSV export for invoicing"]),
          ("Team and external consultants", ["roles and permissions", "timesheet approval", "edits locked up to a date"])],
  who_title="Who it's for", who=["software houses", "IT companies", "system integrators", "consultants", "consulting firms", "software support"],
  cmp=False,
  faq=[("Is Tymex suitable for software houses?", "Yes. Software houses and IT companies use Tymex to log hours spent on clients, projects and development work."),
       ("Can I keep internal and client hours separate?", "Yes. Entries distinguish internal hours from job hours."),
       ("Can I export hours for invoicing?", "Yes. Timesheets, customers and jobs can be exported to CSV.")],
  cta_title="Want to see where your team's time goes?", cta_lead="In a 30-minute demo we'll show you Tymex on your own projects."),
},
}

def sector_page(page, key, lang):
    S = SECTORS[key]
    L = S[lang]
    path = SECTOR_PATHS[key][lang]
    cta = HOME[lang]["cta1"]
    cta_href = "/#contatti" if lang == "it" else "/en/#contact"
    sectors_label = "Settori" if lang == "it" else "Industries"
    blocks = "".join(f'<div class="card--line reveal"><h3>{esc(h)}</h3><ul class="list-check mt-s">{lis(map(esc, items))}</ul></div>'
                     for h, items in L["blocks"])
    pills = lis(map(esc, L["who"]))
    how_out = f'<p class="lead mt-m">{esc(L["how_out"])}</p>' if L["how_out"] else ""
    cmp_html = ""
    if L["cmp"]:
        H = HOME[lang]
        c1, c2 = H["cmp_cols"]
        rows = "".join(f'<tr><th scope="row">{esc(a)}</th><td data-label="{esc(c1)}">{esc(b)}</td><td class="us" data-label="{esc(c2)}">{esc(c)}</td></tr>'
                       for a, b, c in H["cmp_rows"])
        cmp_html = f'''<section class="section" style="padding-top:0"><div class="wrap"><div class="box reveal" style="max-width:880px;margin:0 auto">
<h2 class="h-md">{esc(H["cmp_title"])}</h2><p class="mt-s" style="color:var(--muted)">{esc(H["cmp_lead"])}</p>
<table class="compare mt-m"><thead><tr><th scope="col"><span hidden>—</span></th><th scope="col">{esc(c1)}</th><th scope="col" class="us">{esc(c2)}</th></tr></thead><tbody>{rows}</tbody></table>
</div></div></section>'''
    faq_t = "Domande frequenti" if lang == "it" else "Frequently asked questions"
    body = f'''
<section class="page-hero">
  <div class="wrap split">
    <div>
      {{CRUMBS}}
      <h1><span class="kw intro" style="--d:0">{esc(L["kw"])}</span><span class="intro" style="--d:1;display:block">{esc(L["h1"])}</span></h1>
      <p class="lead intro" style="--d:2">{esc(L["lead"])}</p>
      <div class="btn-row intro" style="--d:3"><a class="btn btn--primary" href="{cta_href}">{esc(cta)}</a></div>
    </div>
    <div class="intro" style="--d:2" data-parallax="0.04">{S["illu"].format(label=esc(L["illu_label"]))}</div>
  </div>
</section>

<section class="section">
  <div class="wrap split split--top">
    <div class="box reveal">
      <h2 class="h-md">{esc(L["prob_title"])}</h2>
      <ul class="list-check mt-m">{lis(map(esc, L["prob"]))}</ul>
      <p class="mt-m" style="color:var(--muted)">{esc(L["prob_out"])}</p>
    </div>
    <div>
      <h2 class="h-lg" data-split>{esc(L["how_title"])}</h2>
      <p class="lead mt-m">{esc(L["how_lead"])}</p>
      <ul class="pills mt-m">{lis(map(esc, L["how"]))}</ul>
      {how_out}
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="wrap">
    <div class="split">
      <div><h2 class="h-lg" data-split>{"Come ti aiuta Tymex" if lang == "it" else "How Tymex helps"}</h2></div>
      <div class="frame reveal" style="max-width:260px;justify-self:center;padding:9px;border-radius:40px;background:var(--ink-2)"><img src="/img/app-nuovo-rapportino.webp" width="600" height="1298" alt="{esc(HOME[lang]["alt_b"])}" loading="lazy" style="border-radius:32px"></div>
    </div>
    <div class="grid grid--2 mt-l">{blocks}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <h2 class="h-lg" data-split>{esc(L["who_title"])}</h2>
    <ul class="pills mt-m">{pills}</ul>
  </div>
</section>

{cmp_html}

<section class="section section--tint">
  <div class="wrap">
    <h2 class="h-lg center" data-split>{faq_t}</h2>
    <div class="mt-l">{faq_block([(q, esc(a)) for q, a in L["faq"]])}</div>
  </div>
</section>

<section class="section">
  <div class="wrap"><div class="cta-band reveal">
    <div><h2 class="h-lg">{esc(L["cta_title"])}</h2><p>{esc(L["cta_lead"])}</p></div>
    <a class="btn btn--light" href="{cta_href}">{esc(cta)}</a>
  </div></div>
</section>
'''
    crumbs = [(sectors_label, "/#settori" if lang == "it" else "/en/#industries"), (L["crumb"], path)]
    import build
    body = body.replace("{CRUMBS}", build.breadcrumbs_html(lang, crumbs))
    page(path, lang, L["title"], L["desc"], body, alts=SECTOR_PATHS[key], crumbs=crumbs,
         ld=[faq_ld([(q, a) for q, a in L["faq"]]),
             {"@type": "WebPage", "name": L["title"], "about": {"@id": SITE + "/#app"}, "inLanguage": lang}])

# ---------------------------------------------------------------- CHI SIAMO, SUPPORTO
def about(page, lang):
    import build
    if lang == "it":
        path, crumbs = "/chi-siamo/", [("Chi siamo", "/chi-siamo/")]
        title = "Chi siamo – Servizi Informatici Srl, Parma | Tymex"
        desc = "Tymex è sviluppato da Servizi Informatici Srl di Parma, partner Sistemi dal 1990, in collaborazione con Web 81, per semplificare la raccolta delle ore."
        h1 = "Servizi Informatici Srl, dal 1990 a Parma."
        kw = "Chi siamo"
        paras = ["Servizi Informatici Srl nasce nel 1990 e diventa subito concessionario certificato Sistemi Spa per le province di Parma, Piacenza e Reggio Emilia.",
                 "Grazie alle competenze e alle certificazioni ottenute riceve la qualifica di Sistemi Città e la denominazione di Sistemi Parma.",
                 "Negli anni sviluppa competenze soprattutto per gli studi commercialisti (linea Profis) e per le aziende (linee Spring SQL ed eSOLVER).",
                 "Realizziamo siti web per aziende e studi e integriamo tramite API i nostri software con e-commerce, app e servizi cloud.",
                 "Oggi l'azienda conta 14 addetti, divisi tra le diverse linee di prodotto.",
                 "Tymex nasce da questa esperienza, sviluppato in collaborazione con Web 81, per semplificare la raccolta delle ore nelle aziende che lavorano su commessa."]
        cta = ("Parliamo della tua azienda", "/#contatti", "Richiedi una demo")
    else:
        path, crumbs = "/en/about/", [("About us", "/en/about/")]
        title = "About us – Servizi Informatici Srl, Parma, Italy | Tymex"
        desc = "Tymex is developed by Servizi Informatici Srl of Parma, Italy, a Sistemi partner since 1990, together with Web 81, to make collecting hours simple."
        h1 = "Servizi Informatici Srl, in Parma since 1990."
        kw = "About us"
        paras = ["Servizi Informatici Srl was founded in 1990 and immediately became a certified Sistemi Spa dealer for the provinces of Parma, Piacenza and Reggio Emilia.",
                 "Thanks to its skills and certifications it earned the Sistemi Città qualification and the name Sistemi Parma.",
                 "Over the years it has built expertise above all for accounting firms (Profis line) and businesses (Spring SQL and eSOLVER lines).",
                 "We build websites for companies and professional firms and integrate our software via API with e-commerce, apps and cloud services.",
                 "Today the company has 14 employees across its product lines.",
                 "Tymex grew out of this experience, developed together with Web 81, to make collecting hours simple for businesses that work by the job."]
        cta = ("Let's talk about your business", "/en/#contact", "Book a demo")
    ps = "".join(f"<p>{esc(p)}</p>" for p in paras)
    body = f'''<section class="page-hero"><div class="wrap">{build.breadcrumbs_html(lang, crumbs)}
<h1><span class="kw intro" style="--d:0">{kw}</span><span class="intro" style="--d:1;display:block">{esc(h1)}</span></h1></div></section>
<section class="section" style="padding-top:24px"><div class="wrap split split--top">
<div class="prose reveal" style="margin:0">{ps}</div>
<div class="reveal">{I.ILLU_TIME.format(label="")}</div></div></section>
<section class="section" style="padding-top:0"><div class="wrap"><div class="cta-band reveal"><div><h2 class="h-lg">{esc(cta[0])}</h2></div><a class="btn btn--light" href="{cta[1]}">{esc(cta[2])}</a></div></div></section>'''
    page(path, lang, title, desc, body, alts={"it": "/chi-siamo/", "en": "/en/about/"}, crumbs=crumbs,
         ld=[{"@type": "AboutPage", "name": title, "about": {"@id": SITE + "/#org"}}])

def support(page, lang):
    import build
    if lang == "it":
        path, crumbs = "/supporto/", [("Supporto", "/supporto/")]
        title = "Supporto Tymex: manuale, video guide e storico versioni"
        desc = "Assistenza per gli utenti Tymex: manuale utente, video guide, storico delle versioni, condizioni generali e contatti del supporto."
        h1, kw = "Come possiamo aiutarti?", "Supporto"
        cards = [(I.DOC, "Manuale utente", "La guida completa per configurare e usare Tymex.", "[SEGNAPOSTO: link al manuale PDF]", None),
                 (I.PLAY.replace('fill="currentColor"', 'fill="currentColor" width="26" height="26"'), "Video guide", "Brevi video su come si usano app e web app.", "Apri il canale YouTube", CHANNEL),
                 (I.COPY, "Storico versioni", "Tutte le novità rilasciate, versione per versione.", "Vedi lo storico", "/storico-versioni/"),
                 (I.LOCK, "Sicurezza", "Come sono protetti i dati e come funziona l'infrastruttura.", "Leggi di più", "/sicurezza/"),
                 (I.DOC, "Condizioni generali", "Le condizioni generali di contratto del servizio.", "Leggi le condizioni", "/condizioni-generali/"),
                 (I.GLOBE, "Accedi a Tymex", "Entra nella web app con le tue credenziali.", "web.tymex.it", WEBAPP)]
        help_t, help_p = "Serve aiuto?", "Scrivici o chiamaci: ti rispondiamo al più presto."
    else:
        path, crumbs = "/en/support/", [("Support", "/en/support/")]
        title = "Tymex support: user guide, video guides and release notes"
        desc = "Help for Tymex users: user guide, video guides, release notes, terms and support contacts."
        h1, kw = "How can we help?", "Support"
        cards = [(I.DOC, "User guide", "The complete guide to setting up and using Tymex (in Italian).", "[PLACEHOLDER: link to user guide PDF]", None),
                 (I.PLAY.replace('fill="currentColor"', 'fill="currentColor" width="26" height="26"'), "Video guides", "Short videos on using the app and the web app (in Italian).", "Open the YouTube channel", CHANNEL),
                 (I.COPY, "Release notes", "Every new feature, version by version (in Italian).", "See release notes", "/storico-versioni/"),
                 (I.LOCK, "Security", "How data is protected and how the infrastructure works.", "Read more", "/en/security/"),
                 (I.DOC, "Terms and conditions", "The general terms of the service (in Italian).", "Read the terms", "/condizioni-generali/"),
                 (I.GLOBE, "Log in to Tymex", "Open the web app with your credentials.", "web.tymex.it", WEBAPP)]
        help_t, help_p = "Need help?", "Email or call us and we will get back to you as soon as possible."
    cs = ""
    for ic, h, p, link, href in cards:
        a = f'<a href="{href}" style="font-weight:700">{esc(link)} →</a>' if href else f'<span class="note">{esc(link)}</span>'
        cs += f'<div class="card reveal"><div class="tile-ico">{ic}</div><h3>{esc(h)}</h3><p>{esc(p)}</p><p class="mt-s">{a}</p></div>'
    body = f'''<section class="page-hero"><div class="wrap">{build.breadcrumbs_html(lang, crumbs)}
<h1><span class="kw intro" style="--d:0">{kw}</span><span class="intro" style="--d:1;display:block">{esc(h1)}</span></h1></div></section>
<section class="section" style="padding-top:24px"><div class="wrap grid grid--3">{cs}</div></section>
<section class="section" style="padding-top:0"><div class="wrap"><div class="cta-band reveal"><div><h2 class="h-lg">{esc(help_t)}</h2><p>{esc(help_p)}</p></div>
<div class="btn-row"><a class="btn btn--light" href="mailto:info@tymex.it">info@tymex.it</a><a class="btn btn--outline-light" href="tel:+390521252824">0521 252824</a></div></div></div></section>'''
    page(path, lang, title, desc, body, alts={"it": "/supporto/", "en": "/en/support/"}, crumbs=crumbs)

def thanks_and_404(page):
    for lang, path, t, h, p, back, href in [
        ("it", "/grazie/", "Grazie – richiesta inviata | Tymex", "Grazie, richiesta ricevuta.", "Ti ricontattiamo al più presto per fissare la demo. Nel frattempo puoi dare un'occhiata alle domande frequenti.", "Torna alla home", "/"),
        ("en", "/en/thank-you/", "Thank you – request sent | Tymex", "Thank you, we've got your request.", "We'll get back to you shortly to set up the demo. In the meantime, have a look at the FAQ.", "Back to home", "/en/")]:
        faq = "/faq-timesheet/" if lang == "it" else "/en/faq/"
        body = f'''<section class="center-page"><div class="wrap center"><h1 class="h-lg intro">{esc(h)}</h1><p class="lead mt-m intro" style="--d:1">{esc(p)}</p>
<div class="btn-row mt-l intro" style="--d:2;justify-content:center"><a class="btn btn--primary" href="{href}">{back}</a><a class="btn btn--ghost" href="{faq}">FAQ</a></div></div></section>'''
        page(path, lang, t, p, body, alts={"it": "/grazie/", "en": "/en/thank-you/"}, noindex=True)
    body = '''<section class="center-page"><div class="wrap center"><p class="eyebrow">Errore 404</p><h1 class="h-lg intro">Pagina non trovata.</h1>
<p class="lead mt-m intro" style="--d:1">La pagina che cerchi non esiste o è stata spostata. <span lang="en">This page doesn't exist or has moved.</span></p>
<div class="btn-row mt-l intro" style="--d:2;justify-content:center"><a class="btn btn--primary" href="/">Vai alla home</a><a class="btn btn--ghost" href="/en/" lang="en">English home</a><a class="btn btn--ghost" href="/blog/">Blog</a></div></div></section>'''
    page("/404.html", "it", "Pagina non trovata | Tymex", "La pagina richiesta non esiste.", body, noindex=True)

def build(page):
    for lang in ("it", "en"):
        home(page, lang)
        for k in SECTORS:
            sector_page(page, k, lang)
        about(page, lang)
        support(page, lang)
    thanks_and_404(page)
