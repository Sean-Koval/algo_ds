class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

# create 4 nodes

n1 = Node("Root Node")
n2 = Node("Left child node")
n3 = Node("right chid node")
n4 = Node("left grandchild node")

# next, connect the nodes together

n1.left_child = n2
n1.right_child = n3
n2.left_child = n4

# traverse the tree

current = n1
while current:
    print(current.data)
    current = current.left_child

# output in order (root node, left child node, left grandchild node)