class Node:
    
    def __init__(self, data=None):
        self.data = data
        # unless the value is changed to next, this will be the endpoint
        self.next = None
    def __str__(self):
        return str(data)
    
# create the nodes for the linked list
n1 = Node('eggs')
n2 = Node('ham')
n3 = Node('bacon')


# link the nodes together
n1.next = n2
n2.nest = n3

current = n1
while current:
    print(current.data)
    current = current.next
