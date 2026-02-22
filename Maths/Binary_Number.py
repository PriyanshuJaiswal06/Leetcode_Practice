class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binary = ""
        flag = True
        while n>0:
            binary = str(n%2) + binary 
            n //= 2
        length = len(binary)
        for i in range(length - 1):
            
            if binary[i] == binary[i+1]:
                flag = False
            
        return flag