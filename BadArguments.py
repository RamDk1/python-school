class NonIntAgumentError(Exception):
    pass

def handleNonIntArgument(func):
    def wrapper(*args):
        for arg in args:
            if type(arg) is not int:
                raise NonIntAgumentError(f"{arg} is not an integer")
        return func(*args)
    return wrapper

@handleNonIntArgument
def add(a, b):
    return a+b
print(add(5, 'hola'))
