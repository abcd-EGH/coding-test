# 신장 트리 (Spanning Tree)
# 그래프 내 모든 정점을 포함하는 '트리'
# 즉, 그래프의 정점은 모두 포함하고, 간선은 일부만을 포함해 트리의 형태를 이루어야 함
# 사이클이 존재해서는 안됨
# 만약 정점 수가 n이라면, 신장 트리는 정확히 n-1개의 간선으로 모든 정점을 연결해야 함
# 깊이 또는 너비 우선 탐색 도중에 사용된 간선들만 모으면 신장 트리가 만들어짐

# DFS, 인접 행렬 활용
def ST_DFS(vtx, adj, s, visited):
    visited[s] = True
    for v in range(len(vtx)):
        if adj[s][v] != 0 and visited[v] == False:
            print(f"( {vtx[s]} {vtx[v]} )", end= ' ')
            ST_DFS(vtx, adj, v, visited)

vtx = ['U','V','W','X','Y']
edge= [[0,  1,  1,  0,  0],
       [1,  0,  1,  1,  0],
       [1,  1,  0,  0,  1],
       [0,  1,  0,  0,  0],
       [0,  0,  1,  0,  0]]

print('ST_DFS(출발:U): ', end="")
ST_DFS(vtx, edge, 0, [False]*len(vtx))
print()

# BFS, 인접 리스트 활용
from queue import Queue
def ST_BFS(vtx, adj, s):
    n = len(vtx)
    visited = [False]*n
    Q = Queue()
    Q.put(s)
    visited[s] = True
    while not Q.empty():
        s = Q.get()
        for v in adj[s]:
            if visited[v] == False:
                Q.put(v)
                visited[v] = True
                print(f"( {vtx[s]} {vtx[v]} )", end= ' ')

vtx = ['U','V','W','X','Y']
aList=[[1, 2], # U는 V, W와 인접함
       [0, 2, 3], # V는 U, W, X와 인접함
       [0, 1, 4],
       [1],
       [2]]

print('ST_BFS(출발:U): ', end="")
ST_BFS(vtx, aList, 0)
print()

