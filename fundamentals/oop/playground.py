
class foo():
    def __init__(self, name):
        foo.name = name
        foo.num = boo(45)
class boo():
    def __init__(self, number):
        boo.number = number

my_foo = foo("mines")


print(my_foo.name + " " + str(foo.num.number))