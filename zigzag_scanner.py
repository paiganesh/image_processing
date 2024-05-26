# Performs zigzag scan of a 2D matrix of type ndarray
# Argument: ndarray type 2D matrix of arbitrary size
# returns: 1 x (m*n) ndarray, where m and n are input matrix dimensions
#
# Contributor:
# Ganesh Pai, Karnataka, India
# May 2024
# ganeshpai24@gmail.com

import numpy as np

def zigzag_scan(matrix:np.ndarray):
    p = 0
    array = np.zeros(matrix.shape[0] * matrix.shape[1], dtype=float)
    
    array[0] = matrix[0,0]; p += 1
    
    rows, cols = matrix.shape[:2]
    i = j = 0
    
    while i != rows-1 or j != cols-1:
        # if reached top-right end, move 1 step right or down
        if j == cols-1:
            i += 1
        else:
            j += 1
        if i > rows-1 or j > cols-1: break
        array[p] = matrix[i,j]; p += 1

        # move down left
        while i != rows-1 and j != 0:
            i += 1; j -= 1
            array[p] = matrix[i,j]; p += 1

        # if reached bottom-left end, move 1 step down or right
        if i == rows-1:
            j += 1
        else:
            i += 1
        if i > rows-1 or j > cols-1: break
        array[p] = matrix[i,j]; p += 1
        
        # move up right
        while i != 0 and j != cols-1:
            i -= 1; j += 1
            array[p] = matrix[i,j]; p += 1
    
    return array


# Reframes 2D ndarray by performing inverse zigzag scan from 1D ndarray to a 2D matrix
# Argument: ndarray type 1D array
#           tuple representing shape of the 2D matrix to be formed    
# returns: m*n ndarray, where m and n are output matrix dimensions
#
# Contributor:
# Ganesh Pai, Karnataka, India
# May 2024
# ganeshpai24@gmail.com

def zigzag_scan_inverse(array:np.ndarray, shape:tuple)->np.ndarray:
    matrix = np.zeros(shape, dtype=float)
    
    rows, cols = shape
    i = j = k = 0
    
    matrix[0,0] = array[0]
    while i != rows-1 or j != cols-1:
        # if reached top-right end, move 1 step right or down
        if j == cols-1:
            i += 1
        else:
            j += 1
        k += 1
        if i > rows-1 or j > cols-1: break
        matrix[i,j] = array[k]

        # move down left
        while i != rows-1 and j != 0:
            i += 1; j -= 1
            k += 1
            matrix[i,j] = array[k]

        # if reached bottom-left end, move 1 step down or right
        if i == rows-1:
            j += 1
        else:
            i += 1
        k += 1
        if i > rows-1 or j > cols-1: break
        matrix[i,j] = array[k]
        
        # move up right
        while i != 0 and j != cols-1:
            i -= 1; j += 1
            k += 1
            matrix[i,j] = array[k]
    
    return matrix
    


if '__name__' == '__main__':
    matrix = np.array(range(1,704381)).reshape((820,859))
    scanned_array  = zigzag_scan(matrix)
    inverse_matrix = zigzag_scan_inverse(scanned_array, matrix.shape[:2])
