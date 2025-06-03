"""
LAB 3
Aseem Nerlekar, Gaurav Purushothaman
This assignment is to demonstrate implemention of link-based List and derivative ADTs of Stack and Queue
"""
from currency import Currency
class Drachma(Currency):

    def __init__(self, value_in=0.0):
        super().__init__(value_in)
        self._name = "Drachma"

    def getName(self):
        """Getter method to return the name of the currency. Overrides the base class method
        
        pre:
        post:
        return: string name of the currency
        """
        return self._name
    
    def copy(self):
        """Method to return a copy of the current object. Overrides the base class method

        pre:
        post
        return: Drachma object with the same value as the current object
        """
        return Drachma(self._whole + self._fractional / 100.0)