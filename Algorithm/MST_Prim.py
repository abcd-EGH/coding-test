# MST에 포함되지 않은 최소 dist의 정점 찾기
INF = 10e+10
def getMinVertex(dist, selected):
    minv = 0
    mindist = INF
    for v in range(len(dist)):
        if selected[v]==False and dist[v]<mindist:
            mindist = dist[v]
            minv = v
    return minv

def MSTPrim(vertex, adj):
    n = len(vertex)
    dist = [INF] * n		# dist는 MST에서 정점까지의 거리 배열
    dist[0] = 0			    # dist: [0, INF, ... INF]
    selected = [False] * n	# selected: [False, False, ... False]

    for _ in range(n):		# n개의 정점을 MST에 추가하면 종료됨
        u = getMinVertex(dist, selected)
        selected[u] = True	# u는 이제 MST에 포함됨
        print(vertex[u], end=' ')	# u출력 
        for v in range(n):
             # 간선 (u,v)가 있고, v ∉ MST 이면
            if adj[u][v] != INF and not selected[v]:
                if adj[u][v]< dist[v]:	# (u,v)가 dist[v]보다 작으면
                    dist[v] = adj[u][v]	# dist[v] 갱신

        print(': ', dist)	# 중간 결과 출력

    print()


# Prim의 MST 테스트 프로그램
vertex =   ['A',    'B',    'C',    'D',    'E',    'F',    'G' ]
weight = [ [0,	   25,		INF,	12,	  INF,     INF,		INF],
           [25,		0,	    10,		INF,	15,	   INF,	    INF],
           [INF,	10,		0,	    INF,	INF,	INF,	16],
           [12,	    INF,    INF,	0,      17,	    37,	    INF],
           [INF,	15,	    INF,    17,	    0,      19,		14  ],
           [INF,	INF,	INF,	37,     19,		0,	    42],
           [INF,    INF,	16,     INF,	14,		42,	    0   ]]    

print("MST By Prim's Algorithm")
MSTPrim(vertex, weight)
