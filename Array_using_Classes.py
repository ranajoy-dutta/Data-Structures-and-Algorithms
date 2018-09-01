import array

class myArray:
    def newArray(self, ar_type):
        self.arr = array.array(ar_type, [])
        print ("New Array created")
        
    def append(self,val):
        self.arr.append(val)
        print ("Value Added : ", val)
        
    def insert(self,pos,val):
        self.arr.insert(pos,val)
        print ("Value ",val," Added at ",pos)

    def pop(self):
        print ("Last value removed : ",self.arr.pop() if len(self.arr)!=0 else "Array is empty")
        
    def remove(self, val):
            print ("Value", val, "Removed." if val in self.arr else val, "not present in array.")
        
    def index(self, val):
            print (self.arr.index(val) if val in self.arr else val,"not present in Array")

    def reverse(self):
        self.arr.reverse()
        print ("Array has been reversed.")
        
    def display(self):
        arr=self.arr
        if len(arr) != 0:
            print ("Array -> ", end = " ")
            for i in range (len(arr)):
                print (arr[i], end=" ")
        else:
            print ("Array is empty.")


