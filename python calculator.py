#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Rudra Shekhar Nag
#
# Created:     02/03/2024
# Copyright:   (c) Rudra Shekhar Nag 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
print("Python Calculator")
first = input("enter first number : ")
second = input("enter second number : ")
operator = input("please enter your desired operator")

if operator == "+" :
    ans = int(first) + int (second)
    print(" Your answer is "+ str(ans))

elif operator == "-" :
    ans = int(first) - int (second)
    print(" Your answer is "+ str(ans))

elif operator == "*" :
    ans = int(first) * int (second)
    print(" Your answer is "+ str(ans))

elif operator == "/" :
    ans = int(first) / int (second)
    print(" Your answer is "+ str(ans))

elif operator == "%" :
    ans = int(first) - int (second)
    print(" Your answer is "+ str(ans))

elif operator == "**" :
    ans = int(first) ** int (second)
    print(" Your answer is "+ str(ans))

elif operator == "//" :
    ans = int(first) // int (second)
    print(" Your answer is "+ str(ans))