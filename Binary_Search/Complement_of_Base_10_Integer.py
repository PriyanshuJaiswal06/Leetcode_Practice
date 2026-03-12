class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        binary = ""
        decimal = 0
        power = 0
        while n>0:
            rem = n%2
            if rem == 1:
                rem = 0
            else:
                rem = 1
            binary = str(rem) + binary
            n //= 2
        for i in range(len(binary)-1, 0, -1):
            if binary[i] == "1":
                decimal += 2**power
            power += 1
        return decimal