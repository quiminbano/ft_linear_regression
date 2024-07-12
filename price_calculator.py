

def main():
    theta0 = float(0)
    theta1 = float(0)
    try:
        number = float(input("Enter a value of mileage \
to calculate the price:\n"))
        result = theta0 + (theta1 * number)
        if number != number or result != result:
            raise AssertionError("An error ocurred during the calculation.")
    except (EOFError, ValueError, OverflowError, AssertionError) as e:
        print(e)
        exit(1)
    print(f"The predicted value of price per mileage is {result}.")


if __name__ == '__main__':
    main()
