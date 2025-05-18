from .node import RBNode
from dataclasses import dataclass

@dataclass
class RBTree:

    def __init__(self):
        self.nil = RBNode(None)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def fix_insert(self, new_node):
        current = new_node
        while current != self.root and current.parent.red == True:
            parent = current.parent
            grandparent = current.parent.parent
            
            if parent == grandparent.left:
                uncle = grandparent.right
                if uncle.red == True:
                    uncle.red = False
                    parent.red = False
                    grandparent.red = True
                    current = grandparent

                elif uncle.red == False:
                    if current == parent.right:
                        current = parent
                        self.rotate_left(current)
                        parent = current.parent
                    parent.red = False
                    grandparent.red = True
                    self.rotate_right(grandparent)
                        
                
            elif parent == grandparent.right:
                uncle = grandparent.left
                if uncle.red == True:
                    uncle.red = False
                    parent.red = False
                    grandparent.red = True
                    current = grandparent
                    
                elif uncle.red == False:
                    if current == parent.left:
                        current = parent
                        self.rotate_right(current)
                        parent = current.parent
                    parent.red = False
                    grandparent.red = True
                    self.rotate_left(grandparent)
                    
        self.root.red = False     

    def rotate_left(self, pivot_parent):
        if pivot_parent == self.nil or pivot_parent.right == self.nil:
            return

        pivot = pivot_parent.right
        pivot_parent.right = pivot.left

        if pivot.left != self.nil:
            pivot.left.parent = pivot_parent

        pivot.parent = pivot_parent.parent

        if self.root == pivot_parent:
            self.root = pivot

        elif pivot_parent == pivot_parent.parent.left:
            pivot_parent.parent.left = pivot

        elif pivot_parent == pivot_parent.parent.right:
            pivot_parent.parent.right = pivot

        pivot.left = pivot_parent
        pivot_parent.parent = pivot

    def rotate_right(self, pivot_parent):
        if pivot_parent == self.nil or pivot_parent.left == self.nil:
            return

        pivot = pivot_parent.left
        pivot_parent.left = pivot.right

        if pivot.right != self.nil:
            pivot.right.parent = pivot_parent

        pivot.parent = pivot_parent.parent

        if self.root == pivot_parent:
            self.root = pivot

        elif pivot_parent == pivot_parent.parent.left:
            pivot_parent.parent.left = pivot

        elif pivot_parent == pivot_parent.parent.right:
            pivot_parent.parent.right =  pivot

        pivot.right = pivot_parent
        pivot_parent.parent = pivot

    def insert(self, val):
        new_node = RBNode(val)
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True

        parent = None
        current = self.root
        
        #this while loop looks for a nil node to replace with our new_node
        while current != self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left

            elif new_node.val > current.val:
                current = current.right

            # else return since the value is a duplicate
            else:
                return

        #now parent should reference to our new_node.parent
        new_node.parent = parent

        #if parent in None, we are dealing with the root node
        if parent == None:
            self.root = new_node

        #compare new_node to parent to figure out if it is  right or left child
        elif parent.val > new_node.val:
            parent.left = new_node

        elif parent.val < new_node.val:
            parent.right = new_node

        self.fix_insert(new_node)

    def search(self, val):
        current = self.root
        
        #search tree for value
        while current != self.nil:
            if val < current.val:
                current = current.left
            elif val > current.val:
                current = current.right
            #if both of the statements above aren't true, it means that we found our node
            else:
                return current

        #if nothing was returned in the while loop, it means val doesn't exist in tree
        return None


