#https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python
def snail(snail_map):
    expected = []
#4 directions available (in the order of): right, down, left, up
#utilizing X and Y values to "block" off the inner and  outer bounds. Repeating the four directions until all the values are blocked off.
#Append the values on a separate list as we go. Avoiding the pop or removing method to change the value of read iterable mid-loop.
    inner_x = -1
    inner_y = -1
    outer_x = len(snail_map[0])
    outer_y = len(snail_map)
    moves = len(snail_map) * len(snail_map[0]) #Keeping a moves counter, if the grid is 3x3, then the loop will stop after 9 moves.
    while moves > 0:
        #right
        for x in range(inner_x+1, outer_x):
            expected.append(snail_map[inner_y+1][x])
        inner_y += 1
        moves -= 1
        #down
        for y in range(inner_y+1, outer_y):
            expected.append(snail_map[y][outer_x-1])
        outer_x -= 1
        moves -= 1
        #left
        for x in reversed(range(inner_x+1, outer_x)):
            expected.append(snail_map[outer_y-1][x])
        outer_y -= 1
        moves -= 1
        #up
        for y in reversed(range(inner_y+1, outer_y)):
            expected.append(snail_map[y][inner_x+1])
        inner_x += 1
        moves -= 1
    return expected
