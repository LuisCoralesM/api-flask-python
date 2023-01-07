def myFunc(*args):
    print(args)
    for arg in args:
        print(arg)


myFunc(2)

myFunc(1, 2, 3)


def myFunc2(**kwargs):
    print(kwargs)
    for arg in kwargs:
        print(arg)


myFunc2(x=1, y=2, z=3)
