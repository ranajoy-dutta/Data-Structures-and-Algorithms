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



            
