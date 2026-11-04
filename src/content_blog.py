"""Nuovi articoli del blog (italiano), nello stesso formato di content_en_blog.py.

Per aggiungere un articolo: copia un blocco, cambia i campi e il testo, metti la copertina in public/img/,
aggiungi la versione inglese in content_en_blog.py (stesso it_slug) e lancia python3 src/build.py.
Formato del testo: "## " titolo, "### " sottotitolo, "- " elenco, "| a | b |" tabella, "= " formula,
"* " riquadro In breve, "> " citazione, "~ " autore della citazione (subito dopo).
"""

POSTS_IT_NEW = [
 dict(slug="rilevazione-ore-risvolti-psicologici-dipendenti",
      title="Rilevazione ore: cosa pensano davvero i tuoi dipendenti (e quali parole usare)",
      seo="Rilevazione ore e dipendenti: cosa pensano davvero | Tymex",
      desc="Perché la rilevazione delle ore spaventa i dipendenti, cosa succede nella loro testa e quali parole usare per presentarla, così diventa uno strumento utile a tutti.",
      date="2026-11-03", img="/img/blog-rilevazione-ore-psicologia.webp",
      alt="Illustrazione: due persone del team con un fumetto, un orologio e un segno di spunta, nei colori di Tymex",
      body="""* La rilevazione ore spaventa quando viene percepita come un controllo, non come uno strumento.
* Le parole con cui la presenti contano quanto il software che scegli.
* Funziona se è veloce, se ha uno scopo chiaro e se restituisce qualcosa a chi la compila.
## Facciamo un esperimento
Immagina di entrare in riunione e dire al tuo team: «Da lunedì registriamo le ore». Fermati un secondo. Cosa sta succedendo nella testa delle persone sedute davanti a te?
Ti do un indizio: non stanno pensando alla marginalità delle commesse. Stanno pensando «Non si fidano di me». Oppure «Adesso mi contano anche i minuti della pausa caffè».
Non è cattiveria. È il cervello che fa il suo lavoro: davanti a una novità ambigua, si prepara al peggio.
## Non sono i fatti, sono i giudizi
Quasi duemila anni fa Epitteto l'aveva già capito benissimo.
> Non sono i fatti in sé a turbare gli uomini, ma i giudizi che gli uomini formulano sui fatti.
~ Epitteto, Manuale, 5
La rilevazione ore, di per sé, è neutra. È un elenco di attività e di numeri. Quello che la rende accettabile o insopportabile è il giudizio che le persone ci costruiscono sopra. E quel giudizio dipende, in buona parte, da come gliela racconti.
## Le paure che nessuno dice ad alta voce
Accanto al grande timore del controllo ce ne sono di più piccoli, che in riunione non arrivano quasi mai:
- essere giudicati sulla quantità di ore e non sulla qualità del lavoro
- dover giustificare pause, imprevisti, attività che non stanno in nessuna casella
- essere confrontati con i colleghi
- perdere tempo in burocrazia invece che nel lavoro vero
- non sapere chi vedrà i dati e che cosa ne farà
Sono paure ragionevoli. Se le ignori non spariscono: si trasformano in timesheet compilati il venerdì sera, a memoria.
## Cambia le parole, cambia la percezione
Ecco il punto. Le parole che usi creano la cornice dentro cui le persone leggono tutto il resto.
Confronta queste due frasi:
- «Da lunedì controlliamo le ore di tutti.»
- «Da lunedì iniziamo a capire quanto ci costano davvero le commesse, così smettiamo di lavorare in perdita senza accorgercene.»
Stesso strumento. Effetto opposto. Nella prima c'è un controllore e un controllato. Nella seconda c'è una squadra con un obiettivo comune.
Qualche sostituzione che funziona:
- non «controllo», ma «visibilità»
- non «verifica delle ore», ma «costo reale delle commesse»
- non «chi ha lavorato meno», ma «quale commessa abbiamo sottostimato»
## Il perché prima del come
Le persone accettano una regola quando ne capiscono lo scopo. Prima di parlare di app e schermate, rispondi a tre domande:
- a cosa servono i dati? A preventivare meglio, distribuire il carico di lavoro, difendere i margini
- cosa non farai con quei dati? Classifiche, caccia al colpevole, sorveglianza
- chi li vedrà, e con quale dettaglio?
Poi mantieni la promessa. Se una commessa sfora, il dato serve a rivedere il preventivo con il cliente, non a cercare chi ha sbagliato. Basta una sola volta in cui il dato viene usato contro qualcuno, e la fiducia se ne va.
## La fatica conta più di quanto pensi
Puoi avere le parole migliori del mondo, ma se compilare un rapportino richiede dieci minuti e tre schermate, nessuno lo farà volentieri. Il cervello odia la fatica inutile: la rimanda.
Per questo lo strumento deve essere rapidissimo, usabile dal telefono nel momento esatto in cui il lavoro finisce. Pochi secondi, e via.
## Restituisci qualcosa
Un timesheet funziona davvero quando è utile anche a chi lo compila. Vedere a colpo d'occhio le giornate complete, ritrovare cosa hai fatto la settimana scorsa, avere numeri concreti per dire «questa commessa ha richiesto il doppio del previsto»: sono vantaggi per chi lavora, non solo per l'azienda.
Quando i dati diventano un modo per difendere il proprio lavoro, invece che per metterlo in discussione, cambia tutto.
## Due regole pratiche
Chiedi di registrare le ore ogni giorno, senza l'ansia del minuto esatto. E verifica con il tuo consulente le norme su privacy e controlli a distanza, e come informare i dipendenti.
## Come aiuta Tymex
Tymex nasce proprio per togliere fatica: è la persona stessa a registrare le proprie ore, dallo smartphone o dal web, in pochi tap. Il calendario mostra subito quali giornate sono complete e un rapportino ricorrente si duplica con un tocco. Chi ha il profilo base vede i propri rapportini; la gestione del team spetta a manager e amministratori.
## In sintesi
Il software è la parte facile. Il resto lo fanno tre cose: le parole con cui lo presenti, la velocità con cui si usa e il modo in cui userai i dati. Fai bene queste tre, e la rilevazione ore smette di essere un controllo. Diventa un modo per lavorare meglio, insieme."""),
]
