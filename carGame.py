user_input = input("< ").upper()
prev_input = ''

while user_input != 'QUIT':

    if user_input == "HELP":
        print('''
Start: To start the car
Stop: To stop the car
Quit: To quit the program
        ''')
    elif user_input == "START":
        if prev_input == user_input:
            print("You have already started the car!")
        else:
            print('Car started..')
    elif user_input == "STOP":
        if prev_input == user_input:
            print("You have already stopped the car!")
        else:
            print('Car stopped..')
    else:
        print('Invalid input')

    prev_input = user_input
    user_input = input("< ").upper()



