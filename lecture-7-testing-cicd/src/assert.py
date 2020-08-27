def square(x):
    return x*x

print(square(10) == 100)

print(square(10) == 101)

assert(square(10) == 100)

def square2(x):
    return x+x

assert(square2(10) == 100)