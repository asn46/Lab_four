"""
Lab 4
Aseem Nerlekar, Gaurav Purushothaman
This assignment is to demonstrate implemention of Binary Search Trees and all its functionalities
"""


from bstnode import BSTNode
from queue import Queue

class BinarySearchTree():
    def __init__(self, root=None):
        self.root = root


    @property
    def root(self):
        """ Property method which gives root of the BinarySearchTree
        pre:
        post:
        return: root - a pointer to a BSTNode object or None
        """
        return self._root

    
    @root.setter
    def root(self, bst_node):
        """ Setter method to set root of the BinarySearchTree to the BSTNode object
        pre: bst_node object of the BSTNode class
        post: TypeError if bst_node not of the BSTNode class
        return: 
        """
        if not isinstance(bst_node, BSTNode) and not bst_node is None:
            raise TypeError("Input must be a BSTNode object")
        self._root = bst_node

    def __del__(self):
        """ Destructor method to delete Binary Search Tree
        pre: 
        post: the tree makes itself empty - root becomes None so rest of the tree is garbage collected
        return: 
        """
        self.empty_tree()


    def search(self, in_data):
        """ Search method to find node that contains data that is input
        pre: in_data - a Drachma object 
        post:
        return: returns BSTnode object whose data matches in_data if found otherwise None
        """
        current_node = self.root
        while current_node is not None: 
            if current_node.data.get_Value() == in_data.get_Value():
                return current_node
            elif in_data.get_Value() < current_node.data.get_Value():
                current_node = current_node.left
            else:
                current_node = current_node.right
        
        return None
    

    def insert_node(self, node):
        """Find node that contains data that is input. This method is called by insert method
        pre: node - a BSTNode object
        post: node is inserted into the tree per its data value
        return:
        """
        if self.root is None:
            self.root = node
        else:
            current_node = self.root
            while current_node is not None:
                if (node.data.get_Value() <  current_node.data.get_Value()):
                    if current_node.left is None:
                        current_node.left = node
                        current_node = None
                    else:
                        current_node = current_node.left
                else: 
                    if current_node.right is None:
                        current_node.right = node
                        current_node = None
                    else:
                        current_node = current_node.right
    

    def contains(self, data):
        """Finds whether a node matching input data exists in the tree
        pre: data - a Drachma object
        post: 
        return: boolean - True if node is found containing this data, otherwise False
        """
        return self.search(data) is not None
    

    def insert(self, data):
        """Inserts node with input data into the tree. Checks for existing node first to avoid duplicates
        pre: data - a Drachma object
        post: node with input data inserted into the tree if no duplicate exists already
        return: boolean - True if node inserted, otherwise False, indicating duplicate
        """
        if self.contains(data):
            return False
        new_node = BSTNode(data)
        self.insert_node(new_node)
        return True
    

    def delete(self, data):
        """Removes node that matches input data from the tree
        pre: data - a Drachma object
        post: node matching input data removed from the tree
        return: boolean - True if node with matching data removed, otherwise False if not found
        """
        parent = None
        current_node = self.root
        while current_node is not None:
            if current_node.data.get_Value() == data.get_Value():
                
                if current_node.left is None and current_node.right is None:
                    if parent is None: 
                        self.root = None
                    elif parent.left == current_node:
                        parent.left = None
                    else: 
                        parent.right = None
                    return True
                
                elif current_node.right is None:
                    if parent is None: 
                        self.root = current_node.left
                    elif parent.left == current_node:
                        parent.left == current_node.left
                    else: 
                        parent.right = current_node.left
                    return True 

                elif current_node.left is None:
                    if parent is None:
                        self.root = current_node.right
                    elif parent.left == current_node:
                        parent.left == current_node.right
                    else: 
                        parent.right = current_node.right
                    return True

                else:   
                    successor = current_node.right
                    while successor.left is not None:
                        successor = successor.left
                    current_node.data = successor.data
                    parent = current_node
                    current_node = current_node.right
                    data = successor.data
            
            elif data.get_Value() > current_node.data.get_Value():
                parent = current_node
                current_node = current_node.right
            
            else: 
                parent = current_node
                current_node = current_node.left
        
        return False 
    

    def print(self):
        """Returns the default inorder traversal to print contents of the tree
        pre:
        post: prints tree contents to console via inorder traversal
        return:
        """
        return self.inorder_traverse(self.root)


    def count(self):
        """Counts the number of nodes in the tree. Uses recursive helper function
        pre:
        post:
        return: integer value of number of nodes in the tree
        """
        return self._recursive_count(self.root)
        

    def _recursive_count(self, node):
        """Helper method to recursively count nodes in the tree
        pre:
        post:
        return: 0 if node is None, otherwise 1 + recursive call to this function for both left and right nodes
        """
        if node is None:
            return 0
        else:
            return 1 + self._recursive_count(node.left) + self._recursive_count(node.right)


    def is_empty(self):
        """Indicates whether the tree is empty or not
        pre:
        post:
        return: boolean - True if root is None (indicating the tree is empty) or False otherwise
        """
        return self.root is None


    def empty_tree(self):
        """ Makes the tree empty
        pre: 
        post: tree root set to None so rest of the tree is garbage collected
        return: 
        """
        self.root = None


    def breadth_first_traverse(self, output_object=None):
        """Traverses the tree in breadth first order using a queue and prints its contents. Optionally outputs to an output_object file
        pre: Optional: output_object - a file
        post: prints contents of tree in breadth first order to the console
        return: 
        """        
        if self.root is not None:
            current_node = self.root
            bf_queue =  Queue()
            while current_node is not None:
                print(str(current_node.data.get_Value()) + ", ", end='')
                if output_object:
                    output_object.write(str(current_node.data.get_Value()) + ", ")
                if current_node.left is not None:
                    bf_queue.enqueue(current_node.left.data)
                if current_node.right is not None:
                    bf_queue.enqueue(current_node.right.data)
                if not bf_queue.isQueueEmpty():
                    current_node = self.search(bf_queue.dequeue())
                else:
                    current_node = None 
                
            del bf_queue 


    def inorder_traverse(self, current_node, output_object=None):
        """Traverses the tree via inorder traversal and prints its contents. Optionally outputs to an output_object file
        pre: current_node - BSTNode object ; Optional: output_object - a file
        post: prints contents of tree in inorder order
        return: 
        """     
        if current_node.left is not None:
            self.inorder_traverse(current_node.left, output_object)
        print(str(current_node.data.get_Value()) + ", ", end='')
        if output_object:
            output_object.write(str(current_node.data.get_Value()) + ", ")
        if current_node.right is not None:
            self.inorder_traverse(current_node.right, output_object)

    
    def preorder_traverse(self, current_node, output_object=None):
        """Traverses the tree via preorder traversal and prints its contents. Optionally outputs to an output_object file
        pre: current_node - BSTNode object ; Optional: output_object - a file
        post: prints contents of tree in preorder order
        return: 
        """    
        print(str(current_node.data.get_Value()) + ", ", end='')
        if output_object:
            output_object.write(str(current_node.data.get_Value()) + ", ")
        if current_node.left is not None:
            self.preorder_traverse(current_node.left, output_object)
        if current_node.right is not None:
            self.preorder_traverse(current_node.right, output_object)


    def postorder_traverse(self, current_node, output_object=None):
        """Traverses the tree via postorder traversal and prints its contents. Optionally outputs to an output_object file
        pre: current_node - BSTNode object ; Optional: output_object - a file
        post: prints contents of tree in postorder order
        return: 
        """    
        if current_node.left is not None:
            self.postorder_traverse(current_node.left, output_object)
        if current_node.right is not None:
            self.postorder_traverse(current_node.right, output_object)
        print(str(current_node.data.get_Value()) + ", ", end='')
        if output_object:
            output_object.write(str(current_node.data.get_Value()) + ", ")
