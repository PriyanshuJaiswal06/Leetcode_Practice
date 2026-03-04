class Solution:
    def isFascinating(self, n: int) -> bool:
        number = "123456789"
        num = str(n)+str(2*n)+str(3*n)
        if sorted(num) == sorted(number):
            return True
        else:
            return False