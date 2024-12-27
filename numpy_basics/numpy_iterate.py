import numpy as np

def numpy_iterate(arr):
    if arr.size == 0:
        print('Empty array')
    elif isinstance(arr, np.ndarray):
        for value in np.nditer(arr):
            print(value)
    else:
        raise TypeError('arr must be np.ndarray')

def numpy_enumerate(arr):
    if arr.size == 0:
        print('Empty array')
    elif isinstance(arr, np.ndarray):
        for index, value in np.ndenumerate(arr):
            print(index, value)
    else:
        raise TypeError('arr must be np.ndarray')


if __name__ == '__main__':
    arr_1 = np.random.randint(1,100, size=(10,10,5))
    print(arr_1)
    print(arr_1.ndim)
    print("*" * 40)
    numpy_iterate(arr_1)
    print()
    numpy_enumerate(arr_1)
    print("*"*40)
    #using for loop
    for i in arr_1:
        for j in i:
            for k in j:
                print(k)

    #check nDim == 0
    print("*" * 40)
    arr_zero = np.array([])
    numpy_iterate(arr_zero)
    numpy_enumerate(arr_zero)

