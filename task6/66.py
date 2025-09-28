n = int(input())
res = []
for i in range(n):
    p = input().split()
    a = int(p[0])
    b = int(p[1])
    x = int(p[2])
    y = int(p[3])
    
    pairA2 = min(a, y)
    have_a = a - pairA2
    have_y = y - pairA2
    #создание пар A2
    
    pairA1 = min(have_a, x)
    have_x = x - pairA1
    #создание пар A1
    
    pairB1 = min(b, have_x)
    #создание пар B1
    
    pairs = pairA2 + pairA1 + pairB1
    res.append(str(pairs))
    #суммирование пар и добавл. в результ.
for result in res:
    print(result)
