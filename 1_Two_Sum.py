class Solution:
    def twoSum(self, nums, target):
        d = {}
        for i,num in enumerate(nums):
            m = target - num
            if m in d:
                return([d[m],i])
            else:
                d[num] = i

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
