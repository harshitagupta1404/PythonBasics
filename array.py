from array import *
# simple operations on array
"""arr=array('i', [1,2,3,4,5])
print(arr)"""
"""arr=array('i', [])
arr.append(1)
arr.append(1)
arr.append(1)
for i in range(len(arr)):
    print(i,arr[i])"""



# find sum of array
"""arr = array('i', [])
sum=0
size = int(input("enter size of array::"))
for i in range(size):
    arr.append(int(input("Enter element:")))
    sum+=arr[i]
print(arr)
print("sum::",sum)"""

# largest element in array
"""size = int(input("enter size::"))
arr=array('i',[])
for i in range(size):
    arr.append(int(input("enter element::")))
large=arr[0]
for i in range(1,len(arr)):
    if arr[i]>large:
        large=arr[i]
print("largest element::",large)"""

# split the array and add first part to the end
"""size = int(input("enter size::"))
arr=array('i',[])
for i in range(0,size):
    arr.append(int(input("enter element::")))
index = int(input("enter the split index:"))
i=0
while i<index:
    hi=arr[0]
    arr.remove(arr[0])
    arr.append(hi)
    i+=1
print(arr)"""

# check if array is monotonic or not

size = int(input("enter size:"))
arr = array('i',[])
for i in range(size):
    arr.append(int(input("enter element:")))
inc=0
dec=0
ctr=0
for i in range(size-1):
    if arr[i]>arr[i+1]:
        inc+=1
        if dec>0:
            ctr+=1
            break
    elif arr[i]<arr[i+1]:
        dec+=1
        if inc>0:
            ctr+=1
            break
    else:
        pass
if ctr==0:
    print("monotonic")
else:
    print("not monotonic")