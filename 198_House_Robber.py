def rob(nums):
    if len(nums)<1:
        return 0
    elif len(nums)==1:
        return(nums[0])
    elif len(nums)==2:
        return(max(nums[0],nums[1]))
    else:
        max_profit = nums[0]
        a = 0
        for i in range(1,len(nums)-1):
            b = nums[i+1]+max_profit
            max_profit = max(a,b)
            a = max_profit
    return max_profit
print(rob([1,2,3,4,5]))
