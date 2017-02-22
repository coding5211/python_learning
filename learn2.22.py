"""
age = 20
name = "Swaroop"
print("{0} was {1} years old when he wrote this book".format(name,age))
print("why is {0} playing with that python?".format(name))
print("{0:.3f}".format(1.0/3))
print("{0:_^11}".format("hello"))
print("{name} wrote {book}".format(name="Swaroop",book="A byte of Python"))
print("a",end=" ")
print("b",end=" ")
print("c")


i = 5
print(i)
i = i + 1
print(i)

s = This is a multi-line string.
this is the second line.
print(s)

length = 5
breadth = 2
area = length * breadth
print("Area is",area)


number = 23
running = True
while running:
    guess = int(input("Enter an integer:"))
    if guess == number:
        print("Yes")
        running = False
    elif guess < number:
        print("small")
    else:
        print("big")
else:
    print("looping")
print("done")


for i in range(1,5):
    print(i)
else:
    print("the for loop is over")

"""


def say_hello():
    print("hello world")


def print_max(a, b):
    if a > b:
        print(a, "is maximum")
    elif a == b:
        print(a, "is equal to", b)
    else:
        print(b, "is maximum")


print_max(3, 4)
x = 50
y = 7
print_max(x, y)


def func():
    global x

    print("x is ", x)
    x = 2
    print("Changed local x to ", x)


func()
print("x is still", x)


def say(message, times=2):
    print(message * times)


say("hello")
say("hello", 5)


def funmun(a, b=5, c=10):
    print("a is", a, "and b is ", b, "and c is", c)


funmun(3, 7)
funmun(25, c=24)
funmun(c=50, a=100)


def total(aa=5, *numbers, **phonebook):
    print("aa", aa)
    for single_item in numbers:
        print("single_item", single_item)
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)


print(total(10, 1, 2, 3, jack=1123, rose=2233, tom=123))


def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return x
    else:
        return y


print(maximum(2, 3))


def maxcu(xx,yy):
    """Hello.
     world."""
    xx = int(xx)
    yy = int(yy)
    if xx>yy:
        print(xx,"x is max")
    else:
        print(yy,"y is max")

maxcu(3,5)
print(maxcu.__doc__)
