class Node:
    def __init__(self, value):
        self.value = value
        self.leaf = True
        self.left = None
        self.right = None
    
    def insert(self, value):
        if self.value == value:
            return
        elif self.value > value:
            if self.left:
                return self.left.insert(value)
            else:
                self.left = Node(value)
        else:
            if self.right:
                return self.right.insert(value)
            else:
                self.right = Node(value)
    
    def find(self, value):
        if self.value == value:
            found = True
        elif self.value == None:
            found = False
        elif self.value < value:
            if self.right:
                return self.right.find(value)
            else:
                found = False
        else:
            if self.left:
                return self.left.find(value)
            else:
                found = True     
        if found:
            print("The data value, {}, is in the tree".format(value))
        else:
            print("The data value, {}, is not in the tree".format(value))
        
    def remove(self, value):
        if self.value == value:

            if self.right and self.left:
                left_child = self.left
                right_child = self.right
                cur = self.right
                while cur.left != None:
                    cur = self.left
                self.value = cur.value
                self.right = right_child
                self.left = left_child    
            elif self.right:
                cur = self.right
                self.value = cur.value
            elif self.left:
                cur = self.left
                self.value = cur.left
            else:
                self.value = None
        elif self.value == None:
            return
        elif self.value < value:
            return self.right.remove(value)
        elif self.value > value:
            return self.left.remove(value)
        
        
class Graph:
    def __init__(self):
        self.root = None
        self.arr = []
    
    def insert(self, value):
        if self.root:
            return self.root.insert(value)
        else:
            self.root = Node(value)

    def find(self, value):
        if self.root:
            return self.root.find( value)
        else:
            print("No data in tree to check")
    
    def remove(self, value):
        if self.root:
            return self.root.remove(value)
        else:
            print("No data to remove from")
            
g = Graph()
g.insert(20)
g.insert(30)
g.insert(23)
g.insert(33)
g.insert(10)

g.find(30)
g.remove(30)
g.find(30)
g.find(10)
g.remove(10)
g.find(10)
g.find(23)
g.remove(23)
g.find(23)
#g.find(60)
#g.find(50)
#g.find(40)
#g.find(70)
