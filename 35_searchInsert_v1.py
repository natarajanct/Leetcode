def searchInsert(nums, target):
    low = 0
    high = len(nums)-1
    while(low<=high):
        mid = (low+high)//2
        if (target == nums[mid]):
            return mid
        elif target > nums[mid]:
            low = mid+1
        else:
            high = mid-1
    return low

print(searchInsert([1,3,5,7], 4))
    
