a = int(input("Enter a number(1-100): "))

for x in range(1, a+1):
    if (x % 3) == 0 and (x % 5) == 0:
        print(f"{x} fizzbuzz")
    elif (x % 3) == 0:
        print(f"{x} fizz")
    elif (x % 5) == 0:
        print(f"{x} buzz")
    else:
        print(x)

