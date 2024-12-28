import numpy as np

if __name__ == '__main__':
    """
    concatenate(): Combines arrays along an existing axis.
    array_split(): Splits an array into smaller sub-arrays (even or uneven).
    stack(): Combines arrays along a new axis, increasing dimensionality.
    """
    array_1 = np.array([1, 2, 3])
    array_2 = np.array([4, 5, 6])
    concat = np.concatenate((array_1, array_2))
    print(concat)
    print()
    stack_1 = np.stack((array_1, array_2), axis=0)
    print(stack_1)
    print()
    stack_2 = np.stack((array_1, array_2), axis=1)
    print(stack_2)
    print()
    stack_3 = np.vstack((array_1, array_2))
    print(stack_3)
    print()
    stack_4 = np.hstack((array_1, array_2))
    print(stack_4) #[1 2 3 4 5 6]
    print()
    stack_5 = np.dstack((array_1, array_2))
    print(stack_5)
    print()
    split_array = np.array([1, 2, 3, 4, 5, 6])
    split_1 = np.array_split(split_array, 2)
    print(split_1) #[array([1, 2, 3]), array([4, 5, 6])]