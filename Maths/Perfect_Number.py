class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        import math
        factors = []
        sum = 0
        if num == 1:
            return False
        for i in range(1, int(math.sqrt(num))+1):
            if num%i == 0:
                factors.append(i)
                if i != num // i:
                    if num// i != num:
                        factors.append(num//i)
        for i in factors:
            sum += i
        if sum == num:
            return True
        else:
            return False