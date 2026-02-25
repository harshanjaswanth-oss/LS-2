
base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))

i = 1
for _ in range(exp):
    i = i * i

print("Result:", i)
