"""Piano editoriale: articoli programmati (italiano).

Ogni articolo ha una data: il sito lo pubblica solo da quel giorno in poi (fuso orario Europe/Rome).
La pubblicazione automatica del martedì è in .github/workflows/pubblica-blog.yml.
"""

POSTS_IT_PIANO = [
 dict(slug="costo-orario-dipendente-come-calcolarlo",
      title="Quanto ti costa davvero un'ora di lavoro? Come calcolare il costo orario di un dipendente",
      seo="Costo orario dipendente: come calcolarlo, con esempio | Tymex",
      desc="Come si calcola il costo orario di un dipendente: retribuzione, contributi, costi indiretti e ore davvero lavorate, con un esempio numerico passo passo.",
      date="2026-11-10", img="/img/blog-costo-orario-dipendente.webp",
      alt="Illustrazione: una moneta con il simbolo dell'euro accanto a un orologio",
      body="""* Il costo orario non è lo stipendio diviso per le ore: contano contributi, ratei e costi indiretti.
* Va diviso per le ore effettivamente lavorate, non per quelle teoriche del contratto.
* È il dato di partenza di ogni preventivo e del calcolo della marginalità delle commesse.
## Perché il costo orario è il numero più importante
Ogni preventivo, ogni commessa, ogni calcolo di marginalità parte da una domanda: quanto costa all'azienda un'ora di lavoro di questa persona?
Se la risposta è sbagliata, è sbagliato tutto quello che viene dopo. Un costo orario sottostimato fa sembrare redditizie commesse che in realtà sono in perdita.
## Cosa entra nel costo di un dipendente
Lo stipendio lordo è solo la parte più visibile. Il costo aziendale annuo comprende di solito:
- la retribuzione lorda annua, comprese le mensilità aggiuntive previste dal contratto
- i contributi a carico dell'azienda
- l'accantonamento del TFR
- i costi indiretti attribuibili alla persona: formazione, attrezzature, auto aziendale, telefono, buoni pasto
Le percentuali di contributi e accantonamenti cambiano in base al contratto collettivo e all'inquadramento: il dato preciso te lo può dare il consulente del lavoro.
## Le ore che contano davvero
Il secondo errore tipico è dividere per le ore teoriche. Un contratto a 40 ore settimanali fa 2.080 ore l'anno sulla carta, ma da queste vanno tolte ferie, festività, permessi e una stima di malattia.
C'è poi un ulteriore passaggio: non tutte le ore lavorate sono ore produttive. Riunioni interne, spostamenti, formazione e attività amministrative sono necessarie, ma non si possono attribuire a una commessa.
## Un esempio passo passo
Facciamo un esempio con numeri ipotetici, solo per vedere il metodo.
Costo aziendale annuo:
- retribuzione lorda: 30.000 euro
- contributi e TFR (ipotesi dell'esempio): 11.000 euro
- costi indiretti: 3.000 euro
Totale: 44.000 euro.
Ore annue:
- ore teoriche: 40 ore × 52 settimane = 2.080 ore
- meno ferie, festività e permessi (ipotesi dell'esempio): 300 ore
Ore effettivamente lavorate: 1.780.
= Costo orario = 44.000 € ÷ 1.780 ore = 24,72 € l'ora
Se le ore produttive, cioè attribuibili alle commesse, sono il 75% del totale, le ore utili diventano 1.335. Il costo per ora produttiva sale a 32,96 euro.
È questo il numero da usare quando prepari un preventivo: le ore non produttive vanno comunque pagate, e qualcuno deve coprirle.
## Gli errori più comuni
- usare lo stipendio netto o solo la retribuzione lorda
- dividere per le ore teoriche del contratto
- dimenticare i costi indiretti
- usare lo stesso costo orario per tutti, indipendentemente dal ruolo
- non aggiornarlo dopo rinnovi contrattuali o aumenti
## Dal costo orario al costo della commessa
Una volta noto il costo orario di ogni persona, il costo del lavoro di una commessa si ottiene moltiplicando le ore registrate per il costo orario di chi le ha svolte. Per questo servono due ingredienti: costi orari corretti e ore registrate con precisione.
## Come aiuta Tymex
In Tymex il costo orario si imposta nel profilo di ogni operatore. Le ore registrate nei rapportini vengono valorizzate automaticamente, e il cruscotto mostra ore e costi per commessa, per cliente e per operatore. Così il costo reale di una commessa è sempre aggiornato, senza fogli di calcolo da tenere allineati.
## In sintesi
Il costo orario corretto si calcola sul costo aziendale completo, diviso per le ore davvero lavorate, meglio ancora per quelle produttive. Ricalcolalo almeno una volta l'anno: è la base di ogni preventivo affidabile."""),

 dict(slug="compilare-timesheet-abitudini",
      title="«Lo compilo venerdì»: perché il timesheet a memoria ti costa ore",
      seo="Come compilare il timesheet senza errori: 5 abitudini | Tymex",
      desc="Perché compilare il timesheet a fine settimana porta a dati sbagliati e cinque abitudini semplici per registrare le ore ogni giorno, in pochi secondi.",
      date="2026-11-17", img="/img/blog-compilare-timesheet.webp",
      alt="Illustrazione: un calendario settimanale con il venerdì evidenziato e un punto di domanda",
      body="""* Il timesheet compilato a memoria è impreciso: la memoria ricostruisce, non registra.
* Il problema non è la pigrizia, è la fatica: se registrare costa poco, lo si fa subito.
* Cinque abitudini bastano per avere dati affidabili senza perdere tempo.
## Venerdì, ore 17:40
Conosci la scena. È venerdì pomeriggio, la settimana è finita, e arriva il messaggio: «Ricordati di compilare il timesheet».
Apri il foglio. Lunedì… cosa hai fatto lunedì mattina? Martedì eri dal cliente, ma per quante ore? Mercoledì una chiamata lunga, poi quella riunione che doveva durare mezz'ora.
Alla fine scrivi numeri tondi. Otto ore qui, quattro e quattro là. Sembra tutto a posto. Non lo è.
## La memoria non è un archivio
La memoria non funziona come una registrazione da riavvolgere: ogni volta che ricordiamo, ricostruiamo. E nel ricostruire semplifichiamo, arrotondiamo, dimentichiamo le cose piccole.
Le cose piccole sono proprio quelle che sfuggono: i dieci minuti al telefono con il cliente, la modifica fatta al volo, la mezz'ora persa a cercare un documento. Prese una per una sembrano niente. Messe insieme, su una commessa, fanno la differenza tra guadagnare e andare in pari.
## Non è pigrizia, è fatica
Chi rimanda il timesheet non è svogliato. Sta facendo quello che fa chiunque davanti a un'attività noiosa e scomoda: la sposta in avanti.
La soluzione quindi non è insistere di più. È rendere la registrazione così facile da non avere motivo di rimandarla.
## 5 abitudini per un timesheet che funziona
### 1. Registra alla fine di ogni attività
Due minuti appena finito un intervento o un lavoro. Il ricordo è fresco, le ore sono esatte, e il pensiero è chiuso.
### 2. Usa il telefono, non aspettare il PC
Se per registrare devi essere alla scrivania, lo farai tardi. Con un'app sul telefono lo fai dove sei, anche dal cliente o in cantiere.
### 3. Duplica le attività ricorrenti
Molte giornate si somigliano. Copiare un'attività di ieri e cambiare solo la data è molto più veloce che riscriverla da zero.
### 4. Guarda il calendario prima di chiudere la giornata
Uno sguardo veloce per vedere se la giornata è completa. Se manca qualcosa, te ne accorgi subito e non il venerdì.
### 5. Scrivi una nota breve
Bastano tre parole: «sostituzione valvola», «revisione tavola 3». A distanza di settimane, quella nota ti dirà cosa hai fatto davvero.
## Cosa ci guadagni tu
Registrare ogni giorno non serve solo all'azienda. Ti toglie il pensiero del venerdì, ti dà dati concreti quando una commessa richiede più tempo del previsto e ti evita di dover ricostruire settimane intere quando qualcuno ti chiede «quanto ci hai messo?».
## Come aiuta Tymex
Tymex è pensato proprio per queste abitudini: i rapportini si inseriscono dallo smartphone in pochi tap, un'attività si duplica con il pulsante Copia e il calendario colora le giornate complete, quelle parziali e quelle con troppe ore. Così il controllo di fine giornata richiede un'occhiata.
## In sintesi
Il timesheet a memoria non è un problema di disciplina, ma di metodo. Registra subito, dal telefono, duplicando quello che si ripete e controllando il calendario prima di chiudere. Cinque abitudini, pochi secondi al giorno, e il venerdì torna a essere solo venerdì."""),

 dict(slug="rapportino-di-intervento-cosa-deve-contenere",
      title="Il rapportino di intervento perfetto: cosa deve contenere (e cosa no)",
      seo="Rapportino di intervento: cosa deve contenere | Tymex",
      desc="I sette campi indispensabili di un rapportino di intervento, gli errori più comuni e come passare dal cartaceo al digitale senza complicare il lavoro dei tecnici.",
      date="2026-11-24", img="/img/blog-rapportino-intervento.webp",
      alt="Illustrazione: una cartellina con un modulo e una lista di controllo spuntata",
      body="""* Un buon rapportino di intervento sta in sette campi: il resto è burocrazia.
* Deve essere veloce da compilare per il tecnico e chiaro da leggere per l'ufficio.
* Il digitale elimina ricopiature, fogli persi e grafie illeggibili.
## A cosa serve davvero un rapportino
Il rapportino di intervento è il documento che racconta cosa è stato fatto, per chi, quando e in quanto tempo. Serve all'ufficio per fatturare, al responsabile per controllare le commesse e al cliente per sapere cosa ha pagato.
Se è incompleto o confuso, qualcuno dovrà telefonare al tecnico per chiedere chiarimenti. E il tempo di quella telefonata non lo paga nessuno.
## I 7 campi indispensabili
### 1. Cliente
Il soggetto per cui è stato svolto l'intervento. È la prima informazione che serve all'amministrazione.
### 2. Commessa
L'intervento va sempre collegato a una commessa: è l'unico modo per sapere quanto costa e quanto rende.
### 3. Attività o servizio
Il tipo di lavoro svolto: manutenzione, installazione, assistenza, progettazione. Meglio scegliere da un elenco predefinito che scrivere a mano libera, così i dati si possono confrontare.
### 4. Data
Il giorno dell'intervento. Sembra ovvio, ma sui rapportini cartacei è uno dei campi più spesso dimenticati o sbagliati.
### 5. Ore lavorate
Il tempo effettivamente impiegato. Senza questo dato non c'è controllo dei costi.
### 6. Materiali e spese
Ricambi, materiali di consumo, trasferte, pedaggi. Se non vengono registrati subito, spesso non vengono più addebitati.
### 7. Note
Poche righe su cosa è stato fatto e su eventuali problemi rilevati. Brevi, ma precise.
## Cosa non serve
Un rapportino con troppi campi viene compilato male. Evita di chiedere informazioni che l'ufficio ha già, come indirizzo e dati fiscali del cliente, o campi facoltativi che nessuno legge. Ogni campo in più è un motivo per rimandare la compilazione.
## Gli errori più comuni
- rapportini compilati giorni dopo l'intervento
- ore arrotondate a mezza giornata o giornata intera
- descrizioni generiche come «intervento tecnico»
- materiali e spese dimenticati
- fogli cartacei persi, bagnati o illeggibili
- lo stesso intervento registrato due volte
## Dal cartaceo al digitale
Il passaggio al digitale risolve gran parte di questi problemi: niente fogli da ricopiare in ufficio, campi obbligatori che non si possono saltare, elenchi a scelta al posto della scrittura libera e dati disponibili subito per chi deve fatturare o controllare le commesse.
L'importante è che lo strumento sia più veloce del foglio di carta. Se il tecnico impiega più tempo con l'app che con la penna, tornerà alla penna.
## Come aiuta Tymex
Con Tymex il tecnico compila il rapportino dallo smartphone, anche presso il cliente: commessa, servizio, ore e data sono obbligatori, mentre cliente, note e spese aggiuntive si aggiungono quando servono. Gli elenchi di clienti, commesse e servizi sono già pronti, e il rapportino arriva subito in ufficio, esportabile in CSV.
## In sintesi
Il rapportino perfetto è quello che il tecnico compila volentieri e che l'ufficio non deve correggere. Sette campi chiari, compilati subito, preferibilmente dal telefono: tutto il resto è burocrazia."""),

 dict(slug="stima-tempi-commessa-perche-sbagliamo",
      title="Il preventivo ottimista: perché sottostimiamo sempre i tempi (e come smettere)",
      seo="Stima dei tempi di una commessa: perché sbagliamo | Tymex",
      desc="Perché le stime dei tempi di una commessa sono quasi sempre ottimiste, cos'è la fallacia della pianificazione e come i dati consuntivi rendono i preventivi più realistici.",
      date="2026-12-01", img="/img/blog-stima-tempi-commessa.webp",
      alt="Illustrazione: una clessidra accanto a un grafico con una barra che supera la linea prevista",
      body="""* Sottostimare i tempi è normale: la psicologia lo chiama fallacia della pianificazione.
* Non si corregge con più impegno, ma guardando come sono andate le commesse simili.
* I dati consuntivi sono l'antidoto migliore al preventivo ottimista.
## «Ci vorranno tre giorni»
Quante volte l'hai detto? Quante volte sono stati davvero tre giorni?
Se sei come quasi tutti, la risposta è: raramente. Non perché tu sia disorganizzato. Perché il cervello umano, quando immagina il futuro, è un ottimista incorreggibile.
## Il tempo che ci sfugge
Seneca lo scriveva già duemila anni fa.
> Non è che abbiamo poco tempo: è che ne abbiamo perso molto.
~ Seneca, De brevitate vitae, 1, 3
Parlava della vita, non dei preventivi. Ma il meccanismo è lo stesso: il tempo non manca, sfugge. Si disperde in mille piccole cose che, al momento di fare i conti, non avevamo messo in conto.
## La fallacia della pianificazione
Alla fine degli anni Settanta gli psicologi Daniel Kahneman e Amos Tversky hanno dato un nome a questo fenomeno: fallacia della pianificazione. È la tendenza a sottostimare il tempo necessario per completare un'attività, anche quando sappiamo che in passato attività simili hanno richiesto di più.
Il motivo è semplice. Quando stimiamo, immaginiamo lo scenario in cui tutto va come deve: nessun imprevisto, nessuna attesa, nessuna modifica del cliente. Pensiamo al lavoro, non a tutto quello che gli sta intorno.
C'è perfino una legge semiseria, quella di Hofstadter: ci vuole sempre più tempo di quanto pensi, anche tenendo conto della legge di Hofstadter.
## Cosa dimentichiamo quando stimiamo
- le richieste di modifica del cliente
- le attese: materiali, approvazioni, risposte
- le riunioni e le telefonate di coordinamento
- gli spostamenti
- le revisioni e le correzioni
- il tempo per chiudere davvero il lavoro: verifiche, documenti, consegna
## Più impegno non basta
Sapere di essere ottimisti non basta a smettere di esserlo. La soluzione più efficace è cambiare punto di vista: invece di chiederti «quanto ci vorrà questa volta?», chiediti «quanto ci sono volute, davvero, le ultime commesse simili?».
È il principio della stima basata sui casi precedenti: si parte da quello che è successo, non da quello che speriamo succeda.
## Tre abitudini per stime più realistiche
### 1. Registra sempre le ore reali
Senza dati consuntivi non c'è niente da confrontare. Ogni commessa conclusa diventa un riferimento per la prossima.
### 2. Confronta stima e realtà a fine commessa
Cinque minuti per guardare quanto avevi previsto e quanto è servito. Non per cercare colpe, ma per imparare.
### 3. Aggiungi un margine esplicito
Se le commesse simili sforano in modo sistematico, inseriscilo nel preventivo come voce dichiarata, non come speranza nascosta.
## Come aiuta Tymex
Tymex registra le ore effettive su ogni commessa, per servizio e per operatore. A fine lavoro hai il consuntivo pronto da confrontare con il preventivo, e lo storico delle commesse passate diventa la base per stimare meglio quelle future.
## In sintesi
Sottostimare i tempi non è un difetto personale: è il modo in cui funziona il nostro cervello. Non si combatte con l'ottimismo al contrario, ma con i dati. Registra le ore reali, confrontale con le stime e lascia che sia il passato a guidare i tuoi prossimi preventivi."""),

 dict(slug="preventivo-consuntivo-scostamenti-commessa",
      title="Preventivo e consuntivo: come leggere gli scostamenti di una commessa",
      seo="Preventivo e consuntivo: come leggere gli scostamenti | Tymex",
      desc="Come confrontare ore preventivate e consuntivate di una commessa, calcolare lo scostamento in percentuale e capirne le cause per migliorare i preventivi futuri.",
      date="2026-12-08", img="/img/blog-preventivo-consuntivo.webp",
      alt="Illustrazione: due barre a confronto, ore previste e ore reali, con una freccia",
      body="""* Lo scostamento misura la differenza tra ore previste e ore realmente lavorate.
* Un +10% e un +50% non sono la stessa cosa: cambiano le cause e le azioni.
* Leggere gli scostamenti in corso d'opera permette di intervenire prima che sia tardi.
## Preventivo e consuntivo, in due righe
Il preventivo è quello che pensi di spendere prima di iniziare una commessa: ore, costi, materiali. Il consuntivo è quello che hai speso davvero, a lavoro finito o in corso.
La differenza tra i due si chiama scostamento. Ed è uno dei dati più utili che un'azienda che lavora su commessa possa avere.
## Come si calcola lo scostamento
La formula è semplice:
= Scostamento % = (ore consuntivate − ore preventivate) ÷ ore preventivate × 100
Un esempio:
- ore preventivate: 100
- ore consuntivate: 110
Lo scostamento è del +10%. Se le ore consuntivate fossero 150, lo scostamento sarebbe del +50%.
Lo stesso calcolo si può fare sui costi, moltiplicando le ore per il costo orario di chi le ha svolte.
## +10% o +50%: perché non è la stessa cosa
Uno scostamento piccolo può dipendere da imprevisti normali: un'attesa, un problema tecnico, una riunione in più. Uno scostamento grande di solito segnala qualcosa di più profondo: una stima sbagliata in partenza, un cambiamento del lavoro richiesto o un problema organizzativo.
Molte aziende si danno delle soglie di attenzione, ad esempio sotto il 10% nessuna azione, oltre il 25% un'analisi delle cause. Le soglie giuste dipendono dal tuo settore e dalle tue commesse: l'importante è deciderle prima.
## Le cause più frequenti
- stima iniziale troppo ottimista
- richieste del cliente fuori dal perimetro concordato
- attese per materiali, approvazioni o informazioni
- inefficienze organizzative o passaggi di consegne
- errori di registrazione delle ore
Le richieste extra meritano un'attenzione particolare: se non vengono riconosciute come tali, finiscono per erodere il margine senza che nessuno se ne accorga.
## Le domande da farsi
Davanti a uno scostamento importante, conviene chiedersi:
- dove si è concentrato, su quale attività o fase?
- era prevedibile al momento del preventivo?
- dipende da noi o da richieste del cliente?
- si è già verificato su commesse simili?
- cosa cambieremo nel prossimo preventivo?
## In corso d'opera, non solo alla fine
Il vero valore degli scostamenti sta nel leggerli mentre la commessa è ancora aperta. Se a metà lavoro le ore consumate sono già l'80% di quelle previste, c'è ancora tempo per parlare con il cliente, rivedere le priorità o riorganizzare il lavoro.
A commessa chiusa, invece, si può solo prenderne atto e imparare per la volta successiva.
## Come aiuta Tymex
Tymex raccoglie le ore consuntivate per commessa, per servizio e per operatore, e il cruscotto web mostra in ogni momento quante ore e quanti costi ha assorbito ciascuna commessa. Confrontando questi dati con il preventivo vedi lo scostamento quando sei ancora in tempo per intervenire. Per l'impatto sul margine, leggi anche la guida su come calcolare la marginalità di una commessa.
## In sintesi
Lo scostamento tra preventivo e consuntivo non è una colpa da nascondere, è un'informazione da usare. Calcolalo, leggilo in corso d'opera, cercane le cause e porta quello che impari nel preventivo successivo."""),
]
