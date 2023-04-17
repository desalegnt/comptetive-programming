class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        answer = []
        intervals.sort()
        for i in intervals:
            if answer and i[0] <= answer[-1][1]:
                answer[-1][1] = max(answer[-1][1], i[1])
            else:
                answer.append(i)
        return answer
