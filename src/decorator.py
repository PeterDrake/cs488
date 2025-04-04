# Adapted from https://stackoverflow.com/a/309000/1435803

def logged(func):
    def f(*args, **kwargs):
        print('Starting ' + func.__name__)
        result = func(*args, **kwargs)
        print('Finishing ' + func.__name__)
        return result
    return f

@logged
def add(x, y):
    return x + y

print(add(2, 3))
