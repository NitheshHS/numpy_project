import numpy as np

if __name__ == '__main__':
    array_1 = np.array([1, 2, 3,11,13,1,3,2,8,19,22,13])
    indices = np.where(array_1 > 4)
    values = array_1[indices]

    print("Indices:", indices)
    print("Values:", values)
    print("sorted: ", np.sort(array_1))
    array_2 = np.array([[1,12,2],[9,8,7]])
    print("sorted: ", np.sort(array_2))
    print("shuffle: ", np.random.shuffle(array_2))
    print("unique:", np.unique(array_2))
    x = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print("flatten x: ", x.flatten())
    print("reverse x: ", np.flip(x))
    print("ravel x: ", x.ravel(order = 'F'))
