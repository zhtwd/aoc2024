import re

def find(s):
    r = re.compile(r'don\'t\(\)|do\(\)|mul\(\d+,\d+\)', flags=re.I | re.X)
    return r.findall(s)

data = open(0).read().splitlines()

res = 0
flag = True
for row in data:
    s = find(row)
    #print(row, s)
    for i in s:
        if i == "don't()":
            flag = False
        elif i == "do()":
            flag = True
        else:
            nbs = i[4:-1]
            a, b = list(map(int, nbs.split(',')))
            if flag:
                res += a * b

print(res)