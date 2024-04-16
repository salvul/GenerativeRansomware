# GenerativeRansomware

# 1 Introduzione
Il presente workshop è stato progettato per introdurti alla Generative AI e per sensibilizzarti su come utenti malintenzionati potrebbero utilizzare questo strumento per scopi malevoli. Attraverso una serie di esercizi pratici, esploreremo come utilizzare la Generative AI per simulare la creazione e l'esecuzione di un ransowmare. Ciascun esercizio è stato strutturato per potenziare la comprensione e le abilità pratiche nel prompt engineering. Questa simulazione verrà eseguita attraverso l'utilizzo del modello di OpenAI ed il framework LangChain.

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
