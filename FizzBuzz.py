class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        
            
        """
        answer = []
        var = ''
        for i in range(1,n+1):
            if n%15 == 0:
                var = 'FizzBuzz'
            elif n%5 == 0:
                var = 'Buzz'
            elif n%3==0:
                var = 'Fizz'
            else:
                var = str(n)
            answer.append(var)
        return answer
