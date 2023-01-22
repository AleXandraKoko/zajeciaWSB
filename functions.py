def add(x, y):
    return x + y

def multiply(x, y):
    return x * y



def  fissbuzz(number):
    if isinstance(number, (int, float))and number > 0:
        number = round(number)
        if number % 3 == 0 and number % 5 == 0:
            return 'fissbuzz'
        elif number % 3 == 0:
            return 'fiss'
        elif number % 5 == 0:
            return 'buzz'
        else:
            return number
    else:
        return 0