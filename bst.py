from bstnode import BSTNode

class BinarySearchTree():
    def __init__(self, root=None):
        self.root = root


    def search(self, data):
        current_node = self.root
        while current_node is not None:        
            if current_node.data == data:
                return current_node
            elif data < current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right
        
        return None
    

    def insert_node(self, node):
        if self.root is None:
            self.root = node
        else:
            current_node = self.root
            # does not account for duplicates
            while current_node is not None:
                if (node.get_Value() >  current_node.get_Value()):
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
        return self.search(data) is not None
    

    def insert(self, data):
        if self.contains(data):
            return False
        new_node = BSTNode(data)
        self.insert_node(new_node)
        return True
    

    def remove(self, data):
        parent = None
        current_node = self.root
        while current_node is not None:
            if current_node.data == data:
                
                # Case: No children
                if current_node.left is None and current_node.right is None:
                    if parent is None: 
                        self.root = None
                    elif parent.left == current_node:
                        parent.left = None
                    else: 
                        parent.right = None
                    return True
                
                # Case: Node with only left child
                elif current_node.right is None:
                    if parent is None: 
                        self.root = current_node.left
                    elif parent.left == current_node:
                        parent.left == current_node.left
                    else: 
                        parent.right = current_node.left
                    return True 

                # Case: Node with only right child
                elif current_node.left is None:
                    if parent is None: #Node is root
                        self.root = current_node.right
                    elif parent.left == current_node:
                        parent.left == current_node.right
                    else: 
                        parent.right = current_node.right
                    return True

                # Case: Node with 2 children
                else:   
                    successor = current_node.right
                    while successor.left is not None:
                        successor = successor.left
                    current_node.data = successor.data
                    parent = current_node
                    current_node = current_node.right
                    data = successor.data
            
            elif data > current_node.data:
                parent = current_node
                current_node = current_node.right
            
            else: 
                parent = current_node
                current_node = current_node.left
        
        return False 
    

    def print(self):
        pass


    def count(self):
        pass


    def is_empty(self):
        pass


    def empty_tree(self):
        pass

    def reverse_breadth_first_traverse(self, current_node):
        list = []
        if current_node.left is not None:
            list = list + self.reverse_breadth_first_traverse(current_node.left)
        if current_node.right is not None:
            list = list + self.reverse_breadth_first_traverse(current_node.right)
        list.append(current_node.data.get_Value())
        return list

        


    def breadth_first_traverse(self, current_node, output_object): # This is reversed version of postorder
        total = self.reverse_breadth_first_traverse(current_node)
        for i in range(len(total)):
            print(str(total[len(total)-i-1]) + ", ", end='')

        
    



    def inorder_traverse(self, current_node, output_object):

        if current_node.left is not None:
            self.inorder_traverse(current_node.left, output_object)
        print(str(current_node.data.get_Value()) + ", ", end='')
        output_object.write(str(current_node.data.get_Value()) + ", ")
        if current_node.right is not None:
            self.inorder_traverse(current_node.right, output_object)


    
    def preorder_traverse(self, current_node, output_object):
        print(str(current_node.data.get_Value()) + ", ", end='')
        output_object.write(str(current_node.data.get_Value()) + ", ")
        if current_node.left is not None:
            self.preorder_traverse(current_node.left, output_object)
        if current_node.right is not None:
            self.preorder_traverse(current_node.right, output_object)


    def postorder_traverse(self, current_node, output_object):
        if current_node.left is not None:
            self.postorder_traverse(current_node.left, output_object)
        if current_node.right is not None:
            self.postorder_traverse(current_node.right, output_object)
        print(str(current_node.data.get_Value()) + ", ", end='')
        output_object.write(str(current_node.data.get_Value()) + ", ")
