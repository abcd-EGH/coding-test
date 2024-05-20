def powerMat(x, n):
    if n == 1:
        return x
    if n % 2 == 0:
        return powerMat(multMat(x, x), n / 2)
    elif n % 2 == 1:
        return multMat(x, powerMat(multMat(x, x), (n-1) / 2))
    
def multMat(x1, x2):
    n = len(x1)
    result = [[0 for _ in range(n)] for _ in range(n)] # n*n 영행렬 초기화
    for i in range(n): # [i][_]
        for j in range(n): # [_][j]
            x1_ = x1[i] # x1에서 곱할 원소들(가로)
            x2_ = [x2[k][j] for k in range(n)] # x2에서 곱할 원소들(세로)
            result[i][j] = sum([a*b for a, b in zip(x1_,x2_)]) # x1에서 추출한 가로 원소 * x2에서 추출한 세로 원소
    return result

if __name__ == "__main__":
    mat1 = [[2,2],[1,2]]
    mat2 = [[3,2],[3,3]]
    print(multMat(mat1, mat2))
    print(powerMat(mat1, 5))