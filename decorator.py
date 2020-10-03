def my_func():
    print("Hello")


my_func()
greet = my_func
del my_func
greet()


def my_func(func):
    def my_inside_func():
        print("I'm inside my_func function")
    func()
    return my_inside_func


my_func(greet)


def my_decorator(func):
    def wrap_func():
        print("Before code!")
        func()
        print("After code!")
    return wrap_func


@my_decorator
def my_original_func():
    print("Original Function!")


my_original_func()


