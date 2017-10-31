import random


def with_chance(chance, value):
    def decorator(func):
        try:
            if hasattr(func, '__call__')==False:
                raise AttributeError
        except AttributeError:
            print("This is not a function")
        def wrapper(*args,**kwarg):
            print(chance)
            x = random.randint(1, 99)
            print(x)
            if x <= chance:
                func()
            else:
                if value != None:
                    print(value)
                else:
                    raise Exception("You havent entered Default Value!")
        return wrapper
    return decorator


#@with_chance(50,"Default Value")
def some_fn(*args,**kwargs):
    print("function")

some_fn = with_chance(50,"Default Value")(some_fn)




if __name__ == '__main__':
    some_fn()
