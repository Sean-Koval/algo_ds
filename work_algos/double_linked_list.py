class Node(object):
    """A double-linked list node"""
    def __inti__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
    
class DoubleLinkedList(Node):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    def append(self, data):
        """Append an item to the list"""
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        self.count += 1
    
    def iter(self):
        """Iterate through the list"""
        current = self.head
        while current:
            val = current.data
            current = current.next 
            yield val
    
    def reverse_iter(self):
        """Iterate backwards through a list"""
        current = self.tail
        while current:
            val = current.data
            current = current.prev 
            yield val
    
    def delete(self, data):
        """Delete a node from the list"""
        current = self.head
        node_deleted = False
        if current is None:
            node_deleted = False
        
        elif current.data == data:
            self.head = current.next
            self.head_prev = None
            node_deleted = True
        
        elif self.tail.data == data:
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True
        
        else:
            while current:
                if current.data == data:
                    current.prev.next = current.next 
                    current.next.prev = current.current.prev 
                    node_deleted = True
                current = current.next
        
        if node_deleted:
            self.count -= 1
        
    
    def search(self, data):
        """Search through the list and return True if the value is found"""
        for node in self.iter():
            if data == node:
                return True
        return False
    
    def print_forward(self):
        """Print nodes in list from first node inserted"""
        for node in self/iter():
            print(node)
    
    def print_backwarc(self):
        """Print nodes in the list from latest to first node"""
        current = self.tail
        while current:
            print(current.data)
            current = current.prev
    
    def insert_head(self, data):
        """Insert new node at the head of the linked list"""
        
        if self.head is not None:
            new_node = Node(data, None, None)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.count += 1
    
    def reverse(self):
        """Reverse the linked list"""
        current = self.head 
        while current:
            temp = current.next
            current.next = current.prev
            current.prev = temp
            current = current.prev
        
        # reverse the order of the head and tail
        temp = self.head
        self.head = self.tail
        self.tail = temp
    
    def __getitem__(self, index):
        if index >  self.count -1:
            raise Exception("Index out of range")
        current = self.head
        for n in range(index):
            current = current.next 
        current.data = value

        
dll = DoublyLinkedList()
dll.append("foo")
dll.append("bar")
dll.append("biz")
dll.append("whew")
print("Items in List : ")
dll.print_foward()
print("List after deleting node with data whew")
dll.delete("whew")
dll.print_foward()

print("List count: {}".format(dll.count))
print("Print list backwards")
dll.print_backward()

print("Reverse list ")
dll.reverse()
dll.print_foward()

print("Append item to front of list")
dll.insert_head(55)
dll.print_foward()

print("Get First element: {}".format(dll[0]))
