from utils.open_database import open_database
from sklearn.linear_model import LinearRegression


def main():
    try:
        km_x, price_y = open_database()
        regression = LinearRegression()
        regression.fit(km_x.reshape(-1, 1), price_y.reshape(-1, 1))
        theta0 = regression.intercept_
        theta1 = regression.coef_
        print(f"The value of theta0 is {theta0} \
and the value of theta1 is {theta1}")
    except (AssertionError, ZeroDivisionError) as e:
        print(e)
        exit(1)


if __name__ == '__main__':
    main()
