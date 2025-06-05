"""
Lab 4
Aseem Nerlekar, Gaurav Purushothaman
This assignment is to demonstrate implemention of Binary Search Trees and all its functionalities
"""

from currency import Currency
from linknode import LinkNode

class SinglyLinkedList():
    def __init__(self):
        self._count = 0
        self._start = None
        self._end = None

    def __del__(self):
        """ Destructor method to delete list entirely
        pre: 
        post: the list makes itself empty; start and end pointers set to None, count value set to 0
        return: 
        """
        self.emptyList()
    
    @property
    def count(self):
        """ Getter method to return count value
        pre:
        post:
        return: integer value of the list object's count
        """
        return self._count
    
    @count.setter
    def count(self, value):
        """ Setter method to set count value
        pre:
        post: TypeError if count value is not integer
        return: 
        """
        if not isinstance(value, int):
            raise TypeError("Count must be an integer value")
        self._count = value

    @property
    def start(self):
        """ Getter method to return list object's start pointer
        pre:
        post:
        return: list object's start pointer - None or a LinkNode object
        """
        return self._start
    
    @start.setter
    def start(self, node):
        """ Setter method to set list object's start pointer
        pre: node - None or pointer to LinkNode object
        post:
        return:
        """
        self._start = node
    
    @property
    def end(self):
        """ Getter method to set list object's end pointer
        pre:
        post: 
        return: list object's end pointer - None or a LinkNode object
        """
        return self._end
    
    @end.setter
    def end(self, node):
        """ Setter method to set list object's end pointer
        pre: node - None or pointer to LinkNode object
        post:
        return:
        """
        self._end = node
    
    def _getNode(self, node_idx):
        """Traverse linked list object and return LinkNode object using index
        pre: node_idx - a node index integer
        post: TypeError if node_idx is not an integer; IndexError if node_idx is less than 0 or greater than or equal to linked list object's count
        return: LinkedNode object specified by node index parameter
        """
        if not isinstance(node_idx, int):
            raise TypeError("Param must be an integer (node index)")
        if node_idx < 0 or node_idx >= self.count:
            raise IndexError("Node index out of range")
        
        curr_node = self.start
        for _ in range(node_idx):
            curr_node = curr_node.next
        return curr_node
    
    def addCurrency(self, currency_obj, node_idx):
        """Allocate new LinkedNode object with currency_obj as data and add to the linked list
        pre: currency_obj - Currency object; node_idx - a node index integer
        post: TypeError if currency_obj is not of the Currency class or if node_idx is not an integer. IndexError if node_idx is less than 0 or greater than or equal to linked list object's count
        return:
        """
        if not isinstance(currency_obj, Currency):
            raise TypeError("Param 1 must be a Currency object")
        if not isinstance(node_idx, int):
            raise TypeError("Param 2 must be an integer (node index)")
        if node_idx < 0 or node_idx > self.count:
            raise IndexError("Node index out of range")
        
        new_node = LinkNode(currency_obj)
        
        if self.count == 0:
            self.start = new_node
            self.end = new_node
        elif node_idx == 0:
            new_node.next = self.start
            self.start = new_node
        elif node_idx == self.count:
            self.end.next = new_node
            self.end = new_node
        else:
            prev_node = self._getNode(node_idx - 1)
            new_node.next = prev_node.next
            prev_node.next = new_node
        self.count += 1

    def _removeNodeAfter(self, curr_node):
        """Helper method to remove node after the specified node from linked list
        pre: curr_node - LinkNode object
        post: node after curr_node removed from linked list
        return:
        """
        if curr_node is None:
            succ_node = self.start.next
            self.start = succ_node
        
            if succ_node is None:
                self.end = None

        elif curr_node is not None:
            succ_node = curr_node.next.next
            curr_node.next = succ_node

            if succ_node is None:
                self.end = curr_node

    def _removeByCurrencyObj(self, curr_obj):
        """Helper method to remove currency object from the linked list via input of a currency object and return a copy of the object
        pre: curr_obj - Currency object
        post: curr_obj removed from linked list
        return: a Currency copy of curr_obj if curr obj is found or -1 if not found
        """
        previous = None
        current = self.start
        while current is not None:
            if current.data.isEqual(curr_obj):
                current_copy = current.data.copy()
                self._removeNodeAfter(previous)
                self.count -= 1
                return current_copy
            previous = current
            current = current.next
        
        return -1

    def _removeByNodeIdx(self, index):
        """Helper method to remove a currency object from the linked list via input of an index of the node that holds the object and return a copy of the object
        pre: index - integer node index
        post: currency object removed from linked list
        return: returns a Currency copy of curr_obj if curr obj is found or -1 if not found
        """
        if index < 0 or index >= self.count:
            raise IndexError("Index out of bounds")
        current = self.start
        previous = None
        count = 0

        while current is not None:
            if count == index:
                current_copy = current.data.copy()
                self._removeNodeAfter(previous)
                self.count -= 1
                return current_copy
            previous = current
            current = current.next
            count += 1
        
        return -1
    
    def removeCurrency(self, param):
        """Main remove currency method to remove currency object from linked list and return a copy; this method diverts to the appropriate helper method depending on type of param
        pre: param - either an integer node index or a Currency object
        post: curr_obj removed from linked list; TypeError if param is neither an integer nor a Currency object
        return: returns a Currency copy of the currency object removed from list or -1 if not found
        """
        if isinstance(param, Currency):
            removed_currency = self._removeByCurrencyObj(param)
        elif isinstance(param, int):
            removed_currency = self._removeByNodeIdx(param)
        else:
            raise TypeError("Input must be Currency object or int (node index)")
        return removed_currency

    def findCurrency(self, currency_obj):
        """Returns the node index at which the currency object is found in the list based on the input currency object
        pre: currency_obj - Currency object
        post: TypeError if currency_obj is not a Currency object
        return: returns index of currency object if found, otherwise returns -1
        """
        if not isinstance(currency_obj, Currency):
            raise TypeError("Input must be a Currency object")
        curr_node = self.start
        index = 0
        while curr_node is not None:
            if(curr_node.data.get_Value() == currency_obj.get_Value()):
                return index
            curr_node=curr_node.next
            index+=1
            
        return -1
    
    def getCurrency(self, node_idx):
        """Takes an index as a parameter and returns the Currency object at the node specified by the index
        pre: node_idx - integer node index
        post: TypeError if node_idx is not an integer
        return: data of the node at given node index - a Currency object
        """
        if not isinstance(node_idx, int):
            raise TypeError("Input must be an integer")
        curr_node = self.start
        for i in range(node_idx):
            curr_node = curr_node.next
        return curr_node.data

    def stringifyList(self):
        """Create and return a string containing the contents of the linked list
        pre:
        post:
        return: string version of the linked list contents
        """
        curr_node = self.start
        result = ""
        while curr_node is not None:
            result += str(curr_node.data.get_Value()) + "\t"
            curr_node = curr_node.next
        return result
    
    def isListEmpty(self):
        """Check if linked list is empty
        pre:
        post:
        return: boolean value - True if list is empty (start is None), otherwise False
        """
        return self.start is None
    
    def countCurrency(self):
        """Get count of Currency nodes in list
        pre:
        post:
        return: count integer value of the linked list object
        """
        return self.count
    
    def emptyList(self):
        """Method to empty the linked list; removes references to nodes by setting start to None, so they will be garbage collected
        pre:
        post: linked list is emptied
        return:
        """
        self.start = None
        self.end = None
        self.count = 0
