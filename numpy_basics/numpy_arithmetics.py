import numpy as np


def add_arrays(array1:np.ndarray, array2:np.ndarray)-> np.ndarray:
    return np.add(array1, array2)


def subtract_arrays(array1, array2):
    return np.subtract(array1, array2)


def multiply_arrays(array1, array2):
    return np.multiply(array1, array2)


def divide_arrays(array1, array2):
    return np.divide(array1, array2)


def square_arrays(array1, array2):
    return np.square(array1), np.square(array2)


def get_maximum(array):
    return np.max(array)


def get_minimum(array):
    return np.min(array)


def sqrt(array):
    return np.sqrt(array)


if __name__ == '__main__':
    array1 = np.array([1, 2, 3, 4, 5])
    array2 = np.array([1, 2, 3, 4, 5])
    print(f"add 2 arrays: {add_arrays(array1, array2)}")
    print(f"subtract 2 arrays: {subtract_arrays(array1, array2)}")
    print(f"multiply 2 arrays: {multiply_arrays(array1, array2)}")
    print(f"divide 2 arrays: {divide_arrays(array1, array2)}")
    print(f"square 2 arrays: {square_arrays(array1, array2)}")
    print(f"get_maximum: {get_maximum(array1)}")
    print(f"get_minimum: {get_minimum(array1)}")
    print(f"square root: {sqrt(array2)}")
