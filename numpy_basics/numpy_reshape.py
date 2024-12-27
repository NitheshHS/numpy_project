import numpy as np

def reshape(arr:np.ndarray, shape:tuple)->np.ndarray:
    return np.reshape(arr, shape)

if __name__ == '__main__':
    array = np.array([1,2,3,4,5,6])
    print(reshape(array, (3,2)))
    print(reshape(array, (2,3)))
    print('\n')
    array_1 = np.array([[1, 2, 3],
                        [4, 5, 6]])
    print(reshape(array_1, (1,6)))
    print(reshape(array_1, (6, 1)))
    print(reshape(array_1, (3, 2)))