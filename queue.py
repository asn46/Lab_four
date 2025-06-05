""" New Code added on line 126
    isQueueEmpty function was added because we cannot call isListEmpty directly and need this function for
    breadth first traversal in the BinarySearchTree class
"""

"""
Lab 4
Aseem Nerlekar, Gaurav Purushothaman
This assignment is to demonstrate implemention of Binary Search Trees and all its functionalities
"""


from currency import Currency
from singlylinkedlist import SinglyLinkedList

class Queue(SinglyLinkedList):
    def __init__(self):
        super().__init__()

    def __del__(self):
        """ Destructor method to delete queue entirely
        pre: 
        post: the queue makes itself empty
        return: 
        """
        self.emptyQueue()
    
    def enqueue(self, currency_obj):
        """ Adds object to the end of the queue
        pre: currency_obj - Currency object that we are adding to the end of the queue
        post: if the currency_object is not of the class Currency - give TypeError
        return: 
        """
        if not isinstance(currency_obj, Currency):
            raise TypeError("Input must be a Currency object")
        super().addCurrency(currency_obj, self.count)

    def dequeue(self):
        """Removes the Currency object at the front of the queue and returns it
        pre: 
        post: if queue is empty(has no start) - give IndexError
        return: deq_item - the value of the LinkNode's data attribute; it should be a Currency object
        """
        if self.start is None:
            raise IndexError("Queue is Empty")
        deq_item = self.start.data
        self.start = self.start.next
        if self.start is None:
            self.end is None
        return deq_item
    
    def peekFront(self):
        """Finds and returns a copy of the Currency object at the front of the queue
        post: if the queue is empty - give IndexError
        return: returns a copy of the Currency object at the front of the queue
        """
        if super().isListEmpty():
            raise IndexError("Stack is empty")
        return super().getCurrency(0).copy()

    def peekRear(self):
        """ Finds and returns a copy of the Currency object at the end of the queue
        pre: 
        post: if the list is empty - give IndexError
        return: returns a copy of the Currency object at the end of the queue
        """
        if super().isListEmpty():
            raise IndexError("Stack is empty")
        return super().getCurrency(self.count-1).copy()

    def stringifyQueue(self):
        """ Gives the queue's contents as a string
        pre: 
        post: 
        return: returns a string version of the queue's contents
        """
        return super().stringifyList()

    def emptyQueue(self):
        """ Makes the queue empty
        pre: 
        post: queue start and end pointers set to None, queue count value set to 0
        return: 
        """
        super().emptyList()

    def isQueueEmpty(self):
        """Shows whether the queue object is empty or not
        pre: 
        post:
        return: boolean value - True if queue is empty, otherwise False
        """
        return super().isListEmpty()

    def addCurrency(self, currency_obj, node_idx):
        """ addCurrency method in this class is not supposed to be run, so it gives NotImplemented Error
        pre: currency_obj which is a Currency object and node_idx, the index of the node
        post: Instantaneously gives a NotImplementedError
        return: 
        """
        raise NotImplementedError("Cannot call parent method directly")
    
    def removeCurrency(self, currency_obj):
        """ removeCurrency method in this class is not supposed to be run, so it gives NotImplemented Error
        pre: currency_obj which is a Currency object
        post: Instantaneously gives a NotImplementedError
        return: 
        """
        raise NotImplementedError("Cannot call parent method directly")
    
    def findCurrency(self, currency_obj):
        """ removeCurrency method in this class is not supposed to be run, so it gives NotImplemented Error
        pre: currency_obj which is a Currency object
        post: Instantaneously gives a NotImplementedError
        return: 
        """
        raise NotImplementedError("Cannot call parent method directly")
    
    def getCurrency(self, node_idx):
        """ getCurrency method in this class is not supposed to be run, so it gives NotImplemented Error
        pre: node_idx is the index of the node
        post: Instantaneously gives a NotImplementedError
        return: 
        """
        raise NotImplementedError("Cannot call parent method directly")
    
    def stringifyList(self):
        """ stringifyList method in this class is not supposed to be run, so it gives NotImplemented Error
        pre: 
        post: Instantaneously gives a NotImplementedError
        return: 
        """
        raise NotImplementedError("Cannot call parent method directly")
    
    def isListEmpty(self):
        """ isListEmpty method in this class is not supposed to be run, so it gives NotImplemented Error
        pre: 
        post: Instantaneously gives a NotImplementedError
        return: 
        """
        raise NotImplementedError("Cannot call parent method directly")
    
    def countCurrency(self):
        """ countCurrency method in this class is not supposed to be run, so it gives NotImplemented Error
        pre:
        post: Instantaneously gives a NotImplementedError
        return: 
        """
        raise NotImplementedError("Cannot call parent method directly")
    
    def emptyList(self):
        """ emptyList method in this class is not supposed to be run, so it gives NotImplemented Error
        pre: 
        post: Instantaneously gives a NotImplementedError
        return: 
        """
        raise NotImplementedError("Cannot call parent method directly")
    

    
