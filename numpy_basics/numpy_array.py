from array import array

import numpy as np




def get_ndim(array: np.ndarray) -> int:
    return array.ndim


def get_size(array: np.ndarray) -> int:
    return array.size


def get_shape(array: np.ndarray) -> tuple:
    return array.shape


def get_dtype(array: np.ndarray) -> np.dtype:
    return array.dtype


if __name__ == "__main__":
    print("1D Array")
    arr = np.array([1, 2, 3])
    print(arr)
    print(get_ndim(arr))
    print(get_size(arr))
    print(get_shape(arr))
    #  2D array
    print("\n2D Array")
    arr2 = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8], ])
    print(arr2)
    print(get_ndim(arr2))
    print(get_size(arr2))
    print(get_shape(arr2))

    # 3D array
    print("\n3D Array")
    arr3 = np.array([
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    ])
    print(arr3)
    print(get_ndim(arr3))
    print(get_size(arr3))
    print(get_shape(arr3))