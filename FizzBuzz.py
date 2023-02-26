class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        
            
        """
        answer = []
        var = ''
        for i in range(1,n+1):
            if i%15 == 0:
                var = 'FizzBuzz'
            elif i%5 == 0:
                var = 'Buzz'
            elif i%3==0:
                var = 'Fizz'
            else:
                var = str(i)
            answer.append(var)
        return answer
