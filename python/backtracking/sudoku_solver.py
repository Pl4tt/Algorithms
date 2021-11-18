def solve(bo):
    find = find_empty(bo)

    if not find:
        return True # solution found
    
    row, col = find

    for i in range(1, 10):
        if is_valid(bo, row, col, i):
            bo[row][col] = i

            if solve(bo):
                return True
            
            bo[row][col] = 0
    
    return False

def find_empty(bo):
    for x in range(len(bo)):
        for y in range(len(bo)):
            if bo[x][y] == 0:
                return (x, y)
    
    return None

def is_valid(bo, row, col, val):
    # check row and col
    for x in range(len(bo)):
        for y in range(len(bo)):
            if bo[x][col] == val and x != row or bo[row][y] == val and y != col:
                return False
    
    # check 3x3 box
    box_x = row // 3
    box_y = col // 3

    for x in range(box_x*3, box_x*3 + 3):
        for y in range(box_y*3, box_y*3 + 3):
            if bo[x][y] == val and (x, y) != (row, col):
                return False
    
    return True

def print_board(bo):
    for x in range(len(bo)):
        if x % 3 == 0 and x != 0:
            print("- - - - - - - - - - - - -")
        for y in range(len(bo)):
            if y % 3 == 0 and y != 0:
                print(" | ", end="")
            if y <= 7:
                print(bo[x][y], end=" ")
            else:
                print(bo[x][y])

def solve_print(bo):
    print('\n--------------------------------------\n')
    print('× Unsolved Suduku:')
    print_board(bo)
    print('\n--------------------------------------\n')
    solve(bo)
    print('× Solved Suduku:')
    print_board(bo)
    print('\n--------------------------------------\n')
