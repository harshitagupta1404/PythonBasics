no = int(input("Enter the no::"))

# approach 1
"""f=1
if no==1 or no==0:
    f=1
else:
    for i in range(1,no+1):
        f=f*i
print("factorial of "+str(no)+" = "+str(f))"""

# approach 2
def fact(n):
    """if n > 1:
        return n*fact(n-1)
    else:
        return 1"""
    if n==1:
        return 1
    else:
        return n*fact(n-1)

if no == 1 or no==0:
    f=1
else:
    f = fact(no)
print("factorial of "+str(no)+" = "+str(f))