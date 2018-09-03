""" Binary Search """
def binarySearch(arr, num):
    beg = 0
    end = len(arr)
    while True:
        mid = (beg+end)//2
        print(mid,arr[mid])
        if arr[mid] == num:
            return mid
        elif arr[mid] > num:
            end = mid
        elif arr[mid] < num:
            beg = mid
        else:
            return False


# --- main ---
array = list(map(int,input("Enter space separated values : ").split()))
element = int(input("Enter the element to find : "))
index = binarySearch(array, element)
if index:
    print("Element found at position : ",index+1)
else:
    print("Element not found!")

            
