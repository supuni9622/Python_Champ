# Use dictionaries when we need to store data as key:value pairs
# Each key should be unique in the dictionary

customer = {
    'name': 'Supuni Manamperi',
    'age': 29,
    'is_verified': True
}

print(customer)
print(customer['name'])
# When we try to print a value by accessing a undefined key it will give a error
# print('birthDay')

print(customer.get('name'))
# But if we try to access it using get method it will give none which represent inavailability of data instead of error message
print(customer.get('birthDay'))
# We can define a default value if needed
print(customer.get('birthDay', 'Jan 29'))

# Updating the existing keys and adding new keys
customer['name'] = 'Nipuni Manamperi'
print(customer)
customer['university'] = 'UoK'
print(customer)

number_dictionary = {
    '0': 'Zero',
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine'
}

phone_number = input('Enter your phone number: ')
output = ''
for number in phone_number:
    output += number_dictionary[number] + ' '
    print(number_dictionary[number])
print(output)



