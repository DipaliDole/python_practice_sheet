"""
# Operators and Conditional Statements
# if else condition

email = input("Enter your email:")
password = input("Enter your password:")

if email == "dipali@gmail.com" and password == "1234": 
    print ("welcome")
elif email == "dipali@gmail.com" and password != "1234":
    print ("invalid password")
    password = input("Enter your password:")
    if password == "1234":
        print ("welcome")
    else:
        print("invalid password")
else:
    print ("invalid email and password")


# if-else example 
# 1. find the min of 3 given numbers
# 2. Menu Driven Program 

a= int(input("Enter first number:"))
b= int(input("Enter second number:"))
c= int(input("Enter third number:"))

if a<b and a<c:
    print ("a is minimum")
elif b<a and b<c:
    print ("b is minimum")
else: 
    print("c is minimum")

import random 
number = random.randint(1, 10)

guess = int(input("guess the number"))
counter = 1
while number!= guess:
    if guess<number :
        print("guess higher")
    else :
        print("guess lower")
    guess = int(input("Guess the number"))
    counter += 1 
else :
    print("correct guessed")
    print("attempts", counter)
"""
# Program - The current population of a town is 10000. The population of the town is 
# increasing at the rate of 10% per year. You have to write a program to find out the 
# population at the end of each of the last 10 years.

current_pop = 10000

for i in range (10,0,-1):
    print(i,current_pop)
    current_pop = current_pop - 0.1*current_pop