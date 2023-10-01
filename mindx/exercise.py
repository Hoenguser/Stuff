#Bai 1
# inp = int(input("Input a whole number: "))
# total = 0
# for i in range(1, inp+1,1):
#     total = total + i
# print(total)

#Bai 2
# start = int(input("Input starting number: "))
# stop = int(input("Input stopping number: "))
# for i in range (start, stop +1, 1):
#     if i % 7 == 0:
#         print(i)

#Bai 3
# start = int(input("Input starting number: "))
# stop = int(input("Input stopping number: "))
# count = 0
# for i in range (start, stop+1,1):
#     for a in range(1,i + 1,1):
#         if i % a == 0:
#             count += 1
#         if count == 3:
#             break
#     if count == 2:
#         print(i)
#     count = 0

#Bai 4
# inp = int(input("Input a number: "))
# total = 1
# for i in range (1, inp +1, 1):
#     total *= i
# print(total)

#Bai 5
# inp = str(input("Input a string: "))
# kytu = []
# sum = ""
# a = len(inp)
# for i in range(a,0,-1):
#     kytu.append(inp[i-1])
#     a -= 1
# for i in range(0,len(kytu),1):
#     sum += kytu[i]
# if sum == inp:
#     print("Day la chuoi doi xung")
# else:
#     print("Day khong la chuoi doi xung")

#Bai 6
# inp = int(input("Input an odd number: "))
# count = "*"
# space = " " 
# for i in range(1, inp+1,1):
#     print(space*(inp-i),count*(2*i-1))

    

#Bai 7
# for i in range(2,11,1):
#     print("Bang cuu chuong",i)
#     for a in range (1, 11,1):
#         print(i,"x",a,"=",i*a)




def Bai_1():
    contact_list = {}
    def add_contact(name,number):
        contact_list[name] = number
    def delete_contact(name):
        contact_list.pop(name)
    def upd_contact(name,number):
        name = str(input("Name to update: "))
        for keys in contact_list:
            if name == keys:
                number = str(input("Updated number: "))
                contact_list[name] = number
                return True
            else:
               return False
        

    
    while True:
        a = str(input("Type a command: "))
        if a == "add":
            name = str(input("Add contact's name: "))
            number = str(input("Add number: "))
            add_contact(name,number)
        if a == "delete":
            name = str(input("Delete name: "))
            delete_contact(name)
        if a == "update":
            while True:
                if upd_contact(name,number):
                    break
                else:
                    continue
        if a == "view":
            for keys in contact_list:
                print(keys+":",contact_list[keys])
        if a == "none":
            break

def Bai_2():
    exchange_list = {
        "USD":24000,
        "YUAN":3300
        
        
    }
    changed = str(input("Input changed currency: "))
    number = int(input("Input amount to exchange: "))
    def exchange(changed,number):
        dollar = None
        yuan = None
        if changed == "USD":    
            dollar = number/exchange_list["USD"]
            return round(dollar,2)
        elif changed == "YUAN":
            yuan = number/exchange_list["YUAN"]
            return round(yuan,2)
    print(exchange(changed,number),changed)

def Bai_3():
    score_list = {}
    while True:
        command = int(input("1 to add student's score, 2 to see score list,0 to stop: "))
        if command == 1:
            name = str(input("Input student's name: "))
            score = str(input("Input student's score: "))
            score_list[name] = score
        if command == 2:
            for scores in score_list:
                print(scores+":",score_list[scores])
        if command == 0:
            break
def Bai_4():
    print('Insert keys, press 0 to stop:')
    key_dic = {}
    dup_dic = {}
    while True:
        key = str(input())
        if key == '0':
            # key_dic.popitem()
            break
        value = str(input(key+":"))
        key_dic[key] = value
        for keys in key_dic:
            if not keys in dup_dic:
                dup_dic[key] = value
    print("Final list")
    for i in dup_dic:
        print(i+":",dup_dic[i])
    
    


    
    

    



a = int(input("Chon bai so may: "))
if a == 1:
    Bai_1()
if a == 2:
    Bai_2()
if a == 3:
    Bai_3()
if a == 4:
    Bai_4()



  
