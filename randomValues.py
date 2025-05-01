import random

for i in range(3):
    print(random.random())

for i in range(3):
    print(random.randint(10,43))

members = ['John', 'Henry', 'James']
leader = random.choice(members)
print(leader)