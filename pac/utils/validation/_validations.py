from ..convertions import check_convert_data


def check_categorical_data(X):
    return True


def checks_data(X, y):
    if not check_convert_data(X, y):
        raise ValueError("Not valid data type")

    if not check_categorical_data(X):
        raise ValueError("Not Categorical Data used in X")

    if not check_categorical_data(y):
        raise ValueError("Not Categorical Data used in y")