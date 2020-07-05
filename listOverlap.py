a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
"""a.sort()
b.sort()
l1=len(a)
l2=len(b)
res=l1 if(l1>l2) else l2
while i in range(res):
    if a[i]<b[i]"""
c=[]
for i in a:
    if i in b and i not in c:
        c.append(i)
print(c)    
