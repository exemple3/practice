def f(snow, start, finish):
    res = 0
    for i in range(start, finish + 1):
        res += snow[i]
    return res

n, k = map(int, input().split())

snow = [0] * (n + 1)

for _ in range(k):
    o = list(map(int, input().split()))
    otype = o[0]

    if otype == 1:
        st, snowk = o[1], o[2]
        snow[st] += snowk
    elif otype == 2:
        start, end = o[1], o[2]
        res = f(snow, start, end)
        print(res)
