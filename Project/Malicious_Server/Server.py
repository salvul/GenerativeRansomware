from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import os

# Ottiene la directory in cui lo script è situato
script_directory = os.path.dirname(os.path.abspath(__file__))

# Definisce una classe MyFTPHandler personalizzata che eredita da FTPHandler
class MyFTPHandler(FTPHandler):
    def on_file_received(self, file):
        print(f"FILE '{file}' RICEVUTO'\n")

# Istanzia un dummy authorizer per gestire gli utenti 'virtuali'
authorizer = DummyAuthorizer()

# Aggiunge un nuovo utente con permessi di scrittura su tutte le directory e sottodirectory
authorizer.add_user("user", "pass", script_directory, perm="elradfmwMT")

# Istanzia un'istanza dell'Handler FTP personalizzato
handler = MyFTPHandler
handler.authorizer = authorizer

# Specifica l'indirizzo e la porta su cui il server FTP deve ascoltare
server_address = ("127.0.0.1", 1337)

# Istanziare il server FTP con l'Handler personalizzato
server = FTPServer(server_address, handler)

# Start il server FTP
server.serve_forever()


