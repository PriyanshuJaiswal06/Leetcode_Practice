#Given an integer n, return true if it is a power of two. Otherwise, return false.

#An integer n is a power of two, if there exists an integer x such that n == 2x.

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        result = 0
        while n>1:
            result += n%2
            n //= 2
        if result == 0:
            return True
            
        else:
            return False

 