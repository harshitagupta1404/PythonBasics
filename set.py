# sets

"""set1 = {"a","b",'a'}
print(set1)
a = set('abcdef')
print(a)"""

"""String = ('G', 'e', 'e', 'k', 's', 'F', 'o', 'r')
Fset1 = frozenset(String)
print("The FrozenSet is: ")
print(Fset1)"""

"""set1={1,2,3,4,5}
set2=set1.copy()
print("ID of set1::",id(set1))
print("ID of set2::",id(set2))
set1.remove(2)
print("set1::",set1)
print("set2::",set2)"""

"""A = {10, 20, 30, 40, 80}
B = {100, 30, 80, 40, 60}
C=A.difference(B)
print(C)"""

A = {10, 20, 30, 40, 80}
B = {100, 30, 80, 40, 60}
A.difference_update(B)
print(A)