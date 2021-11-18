class Queue:
    def __init__(self):
        self.queue = []
    
    def push(self, value):
        self.queue.append(value)

    def pop(self):
        return self.queue.pop(0)
    
    def is_empty(self):
        return not self.queue

    def size(self):
        return len(self.queue)
    
    def peek(self):
        return self.queue[0]



if __name__ == "__main__":
    queue = Queue()
    for i in range(20):
        queue.push(i)
    
    print(queue.size())

    while not queue.is_empty():
        x = queue.pop()
        print(x)