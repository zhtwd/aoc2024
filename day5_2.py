
from collections import defaultdict

data = open(0).read().splitlines()

rules = []
orders = []
orders_lst = []
moved = defaultdict(set)

for row in data:
    if '|' in row:
        rules.append(list(map(int, row.split('|'))))
        a, b = list(map(int, row.split('|')))
        moved[b].add(a)
    elif '' == row:
        pass
    elif ',' in row:
        orders_lst.append(list(map(int, row.split(','))))
        orders.append({x: i for i, x in enumerate(orders_lst[-1])})
        pass


err = set()
for a, b in rules:
    for i, order in enumerate(orders):
        if i in err:
            continue
        if a in order and b in order and order[a] > order[b]:
            err.add(i)


res = 0
for i, order in enumerate(orders_lst):
    if i in err:
        for ii in range(len(order)):
            while order[ii] in moved:
                flag = True
                for jj in range(ii + 1, len(order)):
                    if order[jj] in moved[order[ii]]:
                        order[ii], order[jj] = order[jj], order[ii]
                        flag = False
                        break
                if flag:
                    break
                
        res += order[len(order)//2]

print(res)
