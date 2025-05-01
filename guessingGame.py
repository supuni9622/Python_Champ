secret_number = 9
input_time = 0
input_limit = 3

while input_time < input_limit:
    input_number = int(input("Enter a number between 1 and 10: "))
    input_time += 1

    if secret_number == input_number:
        print('You got it right!')
        break
else:
    print('Sorry! You failed!')
