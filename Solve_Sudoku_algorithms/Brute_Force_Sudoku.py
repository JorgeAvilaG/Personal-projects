import numpy as np

def check_column(position):    
    value = matrix[position]
    count = np.count_nonzero(matrix[0:,position[1]] == value)
    
    if count == 1:
        return True
    else:
        return False

def check_file(position):    
    value = matrix[position]
    count = np.count_nonzero(matrix[position[0],0:] == value)
    
    if count == 1:
        return True
    else:
        return False

def check_cube(position): 
    value = matrix[position]
    if position[0] < 3:
        if   position[1] < 3:
            count =  np.count_nonzero(matrix[0,0:3] == value)
            count += np.count_nonzero(matrix[1,0:3] == value)
            count += np.count_nonzero(matrix[2,0:3] == value)
        elif position[1] < 6:
            count =  np.count_nonzero(matrix[0,3:6] == value)
            count += np.count_nonzero(matrix[1,3:6] == value)
            count += np.count_nonzero(matrix[2,3:6] == value)
        else:
            count =  np.count_nonzero(matrix[0,6:] == value)
            count += np.count_nonzero(matrix[1,6:] == value)
            count += np.count_nonzero(matrix[2,6:] == value)
    elif position[0] < 6:
        if   position[1] < 3:
            count =  np.count_nonzero(matrix[3,0:3] == value)
            count += np.count_nonzero(matrix[4,0:3] == value)
            count += np.count_nonzero(matrix[5,0:3] == value)
        elif position[1] < 6:
            count =  np.count_nonzero(matrix[3,3:6] == value)
            count += np.count_nonzero(matrix[4,3:6] == value)
            count += np.count_nonzero(matrix[5,3:6] == value)
        else:
            count =  np.count_nonzero(matrix[3,6:] == value)
            count += np.count_nonzero(matrix[4,6:] == value)
            count += np.count_nonzero(matrix[5,6:] == value)
    else:
        if   position[1] < 3:
            count =  np.count_nonzero(matrix[6,0:3] == value)
            count += np.count_nonzero(matrix[7,0:3] == value)
            count += np.count_nonzero(matrix[8,0:3] == value)
        elif position[1] < 6:
            count =  np.count_nonzero(matrix[6,3:6] == value)
            count += np.count_nonzero(matrix[7,3:6] == value)
            count += np.count_nonzero(matrix[8,3:6] == value)
        else:
            count =  np.count_nonzero(matrix[6,6:] == value)
            count += np.count_nonzero(matrix[7,6:] == value)
            count += np.count_nonzero(matrix[8,6:] == value)
    
    if count == 1:
        return True
    else:
        return False

def valid_position(position):
    return check_column(position) and check_file(position) and check_cube(position)
    
def move_pointer_forward(pointer):
    if pointer[1] == 8:
        return (pointer[0]+1,0)
    else:
        return (pointer[0],pointer[1]+1)
    
def move_forward(pointer):    
    pointer = move_pointer_forward(pointer)
    while pointer in clues:
        pointer = move_pointer_forward(pointer)
    return pointer
    
def move_pointer_backward(pointer):
    if pointer[1] == 0:
        return (pointer[0]-1,8)
    else:
        return (pointer[0],pointer[1]-1)
    
def move_backward(pointer):    
    pointer = move_pointer_backward(pointer)
    while pointer in clues:
        pointer = move_pointer_backward(pointer)
    return pointer

def sudoku():
    pointer = (0,0)
    while pointer in clues:
            pointer = move_pointer_forward(pointer)
    while pointer != (9,0):
        matrix[pointer] += 1.0
        if matrix[pointer] == 10:
            matrix[pointer] = 0.0
            pointer = move_backward(pointer)
        elif valid_position(pointer):
            pointer = move_forward(pointer)

matrix = np.zeros((9,9))
clues = {(0,0):5,(0,1):3,(0,4):7,
         (1,0):6,(1,3):1,(1,4):9,(1,5):5,
         (2,1):9,(2,2):8,(2,7):6,
         (3,0):8,(3,4):6,(3,8):3,
         (4,0):4,(4,3):8,(4,5):3,(4,8):1,
         (5,0):7,(5,4):2,(5,8):6,
         (6,1):6,(6,6):2,(6,7):8,
         (7,3):4,(7,4):1,(7,5):9,(7,8):5,
         (8,4):8,(8,7):7,(8,8):9}
for clue in clues:
    matrix[clue] = clues[clue]
    
sudoku()
matrix
