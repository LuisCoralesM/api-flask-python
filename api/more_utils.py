def GeneratorFunction():
    yield "Hola"
    yield "Mundo"
    yield "!"


x = GeneratorFunction()

print(next(x))
print(next(x))
print(next(x))

print("FIBONACCI")


def fib(limit):
    a, b = 0, 1

    while a < limit:
        yield a
        a, b = b, a + b


print("Using for in loop")

for i in fib(10):
    print(i)


class IteratorClass:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.x = 0
        return self

    def __next__(self):
        x = self.x

        if x > self.limit:
            raise StopIteration

        self.x = x + 1
        return x


def GeneratorCounter(limit):
    a = 0

    while a <= limit:
        yield a
        a += 1


a = GeneratorCounter(10)

for i in a:
    print(i)


tuple = ('a', 'b', 'c', 'd', 'e')

tuple_iter = iter(tuple)

# print("Inside loop:")
# for index, item in enumerate(tuple_iter):
#     print(item)

#     if index == 2:
#         break

# print("Outside loop:")
# print(next(tuple_iter))
# print(next(tuple_iter))

print("--------")
for i in IteratorClass(10):
    print(i)
