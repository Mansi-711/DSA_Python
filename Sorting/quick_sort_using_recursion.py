def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[-1]
        left, right = [],[]
        for i in range(len(arr)-1):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        left = quick_sort(left)
        right = quick_sort(right)
    return left + [pivot] + right
    
arr= [5,2,3,4,1]
print(quick_sort(arr))
