class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
    	self.head = None
    	self.tail = None

    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        return new_node

    def link_nodes(self, node1, node2):
        node1.next = node2
        node2.prev = node1

    def traverse(self):
        visited = []
        current = self.head
        while current:
            visited.append(current)
            current = current.next
            # Esto lo he tenido que solucionar yo,
            # porque la IA se ha quedado pajarito.
            # jajajajajajja
            if current == self.head:
                break
        return visited