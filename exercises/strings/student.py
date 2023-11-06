def greet(name):
    return f"Hello, {name}!"

def format_position(x, y):
    return f"({x:.3f}, {y:.3f})"

def interactive_greet():
    name= input("What is your name?")
    print(greet(name))

def tip_calculator():
    total_price = int(input('Enter total price: '))
    tip_percentage = input("Enter tip percentage (default=20): ")
    if len(tip_percentage) == 0:
        tip_percentage = 20
    else:
        tip_percentage = int(tip_percentage)
    total = round(total_price * (1 + tip_percentage / 100))
    print(f'You have to pay {total}')
    
def last_character(string):
    if len(string) != 0:
        return string [len(string) -1]
    else:
        return None
