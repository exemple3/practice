def dfs(g, graph, visited):
    visited[g] = True
    for v in graph[g]:
        if not visited[v]:
            dfs(v, graph, visited)
# обход графа, помечает комп. связности

a = input().split()
N = int(a[0])
M = int(a[1])
# вершины и ребра

graph = {}
for i in range(1, N + 1):
    graph[i] = []
# словарь, соседние вершины: вершина i

for i in range(M):
    b = input().split()
    r = int(b[0])
    v = int(b[1])
    graph[r].append(v)
    graph[v].append(r)
# счит. ребра и добавляем в обе стороны

visited = [False] * (N + 1)
comp = 0

for i in range(1, N + 1):
    if not visited[i]:
        dfs(i, graph, visited)
        comp += 1    
# проходим по верш., если не посещена, то принадлежит к др. компоненте
print(comp - 1)
