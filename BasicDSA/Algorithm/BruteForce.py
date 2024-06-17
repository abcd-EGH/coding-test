# 억지 기법으로 문자열 패턴 찾기
def string_matching(T, P): # T: 입력 문자열, P: 찾는 문자열(패턴)
    n = len(T)
    m = len(P)

    for i in range(n-m+1):
        for j in range(m):
            if T[i+j] != P[j]:
                break
            if j == m-1:
                return i
    return -1

# 억지 기법으로 배낭 채우기 (Knapsack problem)
def Knapsack_BF(wgt, val, W): # wgt: 물건별 무게 리스트, val: 물건별 가치, W: 배낭의 용량(물건들의 최대 무게)
    n = len(wgt) # n: 물건 개수
    bestVal = 0 # 배낭에 담을 수 있는 최대 가치

    for i in range(2**n):
        # 이진수의 비트 정보를 이용하여 어떤 물건을 담을지 결정
        # 예를 들어, n이 3일 경우 i가 0이면 이진수로 000이므로 물건을 하나도 담지 않는 경우의 수를 의미
        # i가 5이면 이진수로 101이므로 첫번째와 세번째 물건을 담는 경우의 수를 의미
        # 해당 경우의 수, 즉 부분 집합의 수가 2^n이므로 i에 0부터 2^n-1까지를 순서대로 대입
        s = [0]*n # 이진수를 저장할 리스트
        for d in range(n): # 이진수 계산
            s[d] = i % 2
            i = i // 2
        
        sumWgt = 0 # 현재 배낭의 무게
        sumVal = 0 # 현재 배낭의 가치

        for d in range(n):
            if s[d] == 1:
                sumWgt += wgt[d]
                sumVal += val[d]
        
        if sumWgt <= W and sumVal > bestVal:
            bestVal = sumVal
    
    return bestVal

if __name__ == '__main__':
    print(string_matching('HELLO WORLD', 'LO'))

    weight = [10, 20, 30, 25, 35]	# 물건별 무게
    value  = [60, 100, 120, 70, 85]	# 물건별 가치
    W = 80				            # 배낭의 제한 용량
    print("Knapsack01-BruteForce:", Knapsack_BF(weight, value, W))

