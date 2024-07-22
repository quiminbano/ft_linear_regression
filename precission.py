import numpy as np
from utils.read_file_thetas import get_thetas
from utils.open_database import open_database


def get_R2(price_y, y_predicted):
    size = price_y.size
    mean_y = (sum(price_y) / size)
    ssr = sum((price_y - y_predicted) ** 2)
    sst = sum((price_y - mean_y) ** 2)
    if sst != 0:
        r2 = (1 - (ssr / sst))
    else:
        assert sum(price_y) == mean_y * size, "An error ocurred doing the \
calculations"
        r2 = 1
    return r2


def main():
    try:
        km_x, price_y = open_database()
        assert max(km_x) - min(km_x) != 0, "An error ocurred \
doing the calculations"
        thetas = get_thetas()
        y_predicted = thetas[0] + (thetas[1] * km_x)
        assert np.all(np.isfinite(y_predicted)), "An error ocurred \
doing the calculations"
        data_ammount = price_y.size
        mse = (sum((price_y - y_predicted) ** 2) / data_ammount)
        rmse = (mse ** 0.5)
        r2 = get_R2(price_y, y_predicted)
        print(f"Value of mean squared error (mse): {mse}")
        print(f"Value of mean squared error (rmse): {rmse}")
        print(f"Value of correlation coefficient (r2): {r2}")
    except (ValueError, OverflowError, AssertionError) as e:
        print(e)
        exit(1)


if __name__ == '__main__':
    main()
