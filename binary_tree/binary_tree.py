#####################################################
#This program is the implementation of a binary tree: 2, 3,4, 5 
#####################################################

class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

# Initialize and allocate memory for tree nodes
firstNode = Node(2)
secondNode = Node(3)
thirdNode = Node(4)
fourthNode = Node(5)

# Connect binary tree nodes
firstNode.left = secondNode
firstNode.right = thirdNode
secondNode.left = fourthNode