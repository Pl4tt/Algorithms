# 0 = empty field
# -1 = wall
# -2 = starting position

# replace every 0 with the minimal distance to the starting position without going through a wall
# You are allowed to go right, left, up and down. Diagonal moves are not allowed
# if there is no possibility to reach a 0, just leave it as a 0

# input:
#   n by n (n == n)

# example:
# [-2, 0, 0, -1] -> [-2, 1, 2, -1]
# [0, -1, 0, -1] -> [1, -1, 3, -1]

arr = [
    [0, -2, -1, 0],
    [0, -1, 0, -1],
    [0,  0, 0, -1],
    [-1, -1, 0, 0]
]
sol = [
    [1, -2, -1, 0],
    [2, -1, 6, -1],
    [3, 4, 5, -1],
    [-1, -1, 6, 7]
]


def solve(arr: list[list[int]]) -> list[list[int]]:
    """changes all zero's to the distance to the starting position (-2)
    if they are reachable, the not reachable zero's stays as zero's.
    The modified arr will also be returned."""
    visited, start_pos = create_seq(arr)
    
    depth_search(arr, *start_pos, visited, 0)
    return arr

def depth_search(arr: list[list[int]], x: int, y: int, visited: list[list[bool]], depth: int=0) -> None:
    """goes through all reachable zero's in the arr list and changes
    it's value to the distance to the starting position"""
    if arr[x][y] == 0:
        arr[x][y] = depth

    visited[x][y] = True
    depth += 1
    
    if x+1 < len(arr) and not visited[x+1][y] and arr[x+1][y] == 0:
        depth_search(arr, x+1, y, visited, depth)
    if y+1 < len(arr[x]) and not visited[x][y+1] and arr[x][y+1] == 0:
        depth_search(arr, x, y+1, visited, depth)
    if y-1 >= 0 and not visited[x][y-1] and arr[x][y-1] == 0:
        depth_search(arr, x, y-1, visited, depth)
    if x-1 >= 0 and not visited[x-1][y] and arr[x-1][y] == 0:
        depth_search(arr, x-1, y, visited, depth)

def create_seq(arr: list) -> tuple[list[list[bool]], tuple[int]]:
    """Returns a visited list with lists of booleans
    and the starting position as a tuple"""
    result = []
    for x in range(len(arr)):
        result.append([])
        for y in range(len(arr[0])):
            if arr[x][y] == -2:
                result[x].append(True)
                start = (x, y)
            elif arr[x][y] == -1:
                result[x].append(True)
            else:
                result[x].append(False)
    
    return result, start




if __name__ == "__main__":
    solve(arr)
    print(arr)
    print(sol == arr)