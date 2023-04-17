class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if int(''.join(map(str,nums))) == 0:
            return "0"
        else:
            for i, n in enumerate(nums):
                nums[i] = str(n)
            def compare(n1,n2):
                if n1 + n2 > n2 + n1:
                    return -1
                else:
                    return 1
            nums = sorted(nums, key = cmp_to_key(compare))
            return "".join(nums)
