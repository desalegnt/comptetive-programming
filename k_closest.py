class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        k_closest = []
        for i,j in points:
            heapq.heappush(k_closest, ((math.sqrt(i**2 + j**2)),[i,j]))
        answer = []
        s = 1
        while k_closest and s<=k:
            h = heapq.heappop(k_closest)
            answer.append(h[1])
            s += 1
        return answer
