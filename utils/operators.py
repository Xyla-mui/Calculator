# where the operators should b3
def output(string):
    print(string)
    return


def to_numbers(value):
    if isinstance(value, (int, float)):
        return value

    if isinstance(value, str):
        value = value.strip()
        if value.replace('.', '', 1).replace('-', '', 1).isdigit():
            num = float(value)
            return int(num) if num.is_integer() else num
        else:
            raise ValueError(f"Invalid input: {value!r} is not numeric.")

    # If it's not a number or string at all
    raise TypeError(f"Invalid input type: {type(value).__name__}")

def add(x, y):
    x = to_numbers(x)
    y = to_numbers(y)
    return x + y

def multiply(x, y):
    # Added function to enable me to safely convert string to numbers
    x = to_numbers(x)
    y = to_numbers(y)

    return x * y


def divide(x, y):
    if y == 0:
        return "Error!: Division is Undefined"

    x = to_numbers(x)
    y = to_numbers(y)

    return x / y
# modulus remainder of division


def modulus(x, y):
    if y == 0:
        return ZeroDivisionError
    if isinstance(x,str) or isinstance(y,str):
        return ValueError
    x = to_numbers(x)
    y = to_numbers(y)
    return x % y
