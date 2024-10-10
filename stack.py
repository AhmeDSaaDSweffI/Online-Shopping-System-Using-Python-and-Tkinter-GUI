class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return None if self.isEmpty() else self.items.pop()

    def peek(self):
        return None if self.isEmpty() else self.items[-1]

    def stacksize(self):
        return len(self.items)
