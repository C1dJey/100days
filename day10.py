
#test
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
# print(is_leap_year(1989))

# Calculator
def add(n1,n2):
    return n1 +n2
def mult(n1,n2):
    return n1 * n2
def sub(n1,n2):
    return n1 - n2
def div(n1,n2):
    return n1 / n2
def calculator():
    op = {
        "+": add, 
        "*": mult, 
        "-": sub, 
        "/": div} 
    continue_calc = True
    result = 0
    n1 = float(input("Whats te first number: "))
    while continue_calc:
        symbol = input("Operation :")
        n2 = float(input("Whats te second number: "))
        if symbol in op:
            result = op[symbol](n1, n2)
        else:
            print("Havent this operation")
        print(result)
        again = input("another number ?: ")
        if again == "n":
            continue_calc = False
            print("\n"*20)
        else:
            n1 = result

while True:
    calculator()