def Phan_1():
    def Bai_1():
        inp = int(input("Input a number: "))
        def is_even(inp):
            if inp % 2 == 0:
                return True
            else:
                return False
        if is_even(inp):
            print("This number is even")
        else:
            print("This number isn't even")
    def Bai_2():
        inp = int(input("Input radius: "))
        def cal_area(inp):
            area = inp * 3.14
            return area
        print("Circle's area:",cal_area(inp))
    def Bai_3():
        inp = str(input("Input a text: "))
        def reverse_str(inp):
            a = inp[::-1]
            return a
        print("Reversed text:",reverse_str(inp))
    def Bai_4():
        inp = str(input("Input a text: "))
        def is_palindrome(inp):
            a = inp[::-1]
            if a == inp:
                return True
            else:
                return False
        if is_palindrome(inp):
            print("This is a palindrome")
        else:
            print("This is not a palindrome")

    b = int(input("Chon bai so may: "))
    if b == 1:
        Bai_1()
    if b == 2:
        Bai_2()
    if b == 3:
        Bai_3()
    if b == 4:
        Bai_4()
def Phan_2():
    def Bai_1():
        inp = int(input("Input a number: "))
        def exp(inp):
            total = 1
            for i in range(1,inp+1,1):
                total *= i
            return total
        print(str(inp)+"!"+"=",exp(inp))

    def Bai_2():
        list = [5, 1, 8, 92, -1, 30]
        a = list[:len(list)-1:1]
        print("Original list:",end = " ")
        for i in a:
            print(i,end = ",")
        print(list[len(list)-1]) 
        def is_sorted(): 
            list = [5, 1, 8, 92, -1, 30]
            sorted = []
            while True:
                sorted.append(min(list))
                list.remove(min(list))
                if len(list) == 0:
                    break
            return sorted
        print("Sorted list:",end = " ")
        for i in range(0,len(is_sorted())-1,1):
            print(is_sorted()[i],end = ",")
        print(is_sorted()[len(is_sorted())-1])

    def Bai_3():
        inp = int(input("Input a positive number: "))
        while inp <= 0:
            print("No negative number allowed")
            inp = int(input("Input a positive number: "))
        def print_fibo(inp):
            numbers = [1,1]
            fib = None
            for i in range (1,inp-1,1):
                fib = numbers[i] + numbers[i-1]
                numbers.append(fib)
                fib = None
            return numbers
        print("First",inp,"Fibonacci numbers:",end = " ")
        for i in print_fibo(inp):
            print(i,end = " ")

                


    b = int(input("Chon bai so may: "))
    if b == 1:
        Bai_1()
    if b == 2:
        Bai_2()
    if b == 3:
        Bai_3()

# def Phan_3():
    # def map():
    #     import random
    #     row_1 = ["P","-"*9]
    #     row_2 = ["-"*10]
    #     row_3 = ["-"*10]
    #     row_4 = ["-"*10]
    #     row_5 = ["-"*10]
    #     key_row = random.randint(2,3)
    #     door_row = random.randint(4,5)
    #     key_postition = None
    #     door_position = None
    #     #Choosing key position
    #     if key_row == 2:
    #         key_postition = random.randint(0,9,1)
    #         row_2.pop(key_postition)
    #         row_2.insert(key_postition,"K")
    #     if key_row == 3:
    #         key_postition = random.randint(0,9,1)
    #         row_3.pop(key_postition)
    #         row_3.insert(key_postition,"K")
    #     #Choosing door position
    #     if door_row == 4:
    #         door_postition = random.randint(0,9,1)
    #         row_4.pop(door_postition)
    #         row_5.insert(door_postition,"D")



        



    


a = int(input("Chon phan so may: "))
if a == 1:
    Phan_1()
if a == 2:
    Phan_2()

