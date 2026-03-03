n = 192
number = "123456789"
num = str(n)+str(2*n)+str(3*n)

for i in num:

    if i in number:
        number.replace(i, " ")
        num.replace(i, " ")
print(num)
print(number)
if  len(num) == 0:
    print(True)
else:
    print(False)
