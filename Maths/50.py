
def myPow( x: float, n: int) -> float:
    a=x
    if(n==0):
        return 1
    if(n<0):
        x=1/x
    for i in range(0,abs(n)-1):
        x=a*x
    
    return x
print(myPow(0.00001, 2147483647))
