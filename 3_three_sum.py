def threeSum(nums):
    nums.sort()
    output=[]
    for i in range(len(nums)-2):
        if i>0 and nums[i]==nums[i-1]:
            continue
        first = i+1
        last = len(nums)-1
        while first<last:
            if nums[i]+nums[first]+nums[last]<0:
                first = first+1
            elif nums[i]+nums[first]+nums[last]>0:
                last = last-1
            else:
                output.append((nums[i],nums[first],nums[last]))
                while first<last and nums[first]==nums[first+1]:
                    first = first+1
                while first<last and nums[last]==nums[last-1]:
                    last = last-1
            first=first+1
            last=last-1
    return output

