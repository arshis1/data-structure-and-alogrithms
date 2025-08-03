##################################################################
#This program is the implementation of a binary tree: 2, 3, 4, 5 
#################################################################

class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None
        self.count = 1 #to handle duplicates.

    def insert(self, value):
        if value == self.val:
            self.count +=1
        elif value < self.val:
            if self.left is None:
                self.left = Node(value)
            else:
                self.count +=1
                self.left.insert(value)
        elif value > self.val:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def search(self, target):
        if target == self.value:
            return True 
        elif target <self.value:
            #since this is binary tree, we can ignore the right subtree.
            if self.left is None:
                return  False
            else:
                return self.left.search(target)
        else: #target > self.value
            if self.right is None:
                return False
            else:
                return self.right.search(target)