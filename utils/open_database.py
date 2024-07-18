import pandas as pd
import numpy as np
from pandas.errors import EmptyDataError
from pandas.errors import ParserError


def validate_data(data_set):
    bool_check = data_set.ndim == 2 and data_set.shape[1] == 2
    assert bool_check is True, "The ammount of categories in data.csv \
file is incorrect!!"
    try:
        km = data_set["km"]
    except KeyError:
        raise AssertionError("The dataset contained in data.csv file does not \
have data about the mileage in km!")
    try:
        price = data_set["price"]
    except KeyError:
        raise AssertionError("The dataset contained in data.csv file does not \
have data about the price!")
    km_values = km.values
    price_values = price.values
    type_list = ["f", "i"]
    assert km_values.dtype.kind in type_list, "Some part of the data is \
invalid for mileage(km)!"
    assert price_values.dtype.kind in type_list, "Some part of the data is \
invalid for prices!"
    assert np.all(np.isfinite(km_values)), "Some part of the data is invalid \
for mileage(km)!"
    assert np.all(np.isfinite(price_values)), "Some part of the data is \
invalid for prices!"
    return km_values, price_values


def open_database():
    try:
        data_set = pd.read_csv("data.csv")
        km, price = validate_data(data_set)
    except EmptyDataError:
        raise AssertionError("The csv file provided is empty!")
    except ParserError:
        raise AssertionError("An error ocurred trying to parse the \
information from the csv file!")
    except FileNotFoundError:
        raise AssertionError("The data.csv file was not found in the \
execution folder!")
    except PermissionError:
        raise AssertionError("The file data.csv provided does not have \
reading permissions!")
    except AssertionError as e:
        raise AssertionError(e)
    return km, price
