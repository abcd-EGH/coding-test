# LCS 길이 계산 알고리즘 with recursion
def lcs_recur(X, Y, m, n): # 문자열 X, Y와 그 길이 m, n
    if m == 0 or n == 0: # Case 1
        return 0
    elif X[m-1] == Y[n-1]: # Case 2
        return 1 + lcs_recur(X, Y, m-1, n-1)
    else:
        return max(lcs_recur(X, Y, m-1, n), lcs_recur(X, Y, m, n-1))
    
def lcs_dp(X, Y):
    m = len(X)
    n = len(Y)
    L = [[None]*(n+1) for _ in range(m+1)] # 테이블 준비

    for i in range(m+1):
        pass

x = 'HELLO WORLD'
y = 'GAME OVER'
m = len(x)
n = len(y)

print(lcs_recur(x, y, m, n)) # 재귀 활용