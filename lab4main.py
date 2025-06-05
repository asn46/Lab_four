"""
Lab 4
Aseem Nerlekar, Gaurav Purushothaman
This assignment is to demonstrate implemention of Binary Search Trees and all its functionalities
"""

from bst import BinarySearchTree
from bstnode import BSTNode
from currency import Currency
from drachma import Drachma
from singlylinkedlist import SinglyLinkedList
from queue import Queue

def main():
    print("Welcome to our Lab 4 demonstration -  Gaurav Purushothaman and Aseem Nerlekar")
    currencies = [
        Drachma(57.12),
        Drachma(23.44),
        Drachma(87.43),
        Drachma(68.99),
        Drachma(111.22),
        Drachma(44.55),
        Drachma(77.77),
        Drachma(18.36),
        Drachma(543.21),
        Drachma(20.21),
        Drachma(345.67),
        Drachma(36.18),
        Drachma(48.48),
        Drachma(101.00),
        Drachma(11.00),
        Drachma(21.00),
        Drachma(51.00),
        Drachma(1.00),
        Drachma(251.00),
        Drachma(151.00),
    ]
    bst = BinarySearchTree()
    for i in currencies:
        bst.insert(i)


    output_object = open('output.txt', 'w')

    print_traversal(bst, output_object)
    choice = ""
    while(choice != "q"):
        valid = True
        choice = input("Choose one of the following actions a - add node, s - search node, d - delete node, t - traverse tree, q - quit -> ")
        if(choice == "a"):
            value = 0
            try:
                value = float(input("Enter a value of amount of Drachma you want to add -> "))
            except(ValueError):
                print("Invalid data")
                valid = False
                output_object.write("Invalid data")
            if(valid):
                result = bst.insert(Drachma(value))
                if not result:
                    print("Invalid - duplicate data")
                    output_object.write("Invalid - duplicate data")
        elif(choice =="s"):
            value = 0
            try:
                value = float(input("Enter a value for the node you want to search -> "))
            except(ValueError):
                print("Invalid data")
                valid = False
                output_object.write("Invalid data")
            if(valid):
                data = Drachma(value)
                if(bst.search(data)!=None):
                    print("This node is found")
                else:
                    print("This node is not found")
        elif(choice == "d"):
            value = 0
            try:
                value = float(input("Enter a value of amount of Drachma you want to delete -> "))
            except(ValueError):
                print("Invalid data")
                valid = False
                output_object.write("Invalid data")
            if(valid):
                data = Drachma(value)
                if(not(bst.delete(data))):
                    print("Invalid value")
                    output_object.write("Invalid value")
        elif(choice == "t"):
            print_traversal(bst, output_object)
        
        elif(choice != "q"):
            print("Enter a valid action")
        


    print_traversal(bst, output_object)


    output_object.close()



def print_traversal(bst, output_object):
    """Method to print out all of the different types of traversals
        pre: 
        bst - the binary search tree object
        output_object - the txt file object to write
        post:
        prints out all of the different traversals for the binary tree
        return:
    """
    output_object.write("Breadth-first traverse : ")
    print("Breadth-first traverse : ", end='')
    bst.breadth_first_traverse(output_object)
    

    output_object.write("\nIn-order traverse : ")
    print("\nIn-order traverse : ", end='')
    bst.inorder_traverse(bst.root, output_object)


    output_object.write("\nPre-order traverse : ")
    print("\nPre-order traverse : ", end='')
    bst.preorder_traverse(bst.root, output_object)


    output_object.write("\nPost-order traverse : ")
    print("\nPost-order traverse : ", end='')
    bst.postorder_traverse(bst.root, output_object)

    print()
    output_object.write("\n")



    
        
        

if __name__ == "__main__":
    main()
