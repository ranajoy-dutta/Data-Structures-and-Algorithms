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


#--- main ---

mylist = linked_list()
while True:
       print ("SINGLY LINKED LIST OPERATIONS")
       print ("1. Add")
       print ("2. Length")
       print ("3. Traverse")
       print ("4. Exit")
       ch=int(input("\nEnter your choice :: "))
       if ch==1:
              data=input("Enter Data :")
              mylist.append(data)
              print("*** New Node Added ***")
       elif ch==2:
              length = mylist.length()
              print ("*** Length =  ",length," ***")
       elif ch==3:
              nodes=mylist.display()
              print("Linked List - > " , end="")
              for node in nodes:
                  print(node,end=", ")
       elif ch==4:
              break
       else:
              print ("\tInvalid Choice!!!")
       print("\n","="*50,"\n")
       



    
