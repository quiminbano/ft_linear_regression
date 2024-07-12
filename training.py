import pandas as pd
from pandas.errors import EmptyDataError
from pandas.errors import ParserError
from sklearn.linear_model import LinearRegression


def test_sklearn(x, y):
    model = LinearRegression()
    model.fit(X=x, y=y)
    print(f"Valor theta0: {model.intercept_}, theta1: {model.coef_}")


def normalize_array(array):
    temp = (array - min(array)) / (max(array) - min(array))
    return temp


def get_coeficients(km_x, price_y, iter):
    m = price_y.size
    learning_rate = 0.01
    theta0 = 0
    theta1 = 0
    for i in range(0, iter):
        y_predicted = theta0 + (theta1 * km_x)
        delta_err = y_predicted - price_y
        theta0 -= learning_rate * ((sum(delta_err) / m))
        theta1 -= learning_rate * ((sum(delta_err * km_x) / m))
    return [theta0, theta1]


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
    normalized_y = normalize_array(price_y)
    thetas = get_coeficients(km_x=normalized_x,
                             price_y=normalized_y, iter=1000)
    print(f"The value of theta0 is {thetas[0]}, and the value of theta1 \
is {thetas[1]}")
    test_sklearn(data_set["km"].values.reshape(-1, 1), data_set["price"].values.reshape(-1,1))


if __name__ == '__main__':
    main()
