# 분할정복
def knapSack_bf(W, wt, val, n): 
    if n == 0 or W == 0 :       # 기반 상태. 물건이 없거나 용량이 0이면
        return 0                # 전체 가치 합은 0이 됨
  
    if (wt[n-1] > W):                           # 넣을 수 없음
        return knapSack_bf(W, wt, val, n-1)     # 나머지 항목들로 다시 처리
  
    else: 
        valWith = val[n-1] + knapSack_bf(W-wt[n-1], wt, val, n-1)
        valWithout = knapSack_bf(W, wt, val, n-1)
        return max(valWith, valWithout)

# 동적 계획법
def knapSack_dp(W, wt, val, n):
    A = [[0 for _ in range(W+1)] for _ in range(n+1)] # 테이블 초기화

    for i in range(1, n+1): # 진행방향: 위에서 아래
        for w in range(1, W+1): # 진행방향: 좌에서 우
            if wt[i-1] > w: # i번째 물건이 용량 초과
                A[i][w] = A[i-1][w]
            else: # i번째 물건을 넣을 수 있음
                valWith = val[i-1] + A[i-1][w-wt[i-1]] # i번째 물건을 넣는 경우
                valWithout = A[i-1][w] # i번째 물건을 넣지 않는 경우
                A[i][w] = max(valWith, valWithout)
    return A[n][W]

if __name__ == "__main__":
    val = [60, 100, 190, 120, 200, 150] 
    wt = [2, 5, 8, 4, 7, 6] 
    W = 18
    n = len(val) 
    print("0-1배낭문제(분할 정복): ", knapSack_bf(W, wt, val, n))
    print(knapSack_dp(W, wt, val, n))