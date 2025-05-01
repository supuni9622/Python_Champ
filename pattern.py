numbers = [5, 2, 5, 2, 2]

# Python specific way
for number in numbers:
    print(number*'*')

# In other programming languages and using nested loops
for number in numbers:
    output = ''
    for count in range(number):
        output += 'x'
    print(output)

number_list_2 = [2,2,2,2,8]

for number in number_list_2:
    print(number*'*')

for number in number_list_2:
    output = ''
    for count in range(number):
        output += 'x'
    print(output)


