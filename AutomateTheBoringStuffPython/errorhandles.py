def div2by(divideBy):
    try:
        return 2 / divideBy
    except ZeroDivisionError:
        print('Error: Cannot divide by zero.')


print(div2by(2))
print(div2by(0))
print(div2by(1))
