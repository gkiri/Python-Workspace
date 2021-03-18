class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __repr__(self):
        return self.value
    
class LinkedList:
    def __init__(self):
        self.head = None


    def __repr__(self):
        node = self.head
        nodes = []
        while node:
            nodes.append(node.value)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


    def append(self, value):
        if not self.head:
            self.head = Node(value)
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next
        
        curr.next = Node(value)
    
    def contains(self, value):
        node = self.head
        while node:
            if node.value == value: return True
            node = node.next
        return False


llist = LinkedList()
llist.append('a')
llist.append('b')
llist.append('c')
llist.append('d')
print(llist)


print(llist.contains('a'))
print(llist.contains('b'))
print(llist.contains('c'))
print(llist.contains('d'))
print(llist.contains('z'))
print(llist.contains('x'))
