""""
LAB 3
Aseem Nerlekar, Gaurav Purushothaman
This assignment is to demonstrate implemention of link-based List and derivative ADTs of Stack and Queue
"""
from currency import Currency

class LinkNode:
    def __init__(self, currency_object):
        self._data = currency_object
        self._next = None

    @property
    def data(self):
        """ Property method which gives data of the LinkNode object
        pre: 
        post: 
        return: data - a pointer to a Currency object
        """
        return self._data
    
    @data.setter
    def data(self, currency_object):
        """ Setter method to set data of the LinkNode object to the currency_object
        pre: currency_object of the Currency class
        post: TypeError if currency_object not of the Currency class
        return: 
        """
        if not isinstance(currency_object, Currency):
            raise TypeError("Input must be a Currency object")
        self._data = currency_object
    
    @property
    def next(self):
        """ Property method which gives the next attribute of the LinkNode object
        pre: 
        post: 
        return: next - a pointer to another LinkNode object
        """
        return self._next
    
    @next.setter
    def next(self, node):
        """ Setter method to set the next attribute to point to another LinkNode object
        pre: node - LinkNode object that we want to point to using next
        post: TypeError if node is not a LinkNode object and is not None
        return:
        """
        if not isinstance(node, LinkNode) and node is not None:
            raise TypeError("Input must be a LinkNode object or None")
        self._next = node
