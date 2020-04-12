class queue:
    def __init__(self):
        self.items = []
    def push(self, item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop(0)
    def delay(self):
        return self.items

a = queue()
a.push(5)
a.push(7)
a.push(3)
a.pop()
print(a.delay())