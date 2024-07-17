from read_file_thetas import get_thetas

def get_numbers():
    try:
        print("Please, introduce the value of mileage to predict the price:")
        number = float(input(""))
    except EOFError:
        raise EOFError("Aborted mission!! Thanks for using the program.")
    except (ValueError, OverflowError):
        raise ValueError("The input introduced is invalid!!")
    return number


def main():
    try:
        number = get_numbers()
        thetas = get_thetas()
        result = thetas[0] + (thetas[1] * number)
        assert result == result, "An error ocurred during the calculation."
    except (EOFError, ValueError, OverflowError, AssertionError) as e:
        print(e)
        exit(1)
    print(f"The predicted value of price per mileage is {result}.")


if __name__ == '__main__':
    main()
