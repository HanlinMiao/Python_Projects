terrain = [[1, 1, 1, 1, 0],
           [1, 1, 1, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 1, 0, 1 ,1],
           [1, 0, 0, 0, 1]]


def dps(layout, x, y):
    if x < 0 or x>len(layout)-1:
        print(1)
    elif y < 0 or y>len(layout[x])-1:
        print(2)
    elif layout[x][y] == 1:
        print(x, y)
        layout[x][y] = 0
        dps(layout, x+1, y)
        dps(layout, x, y+1)
        dps(layout, x-1, y)
        dps(layout, x, y-1)
    else:
        print(4)
    
def count_island(layout):
    count  = 0
    for i in range(len(layout)):
        for j in range(len(layout[i])):
            if layout[i][j] == 1:
                count = count+1
                dps(layout, i ,j)
    return count

print(count_island(terrain))
