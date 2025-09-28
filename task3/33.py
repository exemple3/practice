def f(snow, start, finish):
    res = 0
    for i in range(start, finish + 1):
        res += snow[i]
    return res
# сколько снега на улице i

a = input().split()
n = int(a[0])
k = int(a[1])
# улицы и запросы

snow = [0] * (n + 1)

for i in range(k):
    o = []
    for j in input().split():
        o.append(int(j))
    otype = o[0]
    # считывание значений, 1 число - событие
    
    if otype == 1:
        st, snowk = o[1], o[2]
        snow[st] += snowk
    elif otype == 2:
        start, end = o[1], o[2]
        res = f(snow, start, end)
        print(res)
