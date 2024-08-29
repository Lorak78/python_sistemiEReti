import socket
from threading import Thread

SERVER_ADDRESS = ("127.0.0.1", 9000)
MY_ADDRESS = ("0.0.0.0", 43210)

BUFFER_SIZE = 4096

class Receiver(Thread):
    def __init__(self, socket):
        super().__init__()
        self.socket = socket
        self.running = True
    def run(self):
        while self.running:
            data, sender_address = self.socket.recvfrom(BUFFER_SIZE)
            string = data.decode()
            print(f"{sender_address}: {string}")

    def kill(self):
        self.running = False

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(MY_ADDRESS)
    ready= True
    receiver = Receiver(s)
    while True:
        string = input("-> ")
        s.sendto(string.encode(), SERVER_ADDRESS)
        
        if ready:
            receiver.start()
            ready= False

if __name__ == "__main__":
    main()