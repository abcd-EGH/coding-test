# DFS
# 그래프는 인접 행렬로 표현
# 정점 리스트 vtx와 인접 행렬 adj가 주어진다고 가정, 시작 정점은 s
# 각 정점으 방문 여부를 기록하기 위해 visited 배열을 사용, 맨 처음에는 모든 정점을 방문하지 않았으므로 False로 초기화

def DFS(vtx, adj, s, visited):
    print(vtx[s], end = ' ') # 방문한 현재 정점을 출력
    visited[s] = True # visited 배열의 s 인덱스를 True로 변경, 방문했음을 표시

    for v in range(len(vtx)):
        if adj[s][v] != 0 and visited[v] == False:
            # adj[s][v] -> s가 v와 인접하는가? // visited[v] -> 정점 v를 방문한 적이 있는가?
            DFS(vtx, adj, v, visited)

vtx = ['U','V','W','X','Y']
edge= [[0,  1,  1,  0,  0],
       [1,  0,  1,  1,  0],
       [1,  1,  0,  0,  1],
       [0,  1,  0,  0,  0],
       [0,  0,  1,  0,  0]]

print('DFS(출발:U) : ', end="")
DFS(vtx, edge, 0, [False]*len(vtx))
print()


##############################################################

# BFS
# 그래프는 인접 리스트로 표현
# 정점 리스트 vtx와 인접 리스트 aList가 주어진다고 가정, 시작 정점은 s
# 방문 정점을 표시하는 visited 배열을 함수 내부에서 만들어 사용
# 순환 호출을 이용한 DFS와는 달리 BFS는 반복 구조로 구현

from queue import Queue
def BFS_AL(vtx, aList, s):
    n = len(vtx)
    visited = [False]*n
    Q = Queue()
    Q.put(s)
    visited[s] = True
    while not Q.empty():
        s = Q.get() # 큐에서 맨 앞 정점을 꺼냄
        print(vtx[s], end= ' ')
        for v in aList[s]: # aList[s] -> s의 인접 정점들, v -> s의 인접 정점
            if visited[v] == False: # v가 방문하지 않았던 정점일 경우
                Q.put(v) # 큐에 v를 저장
                visited[v] = True # v를 방문했다고 표시

vtx = ['U','V','W','X','Y']
aList=[[1, 2], # U는 V, W와 인접함
       [0, 2, 3], # V는 U, W, X와 인접함
       [0, 1, 4],
       [1],
       [2]]

print('BFS_AL(출발:U): ', end="")
BFS_AL(vtx, aList, 0)
print()


