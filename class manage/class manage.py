from lop import lop

def input_check(cls_input):
    for items in classes_list:
        for name in items:
            if name == cls_input:
                return items[name]
    return False

def add_lop(cls_input):
    name = cls_input
    pupil = str(input('Input number of pupils: '))
    absent = str(input('Input number of absence: '))
    teacher = str(input('Input homeroom teacher: '))
    ranking = str(input('Input ranking: '))
    class_name = lop(name,pupil,absent,teacher,ranking)
    return {name:class_name}

def info_upd(self): #self is class to update
    update = int(input('Info to update:\n1 for name\n2 for pupil\n3 for absence\n4 for teacher\n5 for ranking '))
    if update == 1:
        new_name = str(input('Input new name: '))
        lop.set_name(self,new_name)
    elif update == 2:
        new_pupil = str(input('Input new number of pupils: '))
        lop.set_pupil(self,new_pupil)
    elif update == 3:
        new_absent = str(input('Input new number of absence: '))
        lop.set_absent(self,new_absent)
    elif update == 4:
        new_teacher = str(input('Input new teacher: '))
        lop.set_teacher(self,new_teacher)
    elif update == 5:
        new_ranking = str(input('Input new ranking: '))
        lop.set_ranking(self,new_ranking)
    else:
        print('Invalid informationpp')

def cls_delete(cls_input):
    for items in classes_list:
        for name in items:
            if name == cls_input:
                classes_list.remove(items)


classes_list = []
name_only_list = []
def main():
    print('class management system\n0 to exit\n1 to add class\n2 to update class info\n3 to show one class info\n4 to show information of all classes')
    while True:
        print()
        command = int(input('Input command: '))
        if command == 1:
            duplicate = False
            cls_input = str(input('Input class name: '))
            for name in name_only_list:
                if cls_input == name:
                    duplicate = True
                    break
            if duplicate:
                print('Class already exists')
            else:
                class_name = add_lop(cls_input)
                classes_list.append(class_name)
                name_only_list.append(cls_input) 
        if command == 2:
            cls_input = str(input('Input class to update: '))
            if not input_check(cls_input):
                print('Invalid information')
                continue
            else:
                cls_to_use = input_check(cls_input)
                info_upd(cls_to_use)
        if command == 3:
            cls_input = str(input('Input class to show information: '))
            if not input_check(cls_input):
                print('Invalid information')
                continue
            else:
                lop.show_cls_info(input_check(cls_input))
        if command == 4:
            for items in classes_list:
                for name in items:
                    lop.show_cls_info(items[name])
                print()
        if command == 5:
            cls_input = str(input('Input class to delete: '))
            if not input_check(cls_input):
                print('Invalid information')
                continue
            else:
                cls_delete(cls_input)
        if command == 0:
            break
        else:
            continue


        


if __name__ == '__main__':
    main()






