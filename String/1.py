y = int(input())
for i in range(y):
    x = int(input())

count= 0
def sum(n):
    sum = 0
    while n>0:
        sum += n%10
        n //= 10
    return sum
len_x = len(str(x))
range_l = 1+ (len_x * 9)
for i in range(x, x + range_l):
    if x == i - sum(i):
        count += 1
print(count)