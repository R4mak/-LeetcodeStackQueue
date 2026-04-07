class Stack:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def empty(self):
        return len(self.data) == 0


class MyQueue:
    def __init__(self):
        self.inbox = Stack()
        self.outbox = Stack()

    def push(self, x):
        self.inbox.push(x)

    def _transfer(self):
        if self.outbox.empty():
            while not self.inbox.empty():
                self.outbox.push(self.inbox.pop())

    def pop(self):
        self._transfer()
        return self.outbox.pop()

    def peek(self):
        self._transfer()
        return self.outbox.peek()

    def empty(self):
        return self.inbox.empty() and self.outbox.empty()
