import numpy as np
data = open(0).read().splitlines()

data = [list(s) for s in data]

m = len(data)
n = len(data[0])
data = np.array(data)

dirs = [[0, 1], [1, 1], [1, 0], [-1, -1], [0, -1], [-1, 1], [-1, 0], [1, -1]]

s = 'XMAS'

def isin(x, y):
    if x >= 0 and x < m and y >= 0 and y < n:
        return True
    return False

res = 0

def search(x, y, i, d):
    #print(x, y, i)
    visited.add((x, y))
    global res
    if i == 3 and data[x][y] == 'S':
        #print(' ', x, y)
        res += 1
        return

    nx = x + dirs[d][0]
    ny = y + dirs[d][1]
    if isin(nx, ny) and (s[i + 1] == data[nx][ny]) and ((nx, ny) not in visited):
        search(nx, ny, i + 1, d)


def searchx(x, y):
    global res
    if x > 0 and y > 0 and x < m - 1 and y < n - 1:
        s1 = '' + data[x-1][y+1] + data[x+1][y-1]
        s2 = '' + data[x+1][y+1] + data[x-1][y-1]
        if s1 in ('MS', 'SM') and s2 in ('MS', 'SM'):
            res += 1

res = 0
for i in range(1, m-1):
    for j in range(1, n-1):
        # puzzle 1
        # if data[i][j] == 'X':
        #     #print(i, j)
        #     visited = set()
        #     for d in range(len(dirs)):
        #         search(i, j, 0, d)
        # puzzle 2
        if data[i][j] == 'A':
            searchx(i, j)
            

print(res)