def searchInsert(nums, target):
    if len(nums)<1 or target < nums[0]:
        return 0
    elif target > nums[len(nums)-1]:
        return len(nums)
    elif len(nums)==1:
        if target == nums[0] or target < nums[0]:
            return 0
        else:
            return 1
    else:
        for i in range(len(nums)):
            if target == nums[i]:
                return i
            elif target > nums[i-1] and target < nums[i]:
                return i

print(searchInsert([1,3], 2))
    
