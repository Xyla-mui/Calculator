#where the operators should b3
def output(string):
    print(string)
    return

def multiply(x, y):
    #Added function to enable me to safely convert string to numbers
    def to_numbers(value):
        if isinstance(value, (int, float)):
            return value
        
        if isinstance(value, str):
            value = value.strip()
            if value.replace('.','',1).replace('-','',1).isdigit():
                num = float(value)
                return int(num) if num.is_integer() else num
            else:
                raise ValueError(f"Invalid input: {value!r} is not numeric.")

        # If it's not a number or string at all
        raise ValueError(f"Invalid input type: {type(value).__name__}")

    x = to_numbers(x)
    y = to_numbers(y)

    return x * y

def divide(x, y):
    if y == 0:
        return "Error!: Division is Undefined"
    #Added function to enable me to safely convert string to numbers
    def to_numbers(value):
        if isinstance(value, (int, float)):
            return value
        
        if isinstance(value, str):
            value = value.strip()
            if value.replace('.','',1).replace('-','',1).isdigit():
                num = float(value)
                return int(num) if num.is_integer() else num
            else:
                raise ValueError(f"Invalid input: {value!r} is not numeric.")

        # If it's not a number or string at all
        raise ValueError(f"Invalid input type: {type(value).__name__}")

    x = to_numbers(x)
    y = to_numbers(y)

    return x / y
