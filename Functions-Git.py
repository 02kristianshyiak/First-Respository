# 4.13.3: Greetings
# Kristian Shyiak
# 2.5.19


name = input("What is your name: ")

def greeting():
    print("Hi there " + name + "!")
    print("Nice to meet you")

greeting()


# 4.13.4: Functions and Variables
# Kristian Shyiak
# 2.11.19

x = 406

def print_something():
    x = 3
    print('\n', x)

print('\n', x)
print_something()


# 4.13.6: Functions and Variables, Part 3
# Kristian Shyiak
# 2.18.19


def print_number(x):
    print('\n', x)

print_number(13)
print_number(23)


# 4.14.4: Name & Age
# Kristian Shyiak
# 2.18.19

def name_and_age(name, age):
    print('\n', 'Hi, my name is', name, 'and I am', age, 'years old!')

name_and_age('Kristian', 33)
name_and_age('Kristian', 18)