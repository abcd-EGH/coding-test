def solution(rows, columns, queries):
    answer = []
    # 행렬 정의하기
    mat = []
    for i in range(rows):
        mat.append([i*columns+j+1 for j in range(columns)])
    # 행렬 돌리기
    for query in queries:
        x1, y1, x2, y2 = query
        x1 -= 1 # 행
        y1 -= 1 # 열
        x2 -= 1 # 행
        y2 -= 1 # 열
        temp = mat[x1][y1]
        min_value = temp
        for i in range(x1, x2):
            mat[i][y1] = mat[i+1][y1]
            min_value = min(min_value, mat[i+1][y1])
        
        for i in range(y1, y2):
            mat[x2][i] = mat[x2][i+1]
            min_value = min(min_value, mat[x2][i+1])
            
        for i in range(x2, x1, -1):
            mat[i][y2] = mat[i-1][y2]
            min_value = min(min_value, mat[i-1][y2])
        
        for i in range(y2, y1+1, -1):
            mat[x1][i] = mat[x1][i-1]
            min_value = min(min_value, mat[x1][i-1])
        
        mat[x1][y1+1] = temp
        
        answer.append(min_value)
        
    return answer

test1 = [6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]]
test2 = [3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]]
test3 = [100,97,[[1,1,100,97]]]
tests = [test1, test2, test3]

results = [[8, 10, 25],[1, 1, 5, 3],[1]]

for i in range(len(tests)):
    if solution(*tests[i]) == results[i] : print(f"test{i} 성공")
    else : print(f"test{i} 실패")