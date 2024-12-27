import numpy as np

def slice_array(arr:np.ndarray, start:int=0, end:int=1, steps:int=1) -> np.ndarray:
    return arr[start:end:steps]

if __name__ == '__main__':
    array = np.array([1,2,3,4,5,6,7,8,9])
    print(array)
    print(slice_array(array, start=1, end=5, steps=2))
    array2 = np.array([[1,2,3,4],[5,6,7,8]])
    print(array2)
    print(array2[1, 1:array2[1].size-2])
    array3 = np.array([[
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
    ]])
    print(array3)
    print(array3[0,0, :2])
