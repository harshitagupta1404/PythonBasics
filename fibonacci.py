# fibonacci numbers less than the no entered
no = int(input("Enter n::"))

"""def fib(n):
    a = 0
    b = 1
    if n==1:
        print(a)
    else:
        print(a,end=" ")
        print(b,end=" ")
        c=a+b
        while c<n:
            print(c, end=" ")
            a=b
            b=c
            c=a+b

fib(no)"""

# check if no is fibonacci or not
# 5(n*n)+4 or 5(n*n)+4 should be perfect sq

import math
if (math.ceil(math.sqrt(5*no*no+4)) == math.sqrt(5*no*no+4) or math.ceil(math.sqrt(5*no*no-4)) == math.sqrt(5*no*no-4)):
    print("%d is fibonacci no"%no)
else:
    print("%d is not fibonacci no"%no)
