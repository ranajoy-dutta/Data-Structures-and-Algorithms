""" Linear Search """
def linearSearch(ar, num):
    for i in range(len(ar)):
        if ar[i] == num:
            return i
    return False
    

# --- main ---
array = list(map(int,input("Enter space separated values : ").split()))
element = int(input("Enter the element to find : "))
index = linearSearch(array, element)
if index:
    print("Element found at position : ",index+1)
else:
    print("Element not found!")
