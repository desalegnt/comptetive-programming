class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        ans = []
        i,j = 0, len(nums) - 1
        while len(nums) != len(ans):
            ans.append(nums[i])
            if i != j:
                ans.append(nums[j])
            i += 1
            j -= 1
        return ans
