

def add(x, y):
    # Returns the sum of x and y
    return x + y

def isequal(x, y):
    # Returns True if x is equal to y, otherwise False
    return x == y

def islessthan(x, y):
    # Returns True if x is less than y, otherwise False
    return x < y

def optimise_multiplication(a, b):
    if isequal(a, 0):
        return 0
    if isequal(b, 0):
        return 0
    if isequal(a, 1):
        return b
    if isequal(b, 1):
        return a

    if islessthan(a, b):
        temp = a
        a = b
        b = temp

    counter = 1
    prod = 0

    while islessthan(counter,b):
        tempc = 1
        tempp = a
        while islessthan(add(counter,tempc),b) or isequal(add(counter,tempc),b):
            counter = add(counter,tempc)
            prod = add(prod,tempp)
            tempc = add(tempc,tempc)
            tempp = add(tempp,tempp)

    return add(prod,a)


if __name__ == "__main__":
    # Example usage
    print(optimise_multiplication(3, 4))
