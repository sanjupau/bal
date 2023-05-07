def partition(arr, pivot):
   
    pivot_val = arr[pivot]
 
    i = 0
    
    for j in range(len(arr)):
        
        if arr[j] < pivot_val:
           
            arr[i], arr[j] = arr[j], arr[i]
            
            i += 1
    
    arr[i], arr[pivot] = arr[pivot], arr[i]
    
    return i
arr = input("Enter the array elements separated by space: ").split()
arr = [int(i) for i in arr]
pivot = int(input("Enter the index of the pivot value: "))
partition(arr, pivot)
print("Partitioned array:", arr)



OUTPUT:
  Enter the array elements separated by space: 6 3 2 5 7
Enter the index of the pivot value: 3
Partitioned array: [3, 2, 5, 6, 7]
