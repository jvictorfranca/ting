
class Queue:
    queueList = []
    
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self.queueList = []

    def __len__(self):
        return len(self.queueList)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self.queueList.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        return self.queueList.pop(0)

    def search(self, index):
        if index < 0 or index > len(self.queueList):
            raise IndexError()
        return self.queueList[index]
        """Aqui irá sua implementação"""
