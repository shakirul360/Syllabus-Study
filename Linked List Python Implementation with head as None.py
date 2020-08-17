#By Shakirul Islam Leeon
#git - Shakirul360

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0   
        
#Append function adds checks if the list is empty and adds data to the list however needed.    
    def append(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = Node(data)
        self.count += 1
            
#Size function returns the size of the list  
    def size(self):
        return self.count
    
#insert_at_beginning function adds a node at the start of the list and calls it head of the list    
    def insert_at_beginning(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        self.count += 1
            
#get_array_from_list returns an array created from the data values of the list    
    def get_array_from_list(self):
        if self.count == 0:
            print("No data in list to extract into an array")
        else:
            arr = []
            current_node = self.head
            while current_node:
                arr.append(current_node.data)
                current_node = current_node.next
            return arr
        
#display function prints the data values of the nodes in the list     
    def display(self):
        if self.count == 0:
            print("No data to display")
        else:
            cur = self.head
            while cur:
                print(cur.data, end = ' ')
                cur = cur.next
                
#is_empty function checks if the list is empty and replies accordingly    
    def is_empty(self):
        if self.count == 0:
            return True
        return False
    
# remove function removes a node from the list, given the value to be removed.    
    def remove(self, data):
        if self.count == 0:
            print("No data in list to remove")
        else:
            cur = self.head.next
            prev = self.head
            while prev.data != data and cur.next != None:
                prev = cur
                cur = cur.next
            prev.next = cur.next
            self.count -= 1
    
#pop function removes the last item on the list
    def remove_last(self):
        if self.count == 0:
            print("No Items to remove")
        else:
            current_node = self.head
            while current_node.next:
                if current_node.next.next == None:
                    current_node.next = None
                else:
                    current_node = current_node.next
    
    def remove_first(self):
        if self.count ==0:
            print("No Items to remove")
        else:
            cur = self.head
            self.head = cur.next
        
l = LinkedList()
n = 5
for _ in range(n):
    l.append(input())

l.size()
