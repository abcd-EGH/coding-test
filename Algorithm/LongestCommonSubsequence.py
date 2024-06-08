# LCS 길이 계산 알고리즘 with recursion
def lcs_recur(X, Y, m, n): # 문자열 X, Y와 그 길이 m, n
    if m == 0 or n == 0: # Case 1
        return 0
    elif X[m-1] == Y[n-1]: # Case 2
        return 1 + lcs_recur(X, Y, m-1, n-1)
    else:
        return max(lcs_recur(X, Y, m-1, n), lcs_recur(X, Y, m, n-1))
    
# LCS 길이 계산 알고리즘 with Dynamic Programming
def lcs_dp(X, Y):
    m = len(X)
    n = len(Y)
    L = [[None]*(n+1) for _ in range(m+1)] # 테이블 준비

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: # 마지막 글자가 같으면
                L[i][j] = L[i-1][j-1] + 1
            else: # 마지막 글자가 다르면
                L[i][j] = max(L[i-1][j], L[i][j-1])
    
    return L[m][n], L, lcs_dp_traceback(X, Y, L)

def lcs_dp_traceback(X, Y, L): # L은 이미 계산되어 있는 상태이어야 함
    lcs = ""
    i = len(X) # 맨 마지막 인덱스로 초기화
    j = len(Y) # 맨 마지막 인덱스로 초기화
    while i > 0 and j > 0:
        v = L[i][j]
        if v > L[i][j-1] and v > L[i-1][j-1] and v > L[i-1][j]:
            i -= 1
            j -= 1
            lcs = X[i] + lcs
        elif v == L[i][j-1] and v > L[i-1][j]:
            j -= 1
        else:
            i -= 1
    return lcs

if __name__ == "__main__":
    x = 'HELLO WORLD'
    y = 'GAME OVER'
    m = len(x)
    n = len(y)

    print(lcs_recur(x, y, m, n)) # lcs 길이 계산 with 재귀
    print(lcs_dp(x, y)[0]) # lcs 길이 계산 with 동적 프로그래밍
    print(lcs_dp(x, y)[1]) # lcs 테이블
    print(lcs_dp(x, y)[2]) # lcs