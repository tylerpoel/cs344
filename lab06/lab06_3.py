'''
Using the Keras version of the Boston Housing Price Dataset for some
    initial exploration with Numpy and Keras.
Created by: Tyler Poel, for lab06 in CS 344 at Calvin University
Date: March 15, 2020
'''

from keras.datasets import boston_housing
(train_data, train_labels), (test_data, test_labels) = boston_housing.load_data()

# 6.3 a i
print("Number of training examples: " + str(len(train_data)))
print("Number of test examples: " + str(len(test_data)))

# 6.3 a ii
print(
    'training examples \
    \n\tdimensions: {} \
    \n\tshape: {} \
    \n\tdata type: {}\n\n'.format(
        train_data.ndim,
        train_data.shape,
        train_data.dtype
    )
)

print(
    'testing examples \
    \n\tdimensions: {} \
    \n\tshape: {} \
    \n\tdata type: {} \n'.format(
        test_data.ndim,
        test_data.shape,
        test_data.dtype
    )
)