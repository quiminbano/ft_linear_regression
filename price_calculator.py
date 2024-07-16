

def main():
    try:
        number = float(input("Enter a value of mileage \
to calculate the price:\n"))
        theta0 = float(input("Enter a value of theta0:\n"))
        theta1 = float(input("Now, enter a value of theta1:\n"))
        result = theta0 + (theta1 * number)
        assert result == result, "An error ocurred during the calculation."
    except (EOFError, ValueError, OverflowError, AssertionError) as e:
        print(e)
        exit(1)
    print(f"The predicted value of price per mileage is {result}.")


if __name__ == '__main__':
    main()
