a = input().split()
h = int(a[0])
w = int(a[1])
# ввод высоты и ширины матрицы
matrix = []
for i in range(h):
    row = input().split()
    r = []
    for i in row:
        r.append(int(i))
    matrix.append(row)
# ввод матрицы

min1_r = h   # мин. строка с единицей 
max1_r = -1  # макс. строка с единицей
min1_c = w   # мин. столбец с единицей
max1_c = -1  # макс. столбец с единицей

for i in range(h):
    for j in range(w):
        if matrix[i][j] == 1:
            min1_r = min(min1_r, i)
            max1_r = max(max1_r, i)
            min1_c = min(min1_c, j)
            max1_c = max(max1_c, j)
# для кажд. ячейки обновл. данные

topleft_r = min1_r - 1
topleft_c = min1_c - 1
lowerright_r = max1_r + 1
lowerright_c = max1_c + 1
# так как должен помещаться в
print(topleft_r, topleft_c, lowerright_r, lowerright_c)
