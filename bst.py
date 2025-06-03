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
                if node.data < current_node.data:
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
        self.insert_node(BSTNode)
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


    def breadth_first_traverse(self):
        current_node = self.root
        #create Queue here
        while current_node is not None:
            # process current_node here
            if current_node.left is not None:
                # enqueue left subtree here
                pass
            if current_node.right is not None:
                # enqueue right subtree here
                pass
            # if not queue isEmpty:
                # current_node =  Queue.dequeue
            # else:
                # current_node = None
    
        # destroy Queue here



    def inorder_traverse(self, current_node):
        if current_node is None:
            return
        self.inorder_traverse(current_node.left)
        # process current_node here
        self.inorder_traverse(current_node.right)

    
    def preorder_traverse(self, current_node):
        if current_node is None:
            return
        # process current_node here
        self.preorder_traverse(current_node.left)
        self.preorder_traverse(current_node.right)


    def postorder_traverse(self, current_node):
        if current_node is None:
            return
        self.postorder_traverse(current_node.left)
        self.postorder_traverse(current_node.right)
        # process current_node here

