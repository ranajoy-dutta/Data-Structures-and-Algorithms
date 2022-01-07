def bubble_sort(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped==False:          # exit if array is already sorted
            break
    return arr

# --- main ---
array = list(map(int, input("Enter space separated numbers : ").split()))
sorted_array = bubble_sort(array)
print("Sorted Array : ",sorted_array)
