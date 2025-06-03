from drachma import Drachma

class BSTNode():
    def __init__(self, data=None, left=None, right=None):
        self._data = data
        self._left = left
        self._right = right

    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, drachma):
        if not isinstance(drachma, Drachma):
            raise TypeError("Input must be a Drachma object")
        self._data = drachma
    
    @property
    def left(self):
        return self._left
    
    @left.setter
    def left(self, node):
        if not isinstance(node, BSTNode) and node is not None:
            raise TypeError("Input must be a BSTNode object or None")
        self._left = node

    @property
    def right(self):
        return self._right
    
    @right.setter
    def right(self, node):
        if not isinstance(node, BSTNode) and node is not None:
            raise TypeError("Input must be a BSTNode object or None")
        self._right = node
    
