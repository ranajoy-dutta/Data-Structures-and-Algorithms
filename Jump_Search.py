""" Jump Search """
import math

def jumpSearch(arr, element, n):
    step = int(math.sqrt(n))
    prev = 0
    print(step)
    while arr[int(min(step, n)-1)] < element:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return False
    while arr[int(prev)] < element:
        prev += 1
        if prev == min(step, n):
                return -1
    if arr[int(prev)] == element:
            return int(prev)    

            
# --- main ---
array = list(map(int,input("Enter space separated values : ").split()))
element = int(input("Enter the element to find : "))
step = int(input("Enter step value : "))
step = len(array)
index = jumpSearch(array, element, step)
if index:
    print("Element found at position : ",index+1)
else:
    print("Element not found!")
