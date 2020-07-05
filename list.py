# Creating a List
"""List = [1, 2, 3, 4]
print("Initial List: ")
print(List.index(4,1,2))
print(List)

# Addition of multiple elements
# to the List at the end
# (using Extend Method)
List.extend((8, 'Geeks', 'Always'))
print("\nList after performing Extend Operation: ")
print(List)"""

# print elements of list less than 5
"""lst = [1,1,3,5,8]
for i in range(len(lst)):
  if lst[i]<5:
    print(lst[i])"""

# divisors of given number
"""no=26
lst=[]
for i in range(1,no+1):
    if no%i==0:
        lst.append(i)
print(lst)"""

# swapping first and last elements in a list
"""lst = list()
size = int(input("enter size:"))
for i in range(size):
    lst.append(int(input("enter element:")))
lst[0],lst[size-1]=lst[size-1],lst[0]
print(lst)"""


"""squares = []
for x in range(10):
    squares.append(x**2)
    print(x)
print(squares)
squares = [x**2 for x in range(10)]
print(squares)
print(type(squares))"""

# list comprehensions
"""vec = [-4,-2,0,2,4]
lst1 = [x*2 for x in vec]
print(lst1)
lst2 = [x for x in vec if x>=0]
print(lst2)
lst3 = [(x,y**2) for x in vec for y in vec]
print(lst3)"""

# FLATTEN A LIST
"""vec = [[1,2,3],[4,5,6],[7,8,9]]
lst = [x for y in vec for x in y]
print(lst)"""

# TRANSPOSE ROWS AND COLUMNS
"""matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]
# lst = [[row[i] for row in matrix] for i in range(4)]
lst = []
for i in range(4):
    lst.append([row[i] for row in matrix])
    print("after appending an element::",lst)
print(lst)"""

"""lst="stri"
a,b,c,d = lst
#print(lst)
print(a,b,c,d)"""

# slice
"""words = ['banana', 'pie', 'Washington', 'book']
#sorted(words, key=lambda x: x[::-1])
words[0][::-1]
print(words)"""

"""phrases = ['when in rome', 'what goes around comes around', 'all is fair in love and war']
for x in phrases:
    print(x.split()[2][1])
del(phrases)
print(phrases)"""

nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# print(nums[3:-5])
# print(nums)

print(nums[slice(2,6)])