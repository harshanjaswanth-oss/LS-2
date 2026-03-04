
base = float(input("Enter the base number: "))
exponent = int(input("Enter the exponent (integer): "))


result = 1
if exponent >= 0:
    for i in range(exponent):
        result = result * base
else:
    for i in range(-exponent):
        result = result * base
    result = 1 / result


print("Result:", result)


