def removeDuplicates(self, nums):
    if len(nums)<2:
        return len(nums)
    else:
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==nums[i-1] and i!=0:
                del nums[i]
        return len(nums)
