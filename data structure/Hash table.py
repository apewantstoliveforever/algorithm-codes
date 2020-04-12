class hash_table:
    def __init__(self):
        self.size = 5
        self.table = [None]*self.size

    def hash_key(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash%self.size

    def add(self, key, value):
        hash = self.hash_key(key)
        character = [key, value]
        if self.table[hash] is None:
            self.table[hash] = list([character]) ########### will get error when add into not None element
            return True
        else:
            for pair in self.table[hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.table[hash].append(character)
            return True
    def get(self, key):
        hash = self.hash_key(key)
        if self.table[hash] is None:
            return None
        for pair in self.table[hash]:
            if pair[0] == key:
                return pair[1]
    def delete(self, key):
        hash = self.hash_key(key)
        for i in range(len(self.table[hash])):
            if self.table[hash][i][0] == key:
                self.table[hash].pop(i)
h = hash_table()
h.add('aaa', 7)
h.add('aav', 5)
h.add('op', 3)
h.add('yu', 45)
print(h.table)
print(h.get('op'))
h.delete('aaa')
print(h.table)