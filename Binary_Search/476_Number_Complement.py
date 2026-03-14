class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0:
            return 1
        binary = ""
        decimal = 0
        power = 0
        while num>0:
            rem = num%2
            if rem == 1:
                rem = 0
            else:
                rem = 1
            binary = str(rem) + binary
            num //= 2
        for i in range(len(binary)-1, 0, -1):
            if binary[i] == "1":
                decimal += 2**power
            power += 1
        return decimal