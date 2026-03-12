n = 10
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
print(binary)
for i in range(len(binary)-1, 0, -1):
    
    if binary[i] == "1":
        decimal += 2**power
    power += 1
