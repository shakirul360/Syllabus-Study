class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self, value):
        if self.value == value:
            return
        if self.value > value:
            if self.left:
                return self.left.insert(value)
            else:
                self.left = Node(value)
        if self.value < value:
            if self.right:
                return self.right.insert(value)
            else:
                self.right = Node(value)
    
    def find(self, value):
        if self.value == value: #check to see if the current node's value matches the search value. NOTE - initiation self == root.
            found = True
        elif self.value < value: #if the value is greater, check the right side of the tree if right side is there.
            if self.right:
                return self.right.find(value)
            else:
                found = False
        else:
            if self.left: #if the value is less, check the left side of the tree if left side is there.
                return self.left.find(value)
            else:
                Found = True        
        if found:
            print("Value {} in the tree".format(value))
        else:
            print("value {} not in the tree".format(value))
            
    def pre_order(self):
        if self and self != None:
            print(self.value)
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()
            
    def in_order(self):
        if self:
            if self.left:
                self.left.in_order()
            if self != None:
                print(self.value)
            if self.right:
                self.right.in_order()
            
    def post_order(self):
        if self:
            if self.left:
                self.left.post_order()
            if self.right:
                self.right.post_order()
        if self != None:
            print(self.value)
            
    def delete(self, value):
        if self.value == value: #matches the node's value and then checks to see if it has both left or right, one of them or none.
            if not self.left and not self.right:        #if it has no nodes connected to it
                self.value = None
    
class Tree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            return self.root.insert(value)
        
    def find(self, value):
        if self.root == None:
            print("No tree to find values on")
        else:
            return self.root.find(value)
    
    def pre_order(self):
        print("1....2...3...Pre Order Traversal initiated")
        self.root.pre_order()
    
    def in_order(self):
        print("1....2...3...In Order Traversal initiated")
        self.root.in_order()
    
    def post_order(self):
        print("1....2...3...Post Order Traversal initiated")
        self.root.post_order()
    
    def delete(self, value):
        if self.root:
            if self.root.value == value:     # if the delete value is at the root.
                if not self.root.left and not self.root.right:
                    self.root.value = None
                elif self.root.left and not self.root.right:
                    self.root = self.root.left
                elif not self.root.left and self.root.right:
                    self.root = self.root.right
                
                elif self.root.left and self.root.right:
                    delNodeParent = self.root
                    delNode = self.root.right
                    while delNode.left:
                        delNodeParent = delNode
                        delNode = delNode.left
                    
                    self.root.value = delNode.value
                    if delNode.right:
                        if delNodeParent.value > delNode.value:
                            delNodeParent.left = delNode.right
                        elif delNodeParent.value < delNode.value:
                            delNodeParent.right = delNode.right
                        else:
                            if delNode.value < delNodeParent.value:
                                delNodeParent.left = None
                            else:
                                delNodeParent.right = None
                
            else:
                if self.root.value < value:
                    delnode = self.root.right
                    delnodeparent = self.root
                if self.root.value > value:
                    delnode = self.root.left
                    delnodeparent = self.root
                    
                    while delnode.value != value:
                        if delnode.value > value:
                            delnode = delnode.left
                            delnodeparent = delnode
                        else:
                            delnode = delnode.right
                            delnodeparent = delnode
                    
                    if not delnode.left and not delnode.right:
                        if delnodeparent.value > delnode.value:
                            delnodeparent.left = None
                        else:
                            delnodeparent.right = None
        
                    elif delnode.left and not delnode.right:
                        if value < delnodeparent.value:
                            delnodeparent.left = delnode.left
                        else:
                            delnodeparent.right = delnode.left
                    
                    elif not delnode.left and delnode.right:
                        if data < parent.value:
                            parent.left = node.right
                        else:
                            parent.right = node.right
                        
                    else: #if both left and right children
                        node = delnode #keeping a copy of the node to be replaced
                        while delnode.left:
                            delnodeparent = delnode
                            delnode = delnode.left
                        node.value - delnode.value
                        if delnode.right:
                            if delnodeparent.value > delnode.value:
                                delnodeparent.left = delnode.right
                            elif delnodeparent.value < delnode.value:
                                delnodeparent.right = delnode.right
                        else:
                            if delnode.value < delnodeparent.value:
                                delnodeparent.left = None
                            else:
                                delnodeparent.right = None                
                    
        else:
            print("no tree to remove value from")

            
        
t = Tree()
t.insert(50)
t.insert(30)
t.insert(70)
t.insert(20)
t.insert(40)
t.insert(60)
t.insert(80)
print("PRE DELETE")
print(" ")
t.in_order()
print(" ")
t.pre_order()
print(" ")
t.post_order()
print(" ")

t.delete(50)
t.in_order()
print("POST delete of 50, the root")
t.insert(50)
t.delete(70)
t.in_order()
print("POST delete of 70, a node with both left and right childs")
t.insert(10)
t.delete(10)
t.post_order()
