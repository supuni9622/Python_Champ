try:
    age = int(input('Enter your age: '))
    income = 20000
    risk = income/age
    print(age)
    print(risk)
except ValueError:
    print('Invalid input')
except ZeroDivisionError:
    print('Age cannot be zero')





