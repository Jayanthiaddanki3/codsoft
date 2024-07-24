import random
user=input("enter your choice(rock,paper,scissors)").lower()
while user not in ["rock","paper","scissors"]:
    print("invalid choice")
    user=input("enter your choice(rock,paper,scissors)").lower()
print("users choice is :",user)
list=["rock","paper","scissors"]
computer=random.choice(list)
print("computer choice is",computer)
if(user==computer):
    print("its tie")
elif(user=="rock" and computer=="scissors"):
    print("user won")
elif(user=="paper" and computer=="rock"):
    print("user won")
elif(user=="scissors" and computer=="paper"):
    print("user won")
else:
    print("computer won")
while True:
    result = input("do you want to play again(yes/no)").lower()
    if(result!= "yes"):
        print("thanks for playing")
        break


