#   Test whether the BST is maximal
#
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
    
    def rec_height(self, ptr):
            if ptr is None:
                return 0
            else:
                return max(self.rec_height(ptr.left),self.rec_height(ptr.right)) + 1
                
    def height(self):
        return self.rec_height(self.root)
    
def is_maximal(bst):
    return ((2**int(bst.height())) -1 == int(bst.count()))
