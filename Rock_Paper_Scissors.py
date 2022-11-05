import random
def rps():
    player_choice = input("Enter Your Choice : r, p, s for rock, Paper, Scissor \n")
    choice_options = ['r','p','s']
    comp_choice = random.choice(choice_options)
    print(f'You chose {player_choice} and Computer chose {comp_choice}')
    if player_choice == comp_choice:
        print(f'It is a tie.')
    elif player_choice == 'r':
        if comp_choice == 's':
            print(f'Rock smashes Scissor, You Won')
        elif comp_choice == 'p':
            print(f'Scissor cuts Paper, You Lost')
    elif player_choice == 'p':
        if comp_choice == 'r':
            print(f'Paper covers Rock , You Won')
        elif comp_choice == 's':
            print(f'Scissor cuts Paper, You Lost')
    elif player_choice == 's':
        if comp_choice == 'p':
            print(f'Scissor cuts Paper , You Won')
        elif comp_choice == 'r':
            print(f'Rock smashes Scissor, You Lost')
    choice = input("Do you want to keep playing !? Press y/n \n")
    if choice == 'y':
        rps()
    elif choice == 'n':
        exit()

rps()