from math import sqrt

# check if no is prime or not
"""no=int(input("Enter a no::"))
for i in range(2,int(sqrt(no))):
    if no%i==0:
        print("not prime")
        break;
else:
    print("prime")"""

# print all prime nos in an interval
a,b = input("Enter the range::").split(",")
for i in range(int(a),int(b)+1):
    ctr = 0
    for j in range(2,int(int(i))):
        if i%j==0:
            ctr+=1
            break
    if ctr==0:
        print(i, end=" ")

# print("a: %d, b: %d" %(int(a),int(b)))