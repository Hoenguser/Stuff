from VDV import athlete,Athlete_manager
login_info = {
    'user_name':'Hoang',
    'pass_word':'12345'
}

def check_login(username,password):

    if username == login_info['user_name'] and password == login_info['pass_word']:
        return True
    else:
        return False

athlete_list = Athlete_manager()
def show_menu():
    while True:
        print()
        print(
            '--Action menu--'
            '\n1. Add athlete'
            '\n2. Show athlete information'
            '\n3. Search for athlete'
            '\n4. Delete athlete'
            '\n0. Exit menu'
        )
        command = int(input('Input action: '))

        if command == 1:
            Athlete_manager.create_athlete(athlete_list)
            print(athlete_list.da_list)
        elif command == 2:
            Athlete_manager.info_output(athlete_list)
        elif command == 3:
            Athlete_manager.info_search(athlete_list)
        elif command == 4:
            Athlete_manager.del_athelete(athlete_list)
        elif command == 0:
            break
        else:
            print('Invalid action')
            continue


def main():
    invalid_count = 0
    print('--Athlete Covid management program--\nLogin to continue')
    res = False
    while res == False and invalid_count <5:
        username = str(input('Username: '))
        password = str(input('Password: ' ))
        res = check_login(username,password)
        if res == False:
            print('Incorrect info')
            print()
            invalid_count += 1
            if invalid_count == 5:
                print(f'You input wrong info {invalid_count} times.')
    if res == True:
        print('Correct info')
        show_menu()

ath_1 = athlete('Hoang Nguyen',2000,'Vietnam','currently')
ath_2 = athlete('John Doe',1998,'America','over')
athlete_list.da_list.append(ath_1)
athlete_list.da_list.append(ath_2)           

if __name__ == '__main__':
    main()
