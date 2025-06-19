n = int(input())
res = []
for _ in range(n):
    a, b, x, y = map(int, input().split())
    pairA2 = min(a, y)
    have_a = a - pairA2
    have_y = y - pairA2
    pairA1 = min(have_a, x)
    have_x = x - pairA1
    pairB1 = min(b, have_x)
    pairs = pairA2 + pairA1 + pairB1
    res.append(str(pairs))
print(' '.join(res))
