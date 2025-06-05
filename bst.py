from bstnode import BSTNode
from queue import Queue

class BinarySearchTree():
    def __init__(self, root=None):
        self.root = root


    def search(self, in_data):
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
        return self.search(data) is not None
    

    def insert(self, data):
        if self.contains(data):
            return False
        new_node = BSTNode(data)
        self.insert_node(new_node)
        return True
    

    def delete(self, data):
        parent = None
        current_node = self.root
        while current_node is not None:
            if current_node.data.get_Value() == data.get_Value():
                
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
            
            elif data.get_Value() > current_node.data.get_Value():
                parent = current_node
                current_node = current_node.right
            
            else: 
                parent = current_node
                current_node = current_node.left
        
        return False 
    

    def print(self):
        return self.inorder_traverse(self.root)


    def count(self):
        return self._recursive_count(self.root)
        

    def _recursive_count(self, node):
        if node is None:
            return 0
        else:
            return 1 + self._recursive_count(node.left) + self._recursive_count(node.right)


    def is_empty(self):
        return self.root is None


    def empty_tree(self):
        self.root = None

    def reverse_breadth_first_traverse(self, current_node):
        list = []
        if current_node.left is not None:
            list = list + self.reverse_breadth_first_traverse(current_node.left)
        if current_node.right is not None:
            list = list + self.reverse_breadth_first_traverse(current_node.right)
        list.append(current_node.data.get_Value())
        return list


    def breadth_first_traverse(self, output_object=None):        
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
        if current_node.left is not None:
            self.inorder_traverse(current_node.left, output_object)
        print(str(current_node.data.get_Value()) + ", ", end='')
        if output_object:
            output_object.write(str(current_node.data.get_Value()) + ", ")
        if current_node.right is not None:
            self.inorder_traverse(current_node.right, output_object)

    
    def preorder_traverse(self, current_node, output_object=None):
        print(str(current_node.data.get_Value()) + ", ", end='')
        if output_object:
            output_object.write(str(current_node.data.get_Value()) + ", ")
        if current_node.left is not None:
            self.preorder_traverse(current_node.left, output_object)
        if current_node.right is not None:
            self.preorder_traverse(current_node.right, output_object)


    def postorder_traverse(self, current_node, output_object=None):
        if current_node.left is not None:
            self.postorder_traverse(current_node.left, output_object)
        if current_node.right is not None:
            self.postorder_traverse(current_node.right, output_object)
        print(str(current_node.data.get_Value()) + ", ", end='')
        if output_object:
            output_object.write(str(current_node.data.get_Value()) + ", ")
