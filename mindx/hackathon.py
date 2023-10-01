# Bai 4 Phan 1
# from turtle import *
# a = float(input("Input circle's radius: "))
# penup()
# left(90)
# for i in range (100):
#     forward(a)
#     pendown()
#     forward(2)
#     right(180)
#     penup()
#     forward(a)
#     right(183.6)

# mainloop()

#Phan 2
#Bai 1
# for i in range (3,13,1):
#     print (i)

#Bai 2
# a = int(input("Input a number: "))
# if a <= 0:
#     print("Number must be larger than 0")
# else:
#     for i in range (0, a+1, 1):
#         print(i)

#Bai 3
# a = int(input("Input a number: "))
# if a <= 0:
#     print("Number must be larger than 0")
# else:
#     for i in range(1, a+1,2):
#         print(i)

#Bai 4
# n = int(input("Input number of edges: "))
# from turtle import *
# pendown()
# left(90)
# for i in range(n):
#     right(360/n)
#     forward(100)

# mainloop()

#Phan 3
#Bai 1
# a = float(input("Input a number: "))
# if a >= 13:
#     print("This number is larger than 13")
# elif a == 13:
#     print("it's just 13")
# else:
#     print("This number is not larger than 13")

#Bai 2
# a = int(input("Input a number: "))
# if a%2 == 0:
#     print("This number is even")
# else:
#     print("This number is not even")

#Bai 3
# a = int(input("Input a month: "))
# if a == 2:
#     print("This month has 28 days")
# elif a%2 == 0:
#     print("This month has 30 days")
# else:
#     print("This month has 31 days")

#Phan 4
#Bai 1
# print("== Registration ==")
# a = str(input("username: "))
# b = str(input("Password: "))
# c = str(input("Email: "))
# print("Registered successfully")

#Bai 2
# print("== Registration ==")
# a = str(input("username: "))
# b = str(input("Password: "))
# c = str(input("Repeat password:"))
# while b != c:
#     print("Invalid password. Please input again.")
#     c = str(input("Repeat password:"))
#     if b == c:
#         break
# d = str(input("Email: "))
# print("Registered successfully.")

#Bai 3
# print("== Registration ==")
# a = str(input("username: "))
# b = str(input("Password: "))
# c = str(input("Repeat password:"))
# while b != c:
#     print("Invalid password. Please input again.")
#     c = str(input("Repeat password:"))
#     if b == c:
#         break
# while True:
#     d = str(input("Email: "))
#     check = d.count("@")
#     chack = d.count(".")
#     kytu = len(d)
#     if check == 0 or chack == 0 or kytu <= 8:
#         print("Invalid email. Please input again.")
#     else:
#         break
# print("Registered successfully.")

#Phan 5
print("== FREAKING MATH CONSOLE ==")
print("Give correct answers to get scores")
import random
score = 0
scorelist = []
while True:
    left = None
    right = None
    result = None
    sign = None
    op = int(random.randint(1,4))
    if op == 1:
        left = random.randint(0,50)
        right = random.randint(0,50)
        sign = '+'
        result = left + right
    elif op == 2:
        left = random.randint(0,50)
        right = random.randint(0,left-1)
        sign = '-'
        result = left - right
    elif op == 3:
        left = random.randint(0,20)
        right = random.randint(0,10)
        sign = 'x'
        result = left * right
    elif op == 4:
        right = random.randint(1,10)
        result = random.randint(1,20)
        sign = "/"
        left = right * result
    cor_ans = random.randint(0,1)
    if not cor_ans:
        result = result + random.randint(1,10)
    print(str(left),sign,str(right),"=",str(result))
    choice = int(input("1 for True, 0 for False: "))
    if choice == cor_ans:
        score = score + 1
        print("Score: ",score)
    else:
        print("Incorrect")
        print("Your score is",score)
        scorelist.append(score)
        print("Do you wish to play again? 1 for yes, 0 for no: ", end = "")
        redo_choice = int(input())
        if redo_choice == 1:
            score = 0
            continue
        else:
            break
scorelist.sort
sl_counter = len(scorelist) - 1
highscore = scorelist[sl_counter]
print("Game over")
print("Highscore:",highscore)


    




    









