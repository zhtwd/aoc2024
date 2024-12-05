data = open(0).read().splitlines()

rules = []
orders = []
orders_lst = []
for row in data:
    if '|' in row:
        rules.append(list(map(int, row.split('|'))))
    elif ',' in row:
        orders_lst.append(list(map(int, row.split(','))))
        orders.append({x: i for i, x in enumerate(orders_lst[-1])})


err = set()
for a, b in rules:
    for i, order in enumerate(orders):
        if i in err:
            continue
        if a in order and b in order and order[a] > order[b]:
            err.add(i)
#print(err)

res = 0
for i, order in enumerate(orders_lst):
    if i not in err:
        res += order[len(order)//2]
print(res)
