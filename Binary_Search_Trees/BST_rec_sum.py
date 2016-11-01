#Sums the elements of a BST recursively.

class Node:
    """ A node in a BST. It may have left and right subtrees """
    def __init__(self, item, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right

class BST:
    """ An implementation of a Binary Search Tree """
    def __init__(self):
        self.root = None

    def add(self, item):
        """ Add this item to its correct position on the tree """
        # This is a non recursive add method. A recursive method would be cleaner.
        if self.root == None: # ... Empty tree ...
            self.root = Node(item, None, None) # ... so, make this the root
        else:
            # Find where to put the item
            child_tree = self.root
            while child_tree != None:
                parent = child_tree
                if item < child_tree.item: # If smaller ... 
                    child_tree = child_tree.left # ... move to the left
                else:
                    child_tree = child_tree.right

            # child_tree should be pointing to the new node, but we've gone too far
            # we need to modify the parent nodes
            if item < parent.item:
                parent.left = Node(item, None, None)
            else:
                parent.right = Node(item, None, None)


    def rec_count_all(self, ptr):
        if ptr == None:
            return 0
        else:
            return 1 + self.rec_count_all(ptr.left) + self.rec_count_all(ptr.right)

    def count(self):
        return self.rec_count_all(self.root)

    
    def rec_total(self, ptr):
        if ptr == None:
            return 0
        else:
            return ptr.item + self.rec_total(ptr.left) + self.rec_total(ptr.right)

    def total(self):
        return self.rec_total(self.root)
