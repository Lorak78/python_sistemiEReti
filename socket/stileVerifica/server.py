"""
si vuole gestire un servizio di prenotazioni
il cliente si prenota e dopo 15 secondi viene cancellato
dalla lista dei prenotati

il server deve tenere traccia di chi si è prenotato e
controllare se un cliente si è già prenotato prima di aggiungerlo
"""
import socket
import threading
import time

MY_ADDRESS = ("127.0.0.1", 43211)
BUFFER_SIZE = 4096

lista_prenotazioni = []

class Client_handler(threading.Thread):
    def __init__(self, connection):
        super().__init__()
        self.connection = connection

    def run(self):
        global lista_prenotazioni

        message = self.connection.recv(BUFFER_SIZE)

        print(f"{message.decode()} si è prenotato")
        lista_prenotazioni.append(message.decode())

class Timer(threading.Thread):
    def __init__(self, sleep_time) -> None:
        super().__init__()
        self.sleep_time = 15
    
    def run(self):
        while True:
            global lista_prenotazioni
            time.sleep(self.sleep_time)
            if len(lista_prenotazioni) != 0:
                lista_prenotazioni = lista_prenotazioni[1:]
                print(lista_prenotazioni)


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    t = Timer(15)
    s.bind(MY_ADDRESS)
    s.listen()
    
    t.start()

    while True:
        connection, _ = s.accept()#bloccante
        thread = Client_handler(connection)
        thread.start()

if __name__ == "__main__":
    main()