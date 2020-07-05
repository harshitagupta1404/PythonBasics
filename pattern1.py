# pattern1
"""for i in range(4):
    for j in range(4):
        print("#", end="")
    print()"""

# pattern2
"""for i in range(4):
    for j in range(i+1):
        print("#", end=" ")
    print()"""

# pattern3
for i in range(4):
    for j in range(4-i):
        print("#", end=" ")
    print()