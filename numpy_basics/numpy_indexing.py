import numpy as np

array = np.array([1, 2, 3, 4, 5])
array2 = np.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])
array3 = np.array([
    [
        [1, 2, 3],
        [4, 5, 6],
    ],
    [
        [7, 8, 9],
        [10, 11, 12],
    ]
])

if __name__ == '__main__':
    print(array[0]) #1
    print(array2[0]) #[1 2 3 4 5]
    print(array3[0]) #[[1 2 3] [4 5 6]]
    print(array2[1,0])
    print(array3[0,0,2])
    print(array3[1, 0, 2])