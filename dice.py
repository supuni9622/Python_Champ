import random
from pathlib import Path

class Dice:
    def roll(self):
        first_roll = random.randint(1, 6)
        second_roll = random.randint(1, 6)
        dice_result = (first_roll, second_roll)
        return dice_result

dice_numbers =Dice().roll()
print(dice_numbers)

path = Path('ecommerce')
isPath = path.exists()
print(isPath, path)

#create a new directory
email_path = Path('email')
email_path.mkdir(parents=True, exist_ok=True)
#remove directory
#email_path.rmdir()

# Get all the files in current directory
path = Path()
print(path.glob('*.*'))
print(path.glob('*.txt'))

for file in path.glob('*.*'):
    print(file)

print('-----------------------------------')
# Get all the directories and files in current directory
for directory in path.glob('*'):
    print(directory)
