def isempty(que):
       if que==[]:
              return True
       else:
              return False

def enqueue(que, item):
       que.append(item)
       front=que[0]

def dequeue(que):
       if isempty(que):
              return "underflow"
       else :
              item=que.pop(0)
              if len(que)==0:
                     front=None
              else:
                     front=que[0]
       return item

def Peek(que):
       if isempty(que):
              return "underflow"
       else:
              front=que[0]
              rear=que[len(que)-1]
              return front,rear

#--- main ---
queue=[]
top=None
while True:
       print ("QUEUE OPERATIONS")
       print ("1. Enqueue")
       print ("2. Dequeue")
       print ("3. Peek")
       print ("4. Exit")
       ch=int(input("\nEnter your choice :: "))
       if ch==1:
              item=int(input("Enter Item :"))
              enqueue(queue,item)
              print("*** Element Inserted ***")
       elif ch==2:
              item=dequeue(queue)
              if item=="underflow":
                     print ("*** Underflow! Stack is empty ***")
              else:
                     print ("*** Dequeued item is ",item," ***")
       elif ch==3:
              item=Peek(queue)
              if item=="underflow":
                     print ("*** Underflow! queue is empty ***")
              else:
                     print ("*** Item at front is",item[0]," ***")
                     print ("*** Item at rear is",item[1]," ***")
       elif ch==4:
              break
       else:
              print ("\tInvalid Choice!!!")
       print("="*50,"\n")
       
