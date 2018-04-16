def findMedianSortedArrays(nums1, nums2):
    new_arr = []
    new_arr.extend(nums1)
    new_arr.extend(nums2)
    new_arr = sorted(new_arr)
    mid = len(new_arr)//2
    if len(new_arr)%2==0:
        return (new_arr[mid-1]+new_arr[mid])/2
    else:
        return new_arr[mid]

nums1 = [1,2,3]
nums2 = [4,5,6,7]
print(findMedianSortedArrays(nums1, nums2))
