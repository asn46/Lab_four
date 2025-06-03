""" New Code added on line 108
    get_Value function was added because there was no other way of getting the 
    value of the currency object to display to the user.
"""

""""
LAB 3
Aseem Nerlekar, Gaurav Purushothaman
This assignment is to demonstrate implemention of link-based List and derivative ADTs of Stack and Queue
"""
from abc import ABC, abstractmethod


class Currency(ABC):
    def __init__(self,value_in=0.0):
        self._whole = 0
        self._fractional= 0
        if not isinstance(value_in, (int,float)):
            raise TypeError("Value must be an integer or float")
        if value_in < 0:
            raise ValueError("Value cannot be negative")
        whole_part = int(value_in)
        abs_fractional_float = value_in - whole_part
        fractional_part = int(round(abs_fractional_float * 100))
        self._whole = whole_part
        self._fractional = fractional_part

    @property
    def whole(self):
        """Getter method to return the whole part of the currency value

        pre: 
        post:
        return: integer of whole part of the currency value
        """
        return self._whole
    
    @whole.setter
    def whole(self, value):
        """Setter method to assign the whole part of the currency value

        pre: 
        post: TypeError if value is not an integer, ValueError if value is negative
        return: 
        """
        if not isinstance(value, int):
            raise TypeError("Whole part must be an integer.")
        if value < 0:
            raise ValueError("Whole part cannot be negative.")
        self._whole = value

    @whole.deleter
    def whole(self):
        raise AttributeError("Cannot delete this attribute. Try setting to 0 instead.")
    
    @property
    def fractional(self):
        """Getter method to return the fractional part of the currency value

        pre: 
        post:
        return: integer of fractional part of the currency value
        """
        return self._fractional

    @fractional.setter
    def fractional(self, value):
        """Setter method to assign the fractional part of the currency value

        pre: 
        post: TypeError if value is not an integer, ValueError if value is negative or greater than 99
        return: 
        """
        if not isinstance(value, int):
            raise TypeError("Fractional part must be an integer")
        if value < 0:
             raise ValueError("Fractional part cannot be negative")
        if value > 99:
            raise ValueError("Fractional part cannot be greater than 99")
        self._fractional = value
    
    @fractional.deleter
    def fractional(self):
        raise AttributeError("Cannot delete this attribute. Try setting to 0 instead.")

    @abstractmethod
    def getName(self):
        """Abstract method to return the name of the currency. To be implemented/overridden in derived classes.
        
        pre:
        post:
        return:
        """
        pass
    
    @abstractmethod
    def copy(self):
        """Abstract method to return a new derived Currency object with same attribute values as self. To be implemented/overridden in derived classes.
        
        pre:
        post:
        return:
        """
        pass

    
    def get_Value(self):      
        """ get_Value method gives the numberical value of the currency     #  NEW CODE
                                                                            #  NEW CODE
        pre:                                                                
        post:                                                               
        return: the numerical value of the currency                         
        """                                                                 
        return int(self._whole*100 + self._fractional)/100                  

    def isSameCurrency(self, other):
        """Method to check if two Currency objects are of the same type.
        
        pre: other - a derived Currency object
        post: TypeError if other is not a Currency object
        return: True if both objects are of the same type, False otherwise
        """
        if not isinstance(other, Currency):
            raise TypeError()
        return self.getName() == other.getName()

    def add(self, other):
        """Method to add two Currency objects of the same type.
        
        pre: other - a derived Currency object
        post: self _whole and _fractional increased by added value from other; TypeError if other is not a Currency object
        return: 
        """
        if not self.isSameCurrency(other):
            raise TypeError()
        new_whole = self._whole + other.whole
        new_fractional = self._fractional + other.fractional
        if new_fractional >= 100:
            new_whole += new_fractional // 100
            new_fractional = new_fractional % 100
        self._whole = new_whole
        self._fractional = new_fractional

    def subtract(self, other):
        """Method to subtract two Currency objects of the same type.
        
        pre: other - a derived Currency object
        post: self _whole and _fractional decreased by subtracted value from other; TypeError if other is not a Currency object, ValueError if self is less than other
        return:
        """
        if not self.isSameCurrency(other):
            raise TypeError()
        if self.isGreater(other):
            raise ValueError()
        new_whole = self._whole - other.whole
        new_fractional = self._fractional - other.fractional
        if new_fractional < 0:
            new_whole -= 1
            new_fractional += 100
        self._whole = new_whole
        self._fractional = new_fractional

    def isEqual(self, other):
        """Method to check if two Currency objects are equal.

        pre: other - a derived Currency object
        post: TypeError if other is not a Currency object
        return: True if both objects are equal, False otherwise
        """
        if not self.isSameCurrency(other):
            raise TypeError()
        if self._whole != other.whole or self._fractional != other.fractional:
            return False
        return True
        
    def isGreater(self, other):
        """Method to check if self is greater than other Currency object.
        
        pre: other - a derived Currency object
        post: TypeError if other is not a Currency object
        return: True if self is greater than other, False otherwise
        """
        if not self.isSameCurrency(other):
            raise TypeError()
        if other.whole > self._whole:
            return True
        elif other.whole == self._whole and other.fractional > self._fractional:
            return True
        return False

    def toString(self):
        """Method to return a string representation of the Currency object.
        
        pre:
        post:
        return: string representation of the Currency object
        """
        formatted_value = "{}.{:02d}".format(self._whole, self._fractional)
        return "{} {}".format(formatted_value, self.getName())

    def print(self):
        """Method to print the string representation of the Currency object.
        
        pre:
        post: prints the string representation of the Currency object into console
        return:
        """
        print(self.toString())
