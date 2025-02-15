def add(*args):
    r = 0
    for n in args:
        r += n
    return r


print(add(1, 5, 7, 8, 5))


def calculate(n, **kwargs):
    # for key, value in kwargs.items()
    # print(key)
    # print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        # you can call kwargs directly, but if the value does not exists, there is an exception
        # self.make = kw["make"]
        # If we use get and the keyword does not exist, the value will be None
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Nissan", model="GT-R")

print(my_car.model)
