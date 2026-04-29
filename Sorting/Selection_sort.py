def sortArray(nums: List[int]) -> List[int]:
    for i in range(len(nums)): 
        mini = float('inf')
        for j in range(i,len(nums)):
            if nums[j] < mini:
                mini = nums[j]
                idx = j
        nums[i],nums[idx] = nums[idx],nums[i]
    return nums

print(sortArray([5,1,1,2,0,0]))
