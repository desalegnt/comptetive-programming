class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        nums = list(map(int, nums))
        nums.sort(reverse = True)
        return str(nums[k-1])
