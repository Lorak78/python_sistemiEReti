class Queue():
    def __init__(self) -> None:
        self.lista = []

    def is_empty(self):
        return len(self.queue) == 0
    
    def enqueue(self, elem):
        self.queue.append(elem)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop()
        
        return None
    
    def stampa(self):
        print(self.queue)


def main():
    queue = Queue()

if __name__ == "__main__":
    main()
    