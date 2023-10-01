class athlete:
    count = 0
    def __init__(self,full_name,birth_year,country,isolation_status):
        self.full_name = full_name
        self.birth_year = birth_year
        self.country = country
        self.isolation_status = isolation_status
        athlete.count += 1
        self.id = f'{athlete.count}{country[0:3]}'
    
    def show_info(self):
        print(f'--Information of {self.full_name}--'
              f'\nFull name: {self.full_name}'
              f'\nBirth year: {self.birth_year}'
              f'\nCountry: {self.country}'
              f'\nIsolation status: {self.isolation_status}'
              f'\nID: {self.id}'
              )

class Athlete_manager:
    def __init__(self):
        self.da_list = []

    def create_athlete(self):
        full_name = str(input('Full name: '))
        birth_year = int(input('Birthyear: '))
        country = str(input('Country of origin: '))
        isolation_status = str(input('--Isolation status--'
                                    '\nNormal for no isolation'
                                    '\nCurrently for in islation'
                                    '\nOver for isolation over'
                                    '\nInput: '))
        ath = athlete(full_name,birth_year,country,isolation_status)
        self.da_list.append(ath)
    
    def info_output(self):
        num_of_athlete = str(input('Number of athletes to show information: '))

        if num_of_athlete.isdigit() == True:
            if int(num_of_athlete) <= len(self.da_list):
                for i in range (0,int(num_of_athlete)):
                    athlete.show_info(self.da_list[i])
                    print()
            else:
                print('Input is larger than number of athletes')

        elif num_of_athlete == 'all':
            for i in self.da_list:
                athlete.show_info(i)
                print()
    
    def show_info(self):
        print(f'--Information of {self.full_name}--'
              f'\nFull name: {self.full_name}'
              f'\nBirth year: {self.birth_year}'
              f'\nCountry: {self.country}'
              f'\nIsolation status: {self.isolation_status}'
              f'\nID: {self.id}'
              )
    
    def info_search(self):
        invalid = False
        name_or_id = str(input('Athlete full name or id: '))

        for items in self.da_list:
            if name_or_id == items.full_name or name_or_id ==  items.id:
                print(items.full_name,items.id)
                Athlete_manager.show_info(items)
                invalid = True
                break

        if invalid == False:
            print('Invalid name or id')
    
    def del_athelete(self):
        position = int(input('Athlete ordinal number: '))

        if position > len(self.da_list):
            print('Input exceeds number of athletes')

        else:
            confirm = int(input(f'Do you want to delete {self.da_list[position-1].full_name}?'
                                '\n1 for yes\n0 for no\nInput: '))
            if confirm == 1:
                self.da_list.pop(position-1)
            elif confirm == 0:
                pass
            else:
                print('Invalid input')
    


