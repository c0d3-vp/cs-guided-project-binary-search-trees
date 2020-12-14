"""
Let's implement a binary search tree class and 'search' methods.
"""
class BSTNode:
    def _init_(self, value):
        self.value = value
        self.left = None
        self.right = None

    """ 
    Inserts the input value into our BST
    Doesn't return anything
    Base case: stop recursing when we find an empty spot in the tree to place the value
    How do we move closer to the base case: At each node in the BST, compare the current node's value against the input value.  Decide if we go left or right.  If there's already a child node in the direction we need to go in, continue recursing.
    """
    def insert(self, value):
    # if value == self.value:
    #     return
    if value < self.value:
        if self.left is not None:
            self.left.insert(value)
        else:
            self.left = BSTNode(value)
    
    else:
        if self.right is not None:
            self.right.insert(value)
        else:
            self.right = BSTNode(value)    

    def search(self, value):
        if self.value == target:
            return True
        elif target < self.value:
            if self.left if None:
                return False
            else:
                return self.left.search(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.search(target)