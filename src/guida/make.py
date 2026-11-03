"""Genera guida.html (A4) nello stile del sito tymex.it."""
from html import escape as e

CSS = """
@font-face{font-family:"Montserrat";font-weight:100 900;src:url("montserrat-latin-wght-normal.woff2") format("woff2");unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}
@font-face{font-family:"Montserrat";font-weight:100 900;src:url("montserrat-latin-ext-wght-normal.woff2") format("woff2");unicode-range:U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+1E00-1EFF}
@page{size:A4;margin:0}
:root{--primary:#4654A3;--ink:#270949;--ink2:#1C0E36;--peri:#6B7ACC;--lilac:#BDBBF1;--tint:#F4F4FD;--line:#ECEBFA;--line2:#D5D3F2;--muted:#4A3E66;--muted2:#5A4D78;--on-dark:#D9D6F5;--coral:#F95B3D;--green:#2E9E5B;--orange:#E8902A;--red:#D64545}
*{box-sizing:border-box}
html,body{margin:0;padding:0}
body{font-family:"Montserrat",sans-serif;color:var(--ink);-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{width:210mm;height:297mm;position:relative;overflow:hidden;page-break-after:always;background:#fff;padding:16mm 16mm 0}
.page:last-child{page-break-after:auto}
.top{display:flex;align-items:center;justify-content:space-between;margin-bottom:12mm}
.top img{height:9mm}
.top .tag{font-size:8.5pt;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--muted2)}
.eyebrow{font-size:9pt;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--primary);margin:0 0 4mm}
h1{font-size:32pt;font-weight:900;letter-spacing:-.02em;line-height:1.05;margin:0;max-width:160mm}
.lead{font-size:12.5pt;line-height:1.6;color:var(--muted);margin:5mm 0 0;max-width:165mm}
.body{margin-top:13mm}
.frame{background:#fff;border-radius:6mm;padding:3mm;box-shadow:0 10mm 22mm -14mm rgba(39,9,73,.55);border:1px solid var(--line)}
.frame img{display:block;width:100%;border-radius:3.5mm}
.phone{background:var(--ink2);padding:2.6mm;border-radius:10mm;box-shadow:0 12mm 24mm -14mm rgba(39,9,73,.6)}
.phone img{display:block;width:100%;border-radius:7.5mm}
.grid{display:grid;gap:7mm}
.g2{grid-template-columns:1fr 1fr}
.card{border:1.5px solid var(--line);border-radius:6mm;padding:8.5mm 8mm;background:#fff}
.card.tint{background:var(--tint);border-color:var(--tint)}
.chip{display:inline-block;font-size:8pt;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:#fff;background:var(--primary);border-radius:99px;padding:1.3mm 3mm;margin-bottom:3.5mm}
.chip.peri{background:var(--peri)}.chip.ink{background:var(--ink)}.chip.lilac{background:var(--lilac);color:var(--ink)}
.chip.green{background:var(--green)}.chip.orange{background:var(--orange)}.chip.red{background:var(--red)}
.card h3{font-size:15pt;font-weight:800;margin:0 0 2.5mm;line-height:1.2}
.card p{font-size:11.5pt;line-height:1.6;color:var(--muted);margin:0}
.callout{margin-top:9mm;background:var(--tint);border-radius:6mm;padding:7mm 8mm 7mm 15mm;position:relative;font-size:11.5pt;line-height:1.55;color:var(--ink)}
.callout::before{content:"";position:absolute;left:7mm;top:7mm;bottom:7mm;width:2mm;border-radius:2mm;background:var(--primary)}
.callout b{font-weight:800}
.foot{position:absolute;left:16mm;right:16mm;bottom:10mm;display:flex;justify-content:space-between;align-items:center;font-size:8pt;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--muted2);border-top:1px solid var(--line);padding-top:4mm}
.foot .n{color:var(--primary);font-weight:900;font-size:10pt}
.deco{position:absolute;pointer-events:none}
.compact .card{padding:6mm 7mm}.compact .grid{gap:5mm}
b,strong{font-weight:800}
/* passi */
.steps{display:grid;gap:5.5mm}
.step{display:flex;gap:8mm;align-items:center;border:1.5px solid var(--line);border-radius:6mm;padding:6mm 8mm}
.step .num{flex:none;width:18mm;height:18mm;border-radius:5mm;background:var(--primary);color:#fff;font-weight:900;font-size:18pt;display:flex;align-items:center;justify-content:center}
.step h3{font-size:15.5pt;font-weight:800;margin:0 0 1.2mm}
.step p{font-size:11.5pt;color:var(--muted);margin:0;line-height:1.5}
/* checklist */
.check{display:grid;gap:4mm}
.check div{display:flex;gap:6mm;align-items:center;border:1.5px solid var(--line);border-radius:5mm;padding:5mm 7mm;font-size:12pt;font-weight:600}
.check span{flex:none;width:8mm;height:8mm;border-radius:2mm;border:2px solid var(--primary)}
/* copertina e retro */
.cover{background:linear-gradient(180deg,var(--tint) 0%,#fff 70%);padding:18mm}
.cover h1{font-size:40pt;line-height:1.02;max-width:150mm}
.cover h1 em{font-style:normal;color:var(--primary)}
.back{background:var(--ink);color:#fff;padding:22mm 18mm}
.back h1{color:#fff;font-size:40pt}
.back .lead{color:var(--on-dark)}
"""

DECO = '''<svg class="deco" style="{style}" viewBox="0 0 600 600" aria-hidden="true"><rect x="40" y="40" width="520" height="520" rx="150" fill="{bg}"/>
<rect x="150" y="230" width="70" height="210" rx="35" fill="{fg}"/><rect x="265" y="160" width="70" height="280" rx="35" fill="{fg}"/><rect x="380" y="300" width="70" height="140" rx="35" fill="{fg}"/></svg>'''

pages = []
TOTAL = 17

def page(n, eyebrow, title, lead, body):
    pages.append(f'''<section class="page">
<div class="top"><img src="tymex-logo.png" alt="Tymex"><span class="tag">Guida operativa</span></div>
<p class="eyebrow">{e(eyebrow)}</p><h1>{e(title)}</h1><p class="lead">{e(lead)}</p>
<div class="body">{body}</div>
<div class="foot"><span>Tymex · Guida ai primi passi</span><span>Uso operativo &nbsp; <span class="n">{n:02d}</span></span></div>
</section>''')

def card(chip, title, text, color="", tint=False):
    return f'<div class="card{" tint" if tint else ""}"><span class="chip {color}">{e(chip)}</span><h3>{e(title)}</h3><p>{text}</p></div>'

def callout(html):
    return f'<div class="callout">{html}</div>'

def frame(src, style=""):
    return f'<div class="frame" style="{style}"><img src="{src}" alt=""></div>'

# 1 — copertina
pages.append(f'''<section class="page cover">
{DECO.format(style="right:-60mm;top:-40mm;width:170mm;opacity:.7", bg="#E3E4F7", fg="#fff")}
<div style="position:relative">
<img src="tymex-logo.png" alt="Tymex" style="height:13mm">
<p class="eyebrow" style="margin-top:22mm">Guida ai primi passi · Web + app mobile</p>
<h1>Tutto quello che serve <em>per iniziare.</em></h1>
<p class="lead">Accesso, configurazione iniziale, commesse, operatori e registrazione dei rapportini.</p>
</div>
<div style="position:absolute;left:18mm;right:18mm;top:120mm;height:140mm">
  <div class="frame" style="position:absolute;left:0;top:22mm;width:128mm"><img src="p15_0.png" alt=""></div>
  <div class="phone" style="position:absolute;right:38mm;top:0;width:54mm;transform:rotate(-4deg)"><img src="p12_0.png" alt=""></div>
  <div class="phone" style="position:absolute;right:0;top:16mm;width:54mm;transform:rotate(4deg)"><img src="p13_0.png" alt=""></div>
</div>
<div class="foot" style="left:18mm;right:18mm"><span>Servizi Informatici S.r.l.</span><span>www.tymex.it</span></div>
</section>''')

# 2 — percorso
steps = [("Accedi come amministratore", "Entra su web.tymex.it con le credenziali ricevute."),
         ("Configura servizi e operatori", "Definisci le attività e assegna ruoli, costi e ore."),
         ("Inserisci clienti e commesse", "I clienti sono facoltativi; le commesse servono per i rapportini."),
         ("Distribuisci l’app", "Consegna a ciascun operatore le proprie credenziali."),
         ("Registra e controlla le ore", "Calendario, rapportini, filtri ed esportazioni.")]
page(2, "01 / Orientamento", "Il percorso di avvio",
     "Una guida pratica: dalla prima configurazione alla registrazione e all’esportazione delle ore.",
     '<div class="steps">' + "".join(f'<div class="step"><div class="num">{i+1:02d}</div><div><h3>{e(h)}</h3><p>{e(p)}</p></div></div>' for i, (h, p) in enumerate(steps)) + "</div>")

# 3 — login
page(3, "02 / Accesso", "Login e profili", "Accedi al portale con le credenziali comunicate dal supporto.",
     f'''<div class="grid" style="grid-template-columns:80mm 1fr;align-items:start">{frame("p03_0.png")}
<div class="grid">{card("Amministratore", "Portale web", "URL: <b>web.tymex.it</b><br>Email e password: fornite dal supporto. Al primo accesso cambia la password dal menu Profilo Utente.")}
{card("Operatori", "App e portale web", "Anche gli operatori ricevono credenziali individuali. Il profilo <b>ASSIST</b> registra rapportini personali; per inserirli per altri serve <b>MANAGER</b>.", "peri")}</div></div>
{callout("<b>Tre ruoli:</b> ASSIST (rapportini personali); MANAGER (gestione e validazione del team); ADMIN (utenti, servizi, commesse, export).")}''')

# 4 — servizi
page(4, "03 / Configurazione", "Servizi: crea le attività", "Definisci le tipologie di lavoro selezionabili nei rapportini.",
     f'''<div class="grid g2">{card("Campo 01", "Codice servizio", "Inserisci un identificativo riconoscibile, per esempio <b>001</b>, <b>002</b> o <b>MAN</b>.")}
{card("Campo 02", "Descrizione", "Scrivi un nome chiaro e completo dell’attività, visibile anche agli operatori nell’app.")}
{card("Impostazione", "Attivo", "<b>Da selezionare.</b> Consente di scegliere il servizio nel nuovo rapportino.", "green", True)}
{card("Impostazione", "Attiva di default", "<b>Non selezionare</b> in questa configurazione iniziale.", "orange", True)}</div>
{callout("<b>Prima di proseguire:</b> verifica che ogni servizio che vuoi utilizzare sia attivo e sia riconoscibile dagli operatori.")}''')

# 5 — operatori elenco
page(5, "04 / Configurazione", "Operatori: elenco e creazione", "Dal menu laterale apri Operatori e seleziona AGGIUNGI OPERATORE.",
     f'''{frame("p05_0.png")}<div class="grid" style="grid-template-columns:1fr 88mm;margin-top:8mm;align-items:start">
{callout("Compila <b>Nome</b>, <b>Cognome</b> ed <b>Email</b>. L’indirizzo email diventa la credenziale di accesso all’app.").replace('class="callout"','class="callout" style="margin-top:0"')}
{frame("p05_1.png")}</div>''')

# 6 — profilo operatore
page(6, "05 / Configurazione", "Completa il profilo operatore", "Questi campi influenzano visibilità dei servizi, calendario e calcolo dei costi.",
     f'''<div class="grid g2">{card("Obbligatorio", "Ruolo", "Assegna <b>ASSIST</b>, <b>MANAGER</b> oppure <b>ADMIN</b> in base alle responsabilità.")}
{card("Costi", "Costo orario", "Indica il costo orario in euro. È utilizzato per calcolare il costo delle commesse e la marginalità.", "peri")}
{card("Permessi", "Servizi abilitati", "Seleziona i servizi che l’operatore può registrare nei rapportini.", "ink")}
{card("Calendario", "Ore settimanali", "Definisci le ore previste per ciascun giorno da lunedì a domenica. Servono a colorare gli indicatori giornalieri.", "lilac")}</div>''')

# 7 — clienti
page(7, "06 / Anagrafiche", "Clienti: utili, ma facoltativi", "Associare un cliente a una commessa migliora la consultazione e l’esportazione.",
     f'''{frame("p07_0.png")}<div class="grid g2" style="margin-top:7mm">{card("Navigazione", "Aggiungi cliente", "Apri <b>Clienti</b> e premi <b>AGGIUNGI CLIENTE</b>. La <b>Ragione Sociale</b> è l’unico campo obbligatorio.")}
{card("Vantaggi", "Filtri e CSV", "Selezionando il cliente si visualizzano soltanto le sue commesse. La ragione sociale può comparire negli export CSV.", "green")}</div>
{callout("Gli altri dati sono facoltativi: codice del gestionale, indirizzo, recapiti e dati fiscali. Possono facilitare la riconciliazione.")}''')

# 8 — scheda cliente
page(8, "07 / Anagrafiche", "Scheda cliente", "La scheda raccoglie i riferimenti aziendali e gli eventuali codici del gestionale.",
     f'''<div class="grid" style="grid-template-columns:96mm 1fr;align-items:start">{frame("p08_0.png")}
{card("Da ricordare", "Ragione Sociale obbligatoria", "Tutti gli altri campi possono essere completati successivamente: inserisci subito le informazioni indispensabili.", "", True)}</div>''')

# 9 — commesse
page(9, "08 / Commesse", "Crea le commesse di lavoro", "Ogni intervento o attività su cui registrare ore deve essere associato a una commessa.",
     f'''{frame("p09_0.png")}<div class="grid" style="grid-template-columns:1fr 1fr;margin-top:6mm;align-items:start">{frame("p09_1.png")}
{callout("Dal menu <b>Commesse</b> scegli <b>AGGIUNGI COMMESSA</b>. Nel modulo inserisci codice, descrizione e gli altri parametri operativi.").replace('class="callout"','class="callout" style="margin-top:0"')}</div>''')

# 10 — impostazioni commessa
page(10, "09 / Commesse", "Impostazioni fondamentali", "Una commessa deve essere selezionabile nell’app per poter ricevere rapportini.",
     f'''<div class="grid g2">{card("Identificazione", "Codice e descrizione", "Usa codici e nomi riconoscibili, per esempio <b>CAL-001 · Manutenzione caldaia</b>.")}
{card("Relazioni", "Cliente e servizi", "Associa un cliente se disponibile e abilita le tipologie di servizio pertinenti.", "peri")}
{card("Disponibilità", "Data apertura e stato", "Imposta la data di apertura e seleziona <b>ATTIVA</b> per rendere la commessa disponibile.", "green")}
{card("Scadenza", "Data chiusura", "Campo facoltativo. Dopo la data di chiusura la commessa non sarà più disponibile per nuove registrazioni.", "orange")}</div>''')

# 11 — distribuzione
page(11, "10 / Distribuzione", "Attiva il lavoro sul campo", "Dopo la configurazione, ogni operatore può accedere dal proprio dispositivo.",
     f'''<div class="card" style="background:var(--ink);border-color:var(--ink);color:#fff;padding:9mm;position:relative;overflow:hidden">
{DECO.format(style="right:-18mm;top:-22mm;width:70mm;opacity:.35", bg="#4654A3", fg="#270949")}
<span class="chip lilac">Accesso web</span><h3 style="font-size:24pt;font-weight:900;color:#fff;margin:2mm 0">web.tymex.it</h3><p style="color:var(--on-dark)">Disponibile anche da PC, senza installazione.</p></div>
<div class="grid g2" style="margin-top:5mm">{card("Dispositivi", "iOS", "L’operatore utilizza l’app sul proprio dispositivo ed effettua il login con credenziali personali.", "peri")}
{card("Dispositivi", "Android", "L’operatore utilizza l’app sul proprio dispositivo ed effettua il login con credenziali personali.", "peri")}</div>
{callout("Condividi individualmente le credenziali e indica ai collaboratori quali servizi e commesse devono utilizzare.")}''')

# 12 — calendario
page(12, "11 / Rapportini", "Leggere il calendario", "Il calendario mensile permette di capire subito se le ore previste sono state registrate.",
     f'''<div class="grid" style="grid-template-columns:70mm 1fr;gap:9mm;align-items:start"><div class="phone"><img src="p12_0.png" alt=""></div>
<div class="grid">{card("Indicatore", "Verde · completato", "Ore registrate uguali a quelle previste.", "green")}
{card("Indicatore", "Arancione · parziale", "Ore registrate inferiori al totale previsto.", "orange")}
{card("Indicatore", "Rosso · eccesso", "Ore registrate superiori al totale previsto: controlla i rapportini.", "red")}</div></div>
{callout("Tocca una giornata del calendario per visualizzare l’elenco dei rapportini già registrati.")}''')

# 13 — nuovo rapportino
page(13, "12 / Rapportini", "Inserire un nuovo rapportino", "Seleziona il giorno sul calendario e premi il pulsante +.",
     f'''<div class="grid compact" style="grid-template-columns:62mm 1fr;gap:9mm;align-items:start"><div class="phone"><img src="p13_0.png" alt=""></div>
<div class="grid">{card("Obbligatori", "Campi necessari", "<b>Commessa</b>, <b>Servizio</b>, <b>Ore lavorate</b> e <b>Data</b> devono essere indicati.")}
{card("Facoltativi", "Dettagli aggiuntivi", "Puoi compilare <b>Cliente</b>, <b>Note</b> e <b>Spese aggiuntive</b>, se pertinenti.", "lilac")}
{card("Comando", "Salva", "Conferma il rapportino dopo aver controllato i dati.", "ink")}</div></div>
{callout("<b>Scorciatoia:</b> il pulsante <b>Copia</b> duplica i campi di un rapportino esistente, esclusa la data, da impostare manualmente.")}''')

# 14 — correggere
ops = [("Operazione 01", "Apri un rapportino", "Dal calendario scegli il giorno e apri il rapportino nell’elenco.", ""),
       ("Operazione 02", "Matita · modifica", "Aggiorna i campi necessari, tra cui commessa, servizio, ore e note.", "peri"),
       ("Operazione 03", "Cestino · elimina", "Elimina il rapportino selezionato. <b>Questa operazione è definitiva e non reversibile.</b>", "red")]
page(14, "13 / Gestione", "Correggere e verificare le ore", "Le registrazioni possono essere consultate, modificate ed eventualmente eliminate.",
     '<div class="grid">' + "".join(card(a, b, c, d) for a, b, c, d in ops) + "</div>")

# 15 — esporta
page(15, "14 / Gestione web", "Consulta ed esporta", "Dal portale web è disponibile l’elenco dei rapportini con filtri e download dei dati.",
     f'''{frame("p15_0.png")}<div class="grid g2" style="margin-top:7mm">{card("Ricerca", "Filtri disponibili", "Imposta le date <b>Dal / Al</b> e filtra per <b>Commessa, Cliente, Servizio, Operatore</b>.")}
{card("Download", "Esporta su CSV", "Il pulsante <b>Esporta su CSV</b> scarica i rapportini filtrati per Excel o ulteriori elaborazioni.", "green")}</div>''')

# 16 — checklist
items = ["Accesso Admin verificato e password aggiornata", "Servizi creati e impostati come attivi",
         "Operatori configurati con ruoli e costo orario", "Ore settimanali e servizi assegnati agli operatori",
         "Clienti caricati, se utili alla gestione", "Commesse attive e servizi correttamente associati",
         "Credenziali distribuite agli operatori", "Primo rapportino inserito e verificato"]
page(16, "15 / Riepilogo", "Checklist prima della consegna", "Controlla queste attività prima di avviare l’operatività quotidiana.",
     '<div class="check">' + "".join(f"<div><span></span>{e(i)}</div>" for i in items) + "</div>")

# 17 — retro
pages.append(f'''<section class="page back">
{DECO.format(style="right:-70mm;bottom:-60mm;width:200mm;opacity:.55", bg="#4654A3", fg="#270949")}
<div style="position:relative">
<div style="display:flex;align-items:center;gap:5mm"><img src="p17_0.png" alt="" style="width:16mm;border-radius:4mm"><span style="font-size:22pt;font-weight:900;letter-spacing:.02em">TYMEX</span></div>
<h1 style="margin-top:40mm">Pronti a iniziare.</h1>
<p class="lead">Una guida operativa per amministratori, manager e operatori: dalla configurazione iniziale fino alla consultazione dei rapportini.</p>
<div style="margin-top:48mm;background:#fff;color:var(--ink);border-radius:7mm;padding:9mm;width:110mm">
<span class="chip">Hai bisogno di assistenza?</span>
<p style="font-size:20pt;font-weight:900;margin:2mm 0 2mm">info@tymex.it</p>
<p style="font-size:13pt;font-weight:700;margin:0 0 2mm">0521 252824</p>
<p style="font-size:11pt;color:var(--muted);margin:0">www.tymex.it</p></div>
</div>
<div class="foot" style="left:18mm;right:18mm;color:var(--on-dark);border-color:rgba(255,255,255,.15)"><span>Servizi Informatici S.r.l. · Via Sicuri 42/a, Parma</span><span></span></div>
</section>''')

assert len(pages) == TOTAL, len(pages)
open("guida.html", "w", encoding="utf-8").write(
    f'<!doctype html><html lang="it"><head><meta charset="utf-8"><title>Tymex – Guida ai primi passi</title><style>{CSS}</style></head><body>{"".join(pages)}</body></html>')
print("ok", len(pages))
