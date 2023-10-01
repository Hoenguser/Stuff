def Bai_1():
    numbers = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5,
               'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10}
    num_inp = str(input("Input a roman number: "))
    for key in numbers:
        if num_inp == key:
            print(numbers[key])
    if not num_inp in numbers:
        print("Not found")

def Bai_3():
    number_list = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X',
                 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX']
    number_dic = {}
    value = 1
    for i in number_list:
        number_dic[i] = value
        value += 1
    num_inp = str(input("Input a roman number: "))
    for key in number_dic:
        if num_inp == key:
            print(number_dic[key])
    if not num_inp in number_dic:
        print("Not found")

def Bai_4():
    students = [{'firstName': 'Nikki', 'lastName': 'Roysden'},
            {'firstName': 'Mervin', 'lastName': 'Friedland'},
            {'firstName': 'Aron', 'lastName': 'Wilkins'}]
    print("List of students: ",end = "")
    for index in students:
        print()
        print("-",end = " ")
        for keys in index:
            print(index[keys],end = " ")

def Bai_5():
    names = {
    'students': [
    {'firstName': 'Nikki', 'lastName': 'Roysden'},
    {'firstName': 'Mervin', 'lastName': 'Friedland'},
    {'firstName': 'Aron', 'lastName': 'Wilkins'}
    ],
    'teachers': [
    {'firstName': 'Amberly', 'lastName': 'Calico'},
    {'firstName': 'Regine', 'lastName': 'Agtarap'}
  ]
}
    position = 0
    for category in names:
        print("List of",category+":", end = "")
        for name in names[category]:
            print()
            print("-",end = " ")
            # print(name)
            for keys in name:
                print(name[keys],end = " ")
        print()

def Bai_6():
    sequence = str(input("Input sequence: "))
    characters = {}
    for i in range (0,len(sequence),1):
        characters[sequence[i]] = 0
    for i in characters:
        for a in sequence:
            if a == i:
                characters[i] += 1
    print("Frequency of characters: ")
    for i in characters:
        print(i+":",characters[i])




a = int(input("Chon bai so may: "))
if a == 1:
    Bai_1()
if a == 3:
    Bai_3()
if a == 4:
    Bai_4()
if a == 5:
    Bai_5()
if a == 6:
    Bai_6()