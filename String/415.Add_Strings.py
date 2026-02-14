#Given two non-negative integers, num1 and num2 represented as string, 
#return the sum of num1 and num2 as a string.

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        a = 0
        b = 0
        sum = 0
        for i in num1:
            a = a * 10 + (ord(i) - ord('0'))
        for j in num2:
            b = b * 10 + (ord(j) - ord('0'))  
        sum = a + b
        if sum == 0:
            return "0"
        s = ""
        while sum>0:
            s = chr(sum%10 + ord('0')) + s 
            sum //= 10
        return s