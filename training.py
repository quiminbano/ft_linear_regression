import matplotlib.pyplot as plt
import numpy as np
from utils.open_database import open_database


def set_cost_plot(cost, iter, object):
    n_cycles = list(range(1, iter + 1))
    object.scatter(n_cycles, cost)
    object.set_title("Error cost vs Number of iterations cycles")
    object.set_xlabel("Number of iteration cycles")
    object.set_ylabel("Error cost (a.u$^{2}$)")
    object.plot(n_cycles, cost)


def set_regression_plot(thetas, km, price, object):
    price_predicted = thetas[0] + (thetas[1] * km)
    object.scatter(x=km, y=price, label="Real price")
    object.set_title("Price vs mileage")
    object.set_xlabel("Mileage (km)")
    object.set_ylabel("Price (a.u)")
    object.plot(km, price_predicted, color="red", label="Predicted price")
    object.legend()


def get_corrected_thetas(prev_thetas, Xmin, Xmax):
    Ymin = prev_thetas[0]
    Ymax = prev_thetas[0] + prev_thetas[1]
    new_theta1 = (Ymax - Ymin) / (Xmax - Xmin)
    new_theta0 = (Ymin - (new_theta1 * Xmin))
    return [new_theta0, new_theta1]


def get_coeficients(km_x, price_y, iter):
    m = price_y.size
    learning_rate = 0.1
    temp_theta0 = 0
    temp_theta1 = 0
    cost_history = np.zeros(iter)
    thetas = np.zeros(2)
    for i in range(0, iter):
        y_predicted = thetas[0] + (thetas[1] * km_x)
        delta_err = y_predicted - price_y
        cost_history[i] = (((sum(delta_err) * -1) ** 2) / (2 * m))
        temp_theta0 = learning_rate * ((sum(delta_err) / m))
        temp_theta1 = learning_rate * ((sum(delta_err * km_x) / m))
        thetas[0] -= temp_theta0
        thetas[1] -= temp_theta1
        assert np.all(np.isfinite(cost_history)), "Error processing the data!"
        assert np.all(np.isfinite(thetas)), "Error processing the data!"
    return thetas.tolist(), cost_history.tolist()


def normalize_array(array):
    if (max(array) - min(array) == 0):
        raise ZeroDivisionError("The data provided in the dataset is invalid.")
    temp = (array - min(array)) / (max(array) - min(array))
    return temp


def main():
    try:
        km_x, price_y = open_database()
        normalized_x = normalize_array(km_x)
        prev_thetas, cost_history = get_coeficients(km_x=normalized_x,
                                                    price_y=price_y, iter=1000)
    except (AssertionError, ZeroDivisionError) as e:
        print(e)
        exit(1)
    corrected_thetas = get_corrected_thetas(prev_thetas, min(km_x), max(km_x))
    theta0 = corrected_thetas[0]
    theta1 = corrected_thetas[1]
    print(f"The value of theta0 is {theta0} \
and the value of theta1 is {theta1}")
    fig, graph_objects = (plt.subplots(1, 2, figsize=(13, 5)))
    fig.subplots_adjust(wspace=0.5)
    set_regression_plot(corrected_thetas, km_x, price_y, graph_objects[0])
    set_cost_plot(cost_history, 1000, graph_objects[1])
    file = open("result_thetas.txt", "w")
    file.write(f"{theta0},{theta1}")
    file.close()
    plt.show()


if __name__ == '__main__':
    main()
