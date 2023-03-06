class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        for i in range(l):
            for j in range(l):
                if nums[i] < nums[j]:
                    nums[i],nums[j] = nums[j],nums[i]
        
