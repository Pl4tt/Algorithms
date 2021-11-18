class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        return self.stack.pop()
    
    def is_empty(self):
        return not self.stack

    def size(self):
        return len(self.stack)
    
    def peek(self):
        return self.stack[-1]


if __name__ == "__main__":
    stack = Stack()
    for i in range(20):
        stack.push(i)
    
    print(stack.size())

    while not stack.is_empty():
        x = stack.pop()
        print(x)