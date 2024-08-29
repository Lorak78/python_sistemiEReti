"""
si vuole gestire un servizio di prenotazioni
il cliente si prenota e dopo 15 secondi viene cancellato
dalla lista dei prenotati

il server deve tenere traccia di chi si è prenotato e
controllare se un cliente si è già prenotato prima di aggiungerlo
"""
import socket

SERVER_ADDRESS = ("127.0.0.1", 43211)
BUFFER_SIZE = 4096

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(SERVER_ADDRESS)

    s.sendall(input("-> ").encode())

    s.close()

if __name__ == "__main__":
    main()