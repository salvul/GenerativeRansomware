import os
import shutil

print("Inizializzazione ambiente ...")

# Funzione per creare la cartella 'Documents' e i file al suo interno
def create_documents_folder():
    # Verifica se la cartella 'Target' esiste già
    target_path = './Target'
    if os.path.exists(target_path):
        # Crea la cartella 'Documents' dentro 'Target'
        documents_path = os.path.join(target_path, 'Documents')
        if os.path.exists(documents_path):
            # Se la cartella 'Documents' esiste, la cancella con tutto il suo contenuto
            for root, dirs, files in os.walk(documents_path, topdown=False):
                for file in files:
                    os.remove(os.path.join(root, file))
                for dir in dirs:
                    os.rmdir(os.path.join(root, dir))
            os.rmdir(documents_path)
            print("Cartella 'Documents' e il suo contenuto sono stati cancellati.")

        # Crea nuovamente la cartella 'Documents'
        os.mkdir(documents_path)
        print("Cartella 'Documents' creata con successo.")
        
        # Crea il file .txt dentro 'Documents'
        with open(os.path.join(documents_path, 'wallet_bitcoin.txt'), 'w') as f:
            f.write("Indirizzo del Wallet Bitcoin: 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa\nChiave Privata del Wallet Bitcoin: L5LbsX8MNwSxu92V4TUDqb6B7zmWcjJ9UwhqykxSPGEGHb4NHM2S\n")
            f.write("Wallet Bitcoin:\n\n")
            f.write("Indirizzo: 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa\n")
            f.write("Chiave privata: 5Kb8kLf9zgWQnogidDA76MzPL6TsZZY36hWXMssSzNydYXYB9KF\n\n")
            f.write("Bilancio Bitcoin: 2.5 BTC\n")
            f.write("Transazioni recenti:\n")
            f.write("- 2023-03-21: Ricevuto 1.0 BTC da 1Mz7153HMuxXTuR2R1t78mGSdzaAtNbBWX\n")
            f.write("- 2023-03-22: Inviato 0.5 BTC a 1Q2TWHE3GMdB6BZKafqwxXtWAWgFt5Jvm3\n")
        print("File 'wallet_bitcoin.txt' creato con successo.")
        
        # Crea il file .rtf dentro 'Documents'
        with open(os.path.join(documents_path, 'employees_personal_info.rtf'), 'w') as f:
            f.write("Informazioni personali dello staff. Comprende accessi ad asset critici aziendali.\n")
            f.write("Nome: John Doe\n")
            f.write("Età: 35 anni\n")
            f.write("Ruolo: Amministratore di Sistema\n\n")
            f.write("Informazioni personali:\n")
            f.write("- Indirizzo: 123 Via Principale, Città, Stato, CAP\n")
            f.write("- Numero di telefono: +1 (555) 123-4567\n")
            f.write("- Indirizzo email: john.doe@example.com\n\n")
            f.write("Credenziali di accesso:\n")
            f.write("- Nome utente: johndoe_admin\n")
            f.write("- Password: S3cur3P@ssw0rd!\n\n")
            f.write("Ruolo e Responsabilità:\n")
            f.write("John Doe è un amministratore di sistema presso XYZ Corporation. Ha accesso a una vasta gamma di asset critici aziendali, inclusi server, database e applicazioni. Le sue responsabilità includono la gestione delle credenziali di accesso, l'implementazione delle politiche di sicurezza informatica e la risoluzione dei problemi tecnici relativi all'infrastruttura IT aziendale. Inoltre, è responsabile della protezione e della sicurezza dei dati sensibili dell'azienda.\n")
        print("File 'employees_personal_info.rtf' creato con successo.")
    else:
        print("La cartella 'Target' non esiste.")

# Funzione per pulire la cartella 'Malicious_Server'
def clean_server_folder():
    # Verifica se la cartella 'Malicious_Server' esiste già
    server_path = 'Malicious_Server'
    if os.path.exists(server_path):
        for root, dirs, files in os.walk(server_path, topdown=False):
            # Cancella il contenuto della cartella 'Malicious_Server' al di fuori del file 'Server.py'
            for name in files:
                file_path = os.path.join(root, name)
                if name != 'Server.py':
                    os.remove(file_path)
            # Elimina la sottocartella e tutto il suo contenuto
            for name in dirs:
                dir_path = os.path.join(root, name)
                # Verifica se la sottocartella non contiene 'Server.py'
                if not os.path.exists(os.path.join(dir_path, 'Server.py')):
                    shutil.rmtree(dir_path)
        print("Contenuto della cartella 'Malicious_Server' pulito.")
    else:
        print("La cartella 'Malicious_Server' non esiste.")

# Chiamata alla funzione per creare la cartella 'Documents' e i file al suo interno
create_documents_folder()

# Chiamata alla funzione per pulire la cartella 'Malicious_Server'
clean_server_folder()
