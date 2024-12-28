import numpy as np

array = np.array([1,2,3,4,5,6,7], np.int32)

if __name__ == '__main__':
    """
    Use `view` when you need to manipulate the shape or change the dtype of the data without modifying the original array.
    Use `copy` when you need a completely independent copy of the data that can be safely modified without affecting the original array.
    """
    print(array)
    copy_array = np.copy(array)
    print(copy_array)
    array[0] = 10
    assert array[0] != copy_array[0]
    print(array)
    print(copy_array)
    view_array = array.view()
    print(view_array)
    print(array)
    array[2] = 20
    assert array[2] == view_array[2]
    print(array)
    print(view_array)