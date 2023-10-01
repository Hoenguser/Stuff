# list = [2,4,9,13,17,18,22,1,3]
# split = []
# if len(list) == 1:
#     for i in list:
#         print(i,end = " ")
# else:
#     for i in range (0,len(list)//2-1,1):
#         split.append(list[i])

# num_list = [567,945,853,7584,9456,4655,2367,3745]
# def happy_number(number):
#     str_num = str(number)
#     sum_even = 0
#     sum_odd = 0
#     for i in range (len(str_num)):
#         value_str = str_num[i]
#         if %2 == 0:
#             sum_even += value
#         else:
#             sum_odd += value
#     return sum_even == sum_odd

# happy_num = filter(happy_number,num_list)
# print(list(happy_num))



# num_list = [45,78,64,5,32,76,128]
# def exponential(i):
#     copy = i
#     while True:
#         copy /= 2
#         if copy <=2:
#             break
#     if copy ==2:
#         return i
# expo = filter(exponential,num_list)
# for i in list(expo):
#     print(i,end = " ")

# num_list = [43,28,87,6,90]
# def perfect_number(number):
#     while number % 2 == 0:
#         sum_factor = 0
#         half = number // 2
#         for i in range (1,half+1):
#             if number % i == 0:
#                 sum_factor += i
#         return sum_factor == number
#     return False

# perfect_num = filter(perfect_number,num_list)
# print(list(perfect_num))

class lop:
    count = 0
    def __init__(self,name,pupil,absent,teacher,ranking):
        self.name = name
        self.pupil = pupil
        self.absent = absent
        self.teacher = teacher
        self.ranking = ranking

        lop.count += 1
    
#Getter&setter
    def get_name(self):
        return self.name
    
    def set_name(self,new_name):
        self.name = new_name
    
    def get_pupil(self):
        return self.pupil
    
    def set_pupil(self,new_pupil):
        self.pupil = new_pupil
    
    def get_absent(self):
        return self.absent
    
    def set_absent(self,new_absent):
        self.absent = new_absent
    
    def get_teacher(self):
        return self.teacher
    
    def set_teacher(self,new_teacher):
        self.teacher = new_teacher
    
    def get_ranking(self):
        return self.ranking
    
    def set_ranking(self,new_ranking):
        self.ranking = new_ranking
#Show info
    def show_cls_info(self):
        print(f'\nClass{self.name} information')
        print(f'name: {lop.get_name(self)}')
        print(f'pupil: {lop.get_pupil(self)}')
        print(f'absent: {lop.get_absent(self)}')
        print(f'teacher: {lop.get_teacher(self)}')
        print(f'ranking: {lop.get_ranking(self)}')

    






        

        

        
