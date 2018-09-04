def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr

# --- main ---
array = list(map(int, input("Enter space separated numbers : ").split()))
sorted_array = bubbleSort(array)
print("Sorted Array : ",sorted_array)
