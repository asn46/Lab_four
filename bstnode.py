"""
Lab 4
Aseem Nerlekar, Gaurav Purushothaman
This assignment is to demonstrate implemention of Binary Search Trees and all its functionalities
"""
from drachma import Drachma

class BSTNode():
    def __init__(self, data=None, left=None, right=None):
        self._data = data
        self._left = left
        self._right = right

    @property
    def data(self):
        """ Property method which gives the data to the BinarySearchTree object
        pre:
        post:
        return: data - a pointer to a Drachma object
        """
        return self._data
    
    @data.setter
    def data(self, drachma):
        """ Setter method is to  set data of the Binary Search Tree object to the drachma object
        pre: drachma of the Drachma class
        post: TypeError if drachma not of the Drachma class
        return: 
        """
        if not isinstance(drachma, Drachma):
            raise TypeError("Input must be a Drachma object")
        self._data = drachma
    
    @property
    def left(self):
        """ Property method which gives a left pointer for this node
        pre:
        post:
        return: left - the left pointer value of this node
        """
        return self._left
    
    @left.setter
    def left(self, node):
        """ Setter method is to set data of the BinarySearchTree Node object to the left node
        pre: node of the BSTNode
        post: TypeError if node not of the BSTNode class
        return: 
        """
        if not isinstance(node, BSTNode) and node is not None:
            raise TypeError("Input must be a BSTNode object or None")
        self._left = node

    @property
    def right(self):
        """ Property method which gives a right pointer for this node
        pre:
        post:
        return: right - the right pointer value of this node
        """
        return self._right
    
    @right.setter
    def right(self, node):
        """ Setter method is to set data of the BinarySearchTree Node object to the right node
        pre: node of the BSTNode
        post: TypeError if node not of the BSTNode class
        return: 
        """
        if not isinstance(node, BSTNode) and node is not None:
            raise TypeError("Input must be a BSTNode object or None")
        self._right = node
    
