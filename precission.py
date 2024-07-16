import pandas as pd
import numpy as np
from pandas.errors import EmptyDataError
from pandas.errors import ParserError


def get_R2(price_y, y_predicted):
    size = price_y.size
    mean_y = (sum(price_y) / size)
    ssr = sum((price_y - y_predicted) ** 2)
    sst = sum((price_y - mean_y) ** 2)
    r2 = (1 - (ssr / sst))
    return r2

def main():
    try:
        data_set = pd.read_csv("data.csv")
        price_y = data_set["price"].values
        km_x = data_set["km"].values
        theta0 = float(input("Enter the value of theta0:\n"))
        theta1 = float(input("Now, enter the value of theta1:\n"))
        y_predicted = theta0 + (theta1 * km_x)
        assert np.all(np.isfinite(y_predicted)), "An error ocurred \
doing the calculations"
        data_ammount = price_y.size
        mse = (sum((price_y - y_predicted) ** 2) / data_ammount)
        rmse = (mse ** 0.5)
        r2 = get_R2(price_y, y_predicted)
        print(f"Value of r2: {r2}")
    except (FileNotFoundError, EmptyDataError, ParserError,
            PermissionError, ValueError, OverflowError,
            AssertionError, EOFError) as e:
        print(e)
        exit(1)


if __name__ == '__main__':
    main()
