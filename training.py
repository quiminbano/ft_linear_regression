import pandas as pd
from pandas.errors import EmptyDataError
from pandas.errors import ParserError


def get_corrected_thetas(prev_thetas, Xmin, Xmax):
    Ymin = prev_thetas[0]
    Ymax = prev_thetas[0] + prev_thetas[1]
    new_theta1 = (Ymax - Ymin) / (Xmax - Xmin)
    new_theta0 = (Ymin - (new_theta1 * Xmin))
    return [new_theta0, new_theta1]


def get_coeficients(km_x, price_y, iter):
    m = price_y.size
    learning_rate = 0.1
    theta0 = 0
    theta1 = 0
    for i in range(0, iter):
        y_predicted = theta0 + (theta1 * km_x)
        delta_err = y_predicted - price_y
        theta0 -= learning_rate * ((sum(delta_err) / m))
        theta1 -= learning_rate * ((sum(delta_err * km_x) / m))
    return [theta0, theta1]


def normalize_array(array):
    temp = (array - min(array)) / (max(array) - min(array))
    return temp


def main():
    try:
        data_set = pd.read_csv("data.csv")
    except (FileNotFoundError, EmptyDataError, ParserError,
            PermissionError) as e:
        print(e)
        exit(1)
    price_y = data_set["price"].values
    km_x = data_set["km"].values
    normalized_x = normalize_array(km_x)
    prev_thetas = get_coeficients(km_x=normalized_x,
                             price_y=price_y, iter=1000)
    corrected_thetas = get_corrected_thetas(prev_thetas, min(km_x), max(km_x))
    print(corrected_thetas[0], corrected_thetas[1])


if __name__ == '__main__':
    main()
