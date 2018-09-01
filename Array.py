import array

def newArray(ar_type):
    arr = array.array(ar_type, [])
    print ("New Array created")
    
def append(val):
    arr.append(val)
    print ("Value Added : ", val)
    
def insert(pos,val):
    arr.insert(pos,val)
    print ("Value ",val," Added at ",pos)

def pop():
    print ("Last value removed : ",arr.pop() if len(arr)!=0 else "Array is empty")
    
def remove(val):
        print ("Value", val, "Removed." if val in arr else val, "not present in array.")
    
def index(val):
        print (arr.index(val) if val in arr else val,"not present in Array")

def reverse():
    arr.reverse()
    print ("Array has been reversed.")
    
def display():
    if len(arr) != 0:
        print ("Array -> ", end = " ")
        for i in range (len(arr)):
            print (arr[i], end=" ")
    else:
        print ("Array is empty.")


