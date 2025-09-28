import random

n = int(input())
mount = []
for r in range(n):
    row = []
    for c in range(r + 1):
        row.append(random.randint(10, 100))
    mount.append(row)
# создание горы

for row in mount:
    print(row)

mount_dp = []
for row in mount:
    mount_dp.append(row[:]) #все
# создание копии горы для сохранения изначальных данных

for r in range(n - 2, -1, -1):
    for c in range(len(mount_dp[r])):
        mount_dp[r][c] = mount_dp[r][c] + min(mount_dp[r+1][c], mount_dp[r+1][c+1])
# для кажд. элемента добавляем миним. значение под ним

mint = mount_dp[0][0]
print(mint)

p = []
r = 0
c = 0
p.append(mount[r][c]) # использ. знач из mount

while r < n - 1:
    left = mount_dp[r+1][c]
    right = mount_dp[r+1][c+1]
    
    if mount_dp[r+1][c] < mount_dp[r+1][c+1]:
        c += 0 #идем влево
    else:
        c += 1 #идем вправо
    
    r += 1
    p.append(mount[r][c])т
# восстановление пути - выбираем с меньш. временем и запис. из mount

print(*(p))
