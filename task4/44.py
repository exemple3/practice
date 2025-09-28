def f(a):
    n = len(a)
    decode = [0] * n
    for i in range(n):
        decode[a[i] - 1] = i
    return decode
# функция декодировки

a = input().split()
n = int(a[0])
k = int(a[1])
# ввод длины слова и количества шифрования

p = []
    for j in input().split():
        p.append(int(j))
a = input()
# ввод перестановки и слова

decode = f(p)
for i in range(k):
    new_a = ''
    for i in range(n):
        new_a += a[decode[i]]
    a = new_a
# изменяет слово и заменяет им старое
print(a)
