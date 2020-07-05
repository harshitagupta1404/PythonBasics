from collections import deque
d = deque('ghi')
for elem in d:
    print(elem.upper())
d.append('j')
d.appendleft('f')
print(d)
"""print(d[0])
print(type(d))
print(d[-1])"""
d.reverse()
print("reverse deque::", d)
deque(reversed(d))
print("reversed::", deque )
"""lst=list(d)
print(type(lst))
print(lst)
print(lst[0])"""