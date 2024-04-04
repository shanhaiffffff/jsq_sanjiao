import math

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def degrees_to_radians(degrees):
    return degrees * (math.pi / 180)

def radians_to_degrees(radians):
    return radians * (180 / math.pi)

def sin_taylor(degrees, n):
    radians = degrees_to_radians(degrees)
    result = 0
    for i in range(n):
        coef = (-1) ** i
        term = coef * (radians ** (2 * i + 1)) / factorial(2 * i + 1)
        result += term
    return result

def cos_taylor(degrees, n):
    radians = degrees_to_radians(degrees)
    result = 0
    for i in range(n):
        coef = (-1) ** i
        term = coef * (radians ** (2 * i)) / factorial(2 * i)
        result += term
    return result

def arcsin_taylor(x, n):
    result = 0
    for i in range(n):
        coef = factorial(2 * i) / (4 ** i * factorial(i) ** 2 * (2 * i + 1))
        term = coef * (x ** (2 * i + 1))
        result += term
    return radians_to_degrees(result)

def arctan_taylor(x, n):
    result = 0
    for i in range(n):
        coef = (-1) ** i
        term = coef * (x ** (2 * i + 1)) / (2 * i + 1)
        result += term
    return radians_to_degrees(result)

def main():
    print("Welcome to Calculator!")
    while True:
        print("\n1. sin(x)\n2. cos(x)\n3. arcsin(x)\n4. arctan(x)\n5. Exit")
        choice = input("Please select an option: ")

        if choice == '5':
            print("Goodbye!")
            break

        try:
            x = float(input("Enter x in degrees: "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        try:
            n = int(input("Enter number of terms in Taylor series: "))
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
            continue

        if choice == '1':
            print("sin({}) ≈ {:.6f}".format(x, sin_taylor(x, n)))
        elif choice == '2':
            print("cos({}) ≈ {:.6f}".format(x, cos_taylor(x, n)))
        elif choice == '3':
            if abs(x) > 1:
                print("Invalid input! arcsin(x) is only defined for |x| <= 1.")
            else:
                print("arcsin({}) ≈ {:.6f}".format(x, arcsin_taylor(x, n)))
        elif choice == '4':
            print("arctan({}) ≈ {:.6f}".format(x, arctan_taylor(x, n)))
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
