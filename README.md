# GenerativeRansomware

# 1 Introduzione
Il presente workshop è stato progettato per introdurti alla Generative AI e per sensibilizzarti su come utenti malintenzionati potrebbero utilizzare questo strumento per scopi malevoli. Attraverso una serie di esercizi pratici, esploreremo come utilizzare la Generative AI per simulare la creazione e l'esecuzione di un ransowmare. Ciascun esercizio è stato strutturato per potenziare la comprensione e le abilità pratiche nel prompt engineering. Questa simulazione verrà eseguita attraverso l'utilizzo del modello di OpenAI ed il framework LangChain.

## 1.3 Obiettivi
Al termine di questo workshop, l'utente sarà in grado di comprendere il funzionamento dei ransomware e simulare le loro funzioni principali per scopi educativi. Questo utilizzando esclusivamente la Generative AI, senza scrivere direttamente il codice. L'obiettivo è aumentare la consapevolezza sulla sicurezza informatica e promuovere la difesa contro minacce informatiche.

## 1.4 Disclaimer
Le conoscenze condivise in questo workshop sono da intendersi esclusivamente per scopi educativi. L'uso delle tecniche presentate fuori da un contesto di apprendimento può costituire una violazione delle leggi vigenti e avere gravi conseguenze legali. Incoraggiamo sempre ad adottare un approccio responsabile ed etico all'utilizzo della GenAI, per costruire un futuro digitale più sicuro e consapevole.

Per la realizzazione di questo notebook è stato utilizzato il più recente modello GPT-4 Turbo, i cui Training Data risalgono fino a dicembre 2023 e consente una finestra di contesto fino a 128.000 token. Si prega di notare che l'utilizzo di un modello alternativo e/o con prestazioni differenti potrebbe non garantire gli stessi risultati. Si specifica che alla prima registrazione, OpenAI offre all'utente 5$ in omaggio utilizzabili per il modello GPT3.5 (gpt-3.5-turbo). Gli stessi sono sufficienti per eseguire il workshop, ma non garantiscono le stesse prestazioni.

I modelli GPT (Generative Pre-trained Transformer) sono progettati per comprendere e rispondere a domande in molteplici lingue, tra cui l'inglese e l'italiano. Tuttavia, è vero che la qualità delle risposte può variare a seconda della lingua utilizzata, principalmente a causa della quantità e della varietà dei dati di addestramento disponibili. L'inglese, essendo una delle lingue più comunemente usate online e nei dati di addestramento di molti modelli di intelligenza artificiale, tende a produrre risposte più precise e dettagliate, poiché il modello ha avuto accesso a una quantità maggiore di informazioni durante la fase di addestramento.

Quando si utilizzano i modelli GPT di OpenAI, è fondamentale ricordare che le loro risposte possono variare a causa della non deterministicità intrinseca nel processo di generazione del testo. Questo significa che, presentando la stessa richiesta al modello più volte, si potrebbero ottenere risultati differenti in occasioni diverse. Tale variabilità è dovuta al modo in cui i modelli GPT esplorano e selezionano le possibili risposte da un vasto spazio di opzioni, basandosi su probabilità e contesto. Pertanto, è consigliabile interpretare le risposte fornite dai modelli GPT con un approccio critico e considerarle come una delle molteplici prospettive possibili, piuttosto che come soluzioni definitive o esatte.

# 2 Architettura Progetto
Project/<br/>
║<br/>╠══ Malicious_Server/<br/>║     ║<br/>
║     ╚══Server.py<br/>
║         - File Python che istanzia un server FTP per il controllo del sistema di attacco.<br/>
║<br/>
╠══ Target/<br/>
║     ║<br/>
║     ╠══Documents/<br/>
║     ║     ║<br/>
║     ║     ╠══employees_personal_info.rtf<br/>
║     ║     ╚══wallet_bitcoin.txt<br/>
║     ║         - File generati da 'Folder_Generator.py'<br/>
║     ╚══Ransomware.py<br/>
║          - Viene generato durante dell'Esercizio 1 di 'Workbook_Ransomware_generator.ipynb'.<br/>
║          - Viene aggiornato iterativamente con gli esercizi successivi.<br/>
║<br/>
╠══ Utilities/<br/>
║     ║<br/>
║     ╚══Folder_Generator.py<br/>
║         - File Python che:<br/>
║          - Crea la cartella 'Documents' per simulare il sistema della vittima.<br/>
║          - Svuota la cartella 'Malicious_Server', ad eccezione del file 'Server.py'.<br/>
║<br/>
╚══ Workbook_Ransomware_generator.ipynb:<br/>
     - Notebook contenente gli esercizi da svolgere durante il workshop.<br/>

# 3 Installazione pre-requisiti
## 3.1 Installazione Python
Per utilizzare le librerie Python di OpenAI e LangChain, è necessario assicurarsi di avere Python installato correttamente sul proprio sistema. Alcuni Sistemi Operativi già prevedono l'installazione di Python, mentre su altri è necessario configurarlo manualmente. Per verificarne l'installazione, puoi accedere al Terminale o alla riga di comando (su Windows, puoi trovarlo cercando "cmd" nel menu Start), quindi digitare "python" e premere Invio. Se viene visualizzato l'interprete Python, significa che è già installato sul tuo computer. Al contrario, se ricevi un messaggio di errore, dovrai probabilmente procedere con l'installazione di Python attraverso il Microsoft Store o dal sito ufficiale[https://www.python.org/downloads/] e renderlo disponibile nel tuo terminale/riga di comando.

## 3.2 Installazione Visual Studio Code
Un Ambiente di Sviluppo Integrato (IDE) è cruciale per programmare in modo efficiente, fornendo funzionalità come l'editing del codice, la gestione dei progetti e il debugging in un unico strumento. Il nostro consiglio è di approcciarsi a questo notebook attraverso l'utilizzo di Visual Studio Code scaricabile attraverso il Microsoft Store.

## 3.3 Import progetto in Visual Studio Code
Scaricare la cartella di progetto "Project" e caricarla su Visual Studio Code.

```File -> Open Folder -> Project```

## 3.4 Creazione ambiente virtuale / terminale
Creazione ambiente virtuale (fornisce uno spazio di lavoro pulito per l'installazione dei pacchetti Python in modo da non avere conflitti con altre librerie installate per altri progetti):

- ```Terminal -> New Terminal```
- ```python -m venv venv```
- ```.\\venv\Scripts\activate```
- 
### 3.4.1 Troubleshooting
Qualora riscontrassi errori del tipo:

.\\venv\Scripts\activate : Impossibile caricare il file C:\Users\User\Desktop\ransomware\venv\Scripts\Activate.ps1. L'esecuzione di script è disabilitata nel sistema in uso. Per ulteriori informazioni, vedere about_Execution_Policies all'indirizzo
https://go.microsoft.com/fwlink/?LinkID=135170.
In riga:1 car:1
Sarà necessario disabilitare i criteri di restrizione di PowerShell ed impostare i criteri di esecuzione su Senza restrizioni. Questo sarà possibile effettuarlo attraverso i seguenti passaggi:

- Esegui come amministratore PowerShell
- digita ```Set-ExecutionPolicy Unrestricted```
- digita ```s```

## 3.5 Installazione dei pacchetti python
Una volta installato Python e configurato un ambiente virtuale, è possibile installare le librerie necessarie.

Questo notebook richiede l'installazione di diversi pacchetti Python, tra cui:

- **openai** fornisce un comodo accesso all'API OpenAI, consentendo di utilizzare le funzionalità offerte dalla piattaforma OpenAI.
- **langchain** è una libreria che semplifica la creazione di applicazioni basate su LLM.
- **langchain-openai** è un'estensione del pacchetto LangChain che integra specificamente le funzionalità di OpenAI.
- **ipykernel** pacchetto Python che fornisce il kernel per Jupyter, permettendo a Jupyter Notebook / JupyterLab o Visual Studio di eseguire codice Python.
- **pyftpdlib** Una libreria Python per creare server FTP facilmente.
- **cryptography** Un pacchetto Python per crittografia e sicurezza dei dati.
- **tk** Toolkit GUI di Python per creare interfacce utente grafiche.
Si prega di eseguire da terminale (in ambiente virtuale) il comando sottostante. Esso, contiene i comandi essenziali per l'installazione di tutti i pacchetti Python necessari per eseguire il notebook in modo corretto. Questo passaggio è fondamentale per l'esecuzione di qualsiasi altra parte del notebook.

```pip install openai langchain langchain-openai ipykernel pyftpdlib cryptography tk```

**N.B.**: Visual studio potrebbe richiedere di installare dipendenze suggerite. Inoltre, alla richiesta di selezione del Kernel, fare click su Python Evironments e successivamente selezionare il virtual enviroment precedentemente nominato venv

## 3.6 Creazione file target
Assicurarsi di creare i file target per l'esercizio del workbook. Il progetto viene già fornito con dei file di esempio. Il seguente codice permette di rigenerare i file in caso di errore.

```%run ./Utilities/Folder_Generator.py    # reset cartelle```


## 3.7 Creazione funzione di test
Utilizza la funzione successiva per copiare direttamente il codice generato dall'LLM in un file Python denominato 'Ransomware.py'. Il codice Python generato dall'LLM di solito si trova tra tag specifici, per cui assicurati di salvare solo il codice rilevante per l'esecuzione del programma. Utilizzeremo tale funzione per testare i risultati generate dagli esercizi nel seguito.

```import os 

def create_ransom(response):
    target_folder = "Target"

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    with open(os.path.join(target_folder, "Ransomware.py"), "w") as file:
        text = response["text"]
        if "```python" in text and "```" in text:
            start_index = text.index("```python") + len("```python")
            end_index = text.index("```", start_index)
            python_code = text[start_index:end_index].strip()
            file.write(python_code + "\n")
        else:
            file.write(text + "\n")
    
    return True
```

## 3.8 Avvio server C2
Per simulare un sistema di Command & Control, per questo workshop è stato predisposto un file Python chiamato 'Server.py' all'interno della cartella 'Malicious_Server'. Questo script:

istanzia un Server FTP in ascolto sull'indirizzo IP locale 127.0.0.1 e sulla porta 1337.
configura all'interno del Server un'utenza con username 'user' e password 'pass'.
Puoi utilizzare il seguente codice per attivare il Server FTP in un nuovo terminale e assicurati di lasciarlo in esecuzione per l'intera durata del notebook. Se il server viene chiuso accidentalmente, basta rieseguire questo codice per riattivarlo.

```import platform, subprocess, sys

file_path = "./Malicious_Server/Server.py"
 
if platform.system() == "Windows":
    subprocess.Popen(["start", "cmd", "/k", sys.executable, file_path], shell=True)
elif platform.system() == "Linux":
    subprocess.Popen(["gnome-terminal", "--", sys.executable, file_path])
elif platform.system() == "Darwin":  # macOS
    subprocess.Popen(["open", "-a", "Terminal.app", sys.executable, file_path])
```
