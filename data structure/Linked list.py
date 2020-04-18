class Node:
    def __init__(self, n):
        self.data = n
        self.next = None
    def getdata(self):
        return self.data
    def getnext(self):
        return self.next
    def setnext(self, new_next):
        self.next = new_next

class Linked_list:
    def __init__(self):
        self.root = None
        self.size = 0
    def Size(self):
        return self.size

    def add_Node(self, n):
        new_node = Node(n)
        if self.root is None:
            self.root = new_node
            return
        n = self.root
        while n.next is not None:
            n = n.next
        n.next = new_node
    def printList(self):
        temp = self.root
        while(temp):
            print(str(temp.data))
            temp = temp.next
l = Linked_list()
l.add_Node('A')
l.add_Node('B')
l.add_Node('C')
l.add_Node('D')
l.printList()