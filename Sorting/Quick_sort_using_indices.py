def partition(arr,low,high):
    pi = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] < pi:
            i+=1
            arr[i],arr[j] = arr[j], arr[i]
            
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1

def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr,low, p-1)
        quick_sort(arr,p+1,high)
        
    return arr
    
arr = [4,1,9,2,8,3]
print(quick_sort(arr, 0, len(arr)-1))
    
