h, w = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(h)]
min1_r, max1_r = h, -1
min1_c, max1_c = w, -1

for i in range(h):
    for j in range(w):
        if matrix[i][j] == 1:
            min1_r = min(min1_r, i)
            max1_r = max(max1_r, i)
            min1_c = min(min1_c, j)
            max1_c = max(max1_c, j)

topleft_r = min1_r - 1
topleft_c = min1_c - 1
lowerright_r = max1_r + 1
lowerright_c = max1_c + 1
print(topleft_r, topleft_c, lowerright_r, lowerright_c)
