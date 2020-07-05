# armstrong no
no=int(input("Enter a no to check if it's armstrong no or not::"))
# n=no of digits
n=len((str(no)))
"""print(n)
print(type(no))"""
copy = no
sum=0
while copy > 0:
    rem=copy%10
    sum+=pow(rem,n)
    copy=copy//10
if no==sum:
    print("It is an armstrong no")
else:
    print("It is not an armstrong no")
