class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = list()
        for i in nums:
            c = 0
            for j in nums:
                if j < i:
                    c += 1
            output.append(c)
        return output
