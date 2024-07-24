import random
import string
print("enter the desired length of the password")
n=int(input())
password=""
for i in range(0,n):
    password=password+random.choice(string.ascii_letters)
print(password)
    
