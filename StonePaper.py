A="Stone"
B="Paper"
if A==B:
    print("It's a tie!!")
elif A=="Stone":
    if B=="Paper":
        print("B wins")
    else:
        print("A wins")
elif A=="Paper":
    if B=="Stone":
        print("A wins")
    else:
        print("B wins")
elif A=="Scissor":
    if B=="Stone":
        print("A wins")
    else:
        print("B wins")
print("Do u want to play again?")
