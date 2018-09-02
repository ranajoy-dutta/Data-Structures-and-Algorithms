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
        cur = self.head         # initialising current node to head node
        while cur.next != None: # check for last node
            cur = cur.next      # pointing to next node
        cur.next = new_node     # setting last node pointer to new node
         
    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1          # Counter
            cur = cur.next
        return total

    def display(self):
        elements = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            elements.append(cur.data)   # storing the node data in a list
        return elements

    def get(self, index):
        if index >= self.length(): return "ERROR : index out of range!"
        idx = 0
        cur = self.head
        while cur.next != None:
            cur = cur.next
            if idx == index: return cur.data
            idx += 1

    def delete(self, index):
        if index >= self.length(): return "ERROR : index out of range!"
        idx = 0
        cur_node = self.head
        while cur.next != None:
            last_node = cur_node
            cur_node = cur.next
            if idx == index:
                last_node.next = cur_node.next
                return "Node Deleted"
            idx += 1
            




#--- main ---
mylist = linked_list()
while True:
       print ("SINGLY LINKED LIST OPERATIONS")
       print ("1. Add")
       print ("2. Length")
       print ("3. Get")
       print ("4. Traverse")
       print ("5. Delete")
       print ("6. Exit")
       ch=int(input("\nEnter your choice :: "))
       if ch==1:
              data=input("Enter Data :")
              mylist.append(data)
              print("*** New Node Added ***")
       elif ch==2:
              length = mylist.length()
              print ("*** Length =  ",length," ***")
       elif ch==3:
              index = int(input("Enter Index : "))
              print ("*** Output =  ",mylist.get(index)," ***")
       elif ch==4:
              nodes=mylist.display()
              print("Linked List - > " , end="")
              for node in nodes:
                  print(node,end=", ")
       elif ch==5:
              index = int(input("Enter Index : "))
              print ("*** Output =  ",mylist.delete(index)," ***")
       elif ch==6:
              break
       else:
              print ("\tInvalid Choice!!!")
       print("\n","="*50,"\n")
       



    
