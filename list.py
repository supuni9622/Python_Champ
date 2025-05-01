number_list = [1,2,3,4,5, 3, 10,1]

# find the max number

max_number=number_list[0]
for number in number_list:

    if max_number < number:
        max_number = number
print(max_number)

# 2D list

matrix = [
    [1,3,4],
    [2,5,6],
    [7,8,9]
]

print(matrix)
print(matrix[1])
print(matrix[1][1])
matrix[1][1] = 20
print(matrix)

for row in matrix:
    for col in row:
        print(col)