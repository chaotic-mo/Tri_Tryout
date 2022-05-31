def addition(number1, number2):
    print(number1, "+", number2, "= ", end='')
    return number1 + number2
print(addition(10, 12))

def subtraction(number1, number2):
    print(number1, "-", number2, "= ", end='')
    return number1 - number2

print(subtraction(58, 34))

def multiplucation(number1, number2):
    print(number1, "*", number2, "= ", end='')
    return number1 * number2

print(multiplucation(6, 7))

def devison(number1, number2):
    print(number1, "/", number2, "= ", end='')
    return f'{number1 / number2:.0f}'

print(devison(144, 12))

def increment(number, i):
    print(number, "+", i, "= ", end='')
    return number + i

print(increment(12, 1))

def decrement(number, i):
    print(number, "-", i, "= ", end='')
    return number - 1

print(decrement(34, 1))