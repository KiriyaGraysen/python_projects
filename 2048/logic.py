import random

def start_game():
    # initialize a grid
    mat = []
    
    # make a 4x4 grid full of zeros [0]
    for i in range(4):
        mat.append([0] * 4)
    
    # movement keys
    print("Commands are as follows : ")
    print("'W' or 'w' : Move Up")
    print("'S' or 's' : Move Down")
    print("'A' or 'a' : Move Left")
    print("'D' or 'd' : Move Right")
    
    # start the game with a random 2 in the grid
    add_new_2(mat)
    return mat

def find_empty(mat):
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                # return the index of the grid that has 0
                return i, j
    
    # both None if the grid is full
    return None, None
    
def add_new_2(mat):
    # checks if the grid is full of value other except 0
    if all(all(cell != 0 for cell in row) for row in mat):
        return
    
    # tries to find grid position with a value of [0]
    tries = 0
    while tries < 30:
        r = random.randint(0, 3)
        c = random.randint(0, 3)
        if mat[r][c] == 0:
            mat[r][c] = 2
            return
        tries += 1
    # if failed to find [0] after 30 tries find [0] manually
    r, c = find_empty(mat)
    if r is not None and c is not None:
        mat[r][c] = 2

def get_current_state(mat):
    # checks if any cell contains a value of [2048]
    for i in range(4):
        for j in range(4):
            if (mat[i][j] == 2048):
                return "YOU WIN!"
            
    # checks if there are still cell that has a value of zero [0]
    for i in range(4):
        for j in range(4):
            if (mat[i][j] == 0):
                return "GAME NOT OVER YET!"
    
    # checks if there are still same value besides and below each cell (except mat[3][3])
    # that can be merge
    for i in range(3):
        for j in range(3):
            if(mat[i][j] == mat[i + 1][j] or mat[i][j] == mat[i][j + 1]):
                return "GAME NOT OVER YET!"
    
    # checks the cell besides mat[3][3] if still mergeable
    for i in range(3):
        if (mat[3][i] == mat[3][i + 1]):
            return "GAME NOT OVER YET!"
    
    # checks the cell above mat[3][3] if stil mergeable
    for i in range(3):
        if (mat[i][3] == mat[i + 1][3]):
            return "GAME NOT OVER YET!"
    
    # if all conditions are False, then the player lost the game
    return "YOU LOST!"

def compress(mat):
    changed = False
    # initialize a new mat for substitution of values in the grid
    new_mat = []
    # make a 4x4 grid full of zeros [0]
    for i in range(4):
        new_mat.append([0] * 4)
    
    for i in range(4):
        pos = 0
        for j in range(4):
            # check if mat grid has a value except zerp [0]
            if (mat[i][j] != 0):
                # this is to move the value of mat to the pos[0] which is the corner of grid
                # depending on the movement the player chose
                new_mat[i][pos] = mat[i][j]
                
                if (j != pos):
                    changed = True
                pos += 1
                
    return new_mat, changed
    
def merge(mat):
    changed = False
    
    for i in range(4):
        for j in range(3):
            # check if the value next to each other are the same, except zero [0]
            if (mat[i][j] == mat[i][j + 1]) and mat[i][j] != 0:
                # multiply the value by 2
                mat[i][j] *= 2
                # change the value of the cell next to the multiplied cell to zero
                mat[i][j + 1] = 0
                changed = True
    
    return mat, changed
    
def reverse(mat):
    new_mat = []
    
    for i in range(4):
        # creates a new row with empty value
        new_mat.append([])
        for j in range(4):
            # puts the value in the new matrix row from original matrix in reverse order
            new_mat[i].append(mat[i][3 - j])
    return new_mat

def transpose(mat):
    new_mat = []
    
    for i in range(4):
        # creates a new row with empty value
        new_mat.append([])
        for j in range(4):
            # puts the value of the column of the original matrix to row of ne matrix
            new_mat[i].append(mat[j][i])
    return new_mat

def move_left(grid):
    # creates a new grid with the value from compress function
    new_grid, changed1 = compress(grid)
    # overwrite the value of new grid with the value from merge function using new grid as parameter
    new_grid, changed2 = merge(new_grid)
    
    # insert the value of change variable if either changed 1 or changed 2 are either True or False
    changed = changed1 or changed2
    
    # compress the new grid again after merging
    new_grid, temp = compress(new_grid)
    return new_grid, changed
    
def move_right(grid):
    new_grid = reverse(grid)
    new_grid, changed = move_left(new_grid)
    
    new_grid = reverse(new_grid)
    return new_grid, changed
    
def move_up(grid):
    new_grid = transpose(grid)
    new_grid, changed = move_left(new_grid)
    
    new_grid = transpose(new_grid)
    return new_grid, changed
    
def move_down(grid):
    new_grid = transpose(grid)
    new_grid, changed = move_right(new_grid)
    
    new_grid = transpose(new_grid)
    return new_grid, changed