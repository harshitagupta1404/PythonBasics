#linear search

from array import *
arr = array('i',[])
n=int(input("Enter size of array::"))
for i in range(n):
    x=int(input("enter the values in array::"))
    arr.append(x)
no=int(input("Enter no to search::"))
for i in range(0, len(arr)):
    if no==arr[i]:
        print("Found at position "+str(i+1))
        break
    else:
        print("Not found")