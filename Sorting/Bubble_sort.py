def sortArray(nums: List[int]) -> List[int]:
    maxi = float('-inf')
    n = len(nums)
    for i in range(len(nums)):
        for j in range(len(nums[:n-i-1])):
            if nums[j+1] < nums[j]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return nums

print(sortArray([2,3,6,1,0]))
