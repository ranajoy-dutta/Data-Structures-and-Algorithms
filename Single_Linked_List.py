""" Singly Linked - List """
class node:             
    def __init__(self, data=None):
        self.data = data
        self.next = None    


class linked_list:
    def __init__(self):
        self.head = node()      # head Node

    def append(self, data):
        new_node = node(data)   # New Node Data
        cur = self.head         # initialising cursor to head node
        while cur.next != None: # finding last node
            cur = cur.next
            
        cur.next = new_node     # setting last node pointer to new node
         
    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        elements = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            elements.append(cur.data)
        return elements

mylist = linked_list()
mylist.display()
    
