# Given two binary strings a and b, return their sum as a binary string.
# In this problem, we have to add two binary string,
# and then return the sum of them in the binary string.
# Ex- a = 11, b = 1
# the sum of them will be 100 in binary 
# as a is equal to 3 and b is equal to 1 in deciaml system,
# and their sum will be 4 and it is representd as 100 in the binary digit system.

# My proposed solution for this problem is as follow:

# I first converted both the input string into int value and then converted into deciaml degit number,
# and then I sum the resultant of both conversion.
# And then I converted the resultant back to binary string value

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        int_a = int(a)
        int_b = int(b)
        decimal_sum = 0
        binary_sum = ""
        def binary_to_decimal(n):
            i = 0
            decimal = 0
            while n>0:
                decimal = (n%10)* (2**i) + decimal
                n //=10
                i += 1
            return(decimal)
        decimal_sum = binary_to_decimal(int_a) + binary_to_decimal(int_b)
        if decimal_sum == 0:
            return "0"
        while decimal_sum > 0:
            binary_sum = str(decimal_sum%2) + binary_sum
            decimal_sum //= 2
        return (binary_sum)