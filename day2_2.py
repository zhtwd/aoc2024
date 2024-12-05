data = open(0).read().splitlines()

def inrange(a, b):
    d = abs(a - b)
    if d >= 1 and d <= 3:
        return True
    return False


def check(row):
    if len(row) <= 1:
        return True
    dir = row[1] - row[0]
    if not inrange(row[1], row[0]):
        return False
    for i in range(2, len(row)):
        d = row[i] - row[i - 1]
        if dir * d < 0:
            return False
        if not inrange(row[i], row[i - 1]):
            return False
    return True
        

res = 0
for row in data:
    #print(row)
    row = [int(i) for i in row.split()]
    if check(row):
        res += 1
        #print(res)
        continue
    
    for i in range(len(row)):
        if check(row[:i] + row[i + 1:]):
            res += 1
            break

print(res)