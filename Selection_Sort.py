def selectionSort(arr):
    for i in range(len(arr)):
        min_pos = i
        for j in range(i,len(arr)):
            if arr[min_pos] > arr[j]:
                min_pos = j
        if min_pos != i:
            temp = arr[i]
            arr[i] = arr[min_pos]
            arr[min_pos] = temp
    return arr

# --- main ---
array = list(map(int, input("Enter Space separated elements : ").split()))
sorted_array = selectionSort(array)
print("Sorted Array : ",sorted_array)
