print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
op= input("Enter number of the operation: ")
if op in ['1', '2', '3', '4']:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))

    if op == '1':
        c = a + b
        print(f"{a} + {b} = {c}")

    elif op == '2':
        c = a - b
        print(f"{a} - {b} = {c}")

    elif op == '3':
        c = a * b
        print(f"{a} * {b} = {c}")

    elif op == '4':
        if b != 0:
            c = a / b
            print(f"{a} / {b} = {c}")
        else:
            print("Zero is not valid")
else:
    print("Invalid input")
