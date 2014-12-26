def divisible_by_three(number):
    return divisible_by(3, number)

def divisible_by_five(number):
    return divisible_by(5, number)

def divisible_by_fifteen(number):
    return divisible_by(15, number)

def divisible_by(divisor, number):
    return number % divisor == 0

def play(number):
    if divisible_by_fifteen(number):
        return "FissBuss"
    if divisible_by_three(number):
        return "Fiss"
    if divisible_by_five(number):
        return "Buss"
