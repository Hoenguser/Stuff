# def check_square(number):
#     if number == 1:
#         return True
#     else:
#         for i in range (1,number):
#             if i*i == number:
#                 return True
#         return False

# num_list = [5,3,1,9,45,49]
# square = filter(check_square,num_list)
# print(list(square))

# import random
# def gen_list(n):
#     num_list = []
#     for i in range (n):
#         number = random.randint(-100,100)
#         num_list.append(number)
#     return num_list

# def find_number(array,find):
#     for i in range(len(array)):
#         if array[i] == find:
#             break
#         else:
#             return -1
#     return i

# # search = int(input("Number to find: "))
# # result = find_number(search)
# # if not result:
# #     print("Number doesn't exist")
# # else:
# #     print(i)
# def main():
#     n = int(input("Input list length:"))
#     array = gen_list(n)
#     print(array)
#     find_num = int(input("Input number to find: "))
#     index = find_number(array,find_num)
#     print(index)
#     if index == -1:
#         print("Number doesn't exist")
#     else:
#         print(f'Number {find_num} at index',index)

# if __name__ == '__main__':
#     main()

# class student:
#     student_count = 0
#     def __init__(self,first,last,grade):
#         self.first = first
#         self.last = last
#         self.grade = grade
#         self.email = f'{first}{last}@gmail.com'

#         student.student_count += 1
    
#     def full_name(self):
#         return f'{student.first} {student.last}'

#     @classmethod
#     def from_string(cls, student_str):
#         first, last, grade = str(student_str).split('-')
#         return cls(first,last,grade)


# stud_1_str = 'Stephen-King-9'
# stud_2_str = 'John-Doe-10'

# stud_1 = student.from_string(stud_1_str)
# stud_2 = student.from_string(stud_2_str)

# class collegue(student):
#     def __init__(self, first, last, grade,key):
#         super().__init__(first, last, grade)
#         self.key = key



num_list = [
    {
        'a':{
            'name':'th',
            'age':30,
        }
    },
    {
        'b':{
            'name':'pop',
            'age':15,
        }
    },
    {
        'c':{
            'name':'kk',
            'age':43,
        }
    }
]

print(num_list[2])

        





    





# avatar = movies()
# avatar.name = 'avatar'
# avatar.director = 'James Cameron'
# avatar.genre = 'action'
# avatar.duration = 192
# avatar.rating = 9.5

# avatar.year = 2009
# class copy(movies)