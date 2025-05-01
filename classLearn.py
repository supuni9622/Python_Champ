class Point:
    #constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print('Moving')
    def draw(self):
        print('Drawing')


point1 = Point(10,30)
point1.move()
print(point1.x, point1.y)
point1.x = 11
print(point1.x, point1.y)

class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f'Hello, I am {self.name}')

nipuni = Person('Nipuni')
nipuni.talk()

# Inheritance - Get all the methods from parent class

class Mammal:
    def walk(self):
        print('walking')

class Dog(Mammal):
    def bark(self):
        print('barking')

class Cat(Mammal):
    def meow(self):
        print('meowing')

class Elephant(Mammal):
    pass

my_dog = Dog()
my_dog.walk()
my_cat = Cat()
my_cat.walk()
my_dog.bark()
my_cat.meow()
my_elephant = Elephant()
my_elephant.walk()


def add(a, b):
    print(a + b)

