def f(p):
    n = len(p)
    decode = [0] * n
    for i in range(n):
        decode[p[i] - 1] = i
    return decode

n, k = map(int, input().split())
p = list(map(int, input().split()))
a = input()

decode = f(p)
for _ in range(k):
    a = ''.join(a[decode[i]] for i in range(n))
print(a)
