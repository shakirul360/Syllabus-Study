#By Shakirul Islam Leeon
#git - Shakirul360

class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = Node()
        self.count = 0
       ## The above line creates an empty node and sets it as head
    
    #The insert Method first creates a node, and then traverses across the list till it finds None and then attaches the new node.
    def insert(self,data):
        new_node = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
        self.count += 1
        
    #size method returns the size of the linked list
    def size(self):
        return self.count
    
    #get_array_from_list method returns the linked list as an array
    def get_array_from_list(self):
        arr = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            arr.append(cur.data)
        return arr
    
    #display method prints out the values in the linked list
    def display(self):
        cur = self.head
        while cur.next != None:
            cur = cur.next
            print(cur.data,end = ' ')
    
    def is_empty(self):
        if self.count == 0:
            return True
        else:
            return False
    
    def insert_at_beginning(self,data):
        cur = self.head
        next_node = cur.next
        new_node = Node(data)
        new_node.next = next_node
        cur.next = new_node
    
#Get function basically helps us check the value using an index position. It does not remove the value from the Linked List    
    def get(self,index):
        if index >= self.size() or index < 0: # added 'index<0' post-video
            print("ERROR: 'Get' Index out of range!")
            return None
        cur_idx = 0
        cur = self.head
        while True:
            cur = cur.next
            if cur_idx == index: return cur.data
            cur_idx += 1
#Remove function starts from the start and traverses till it finds a node which has the same data as the input, and then removes it accordingly.    
    
    def remove(self,data):
        cur = self.head
        while cur.next.data != data:
            cur = cur.next
        next_node = cur.next
        next2 = next_node.next
        cur.next = next2
        self.count -= 1
        
l = LinkedList()
#n = int(input())
#for _ in range(n):
    #l.insert(int(input()))
#print(l.get_array_from_list())
#print(l.size())
#l.display()
l.is_empty()
