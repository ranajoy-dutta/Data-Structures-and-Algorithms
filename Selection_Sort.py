def selectionSort(arr):
    for i in range(len(arr)):
        min_pos = i                         # assuming i as the minimum element
        for j in range(i,len(arr)):         # finding the minimum element after i
            if arr[min_pos] > arr[j]:
                min_pos = j
                
        if min_pos != i:                    # swapping the minimum element with i position
            temp = arr[i]
            arr[i] = arr[min_pos]
            arr[min_pos] = temp

    return arr

# --- main ---
array = list(map(int, input("Enter Space separated elements : ").split()))
sorted_array = selectionSort(array)
print("Sorted Array : ",sorted_array)
