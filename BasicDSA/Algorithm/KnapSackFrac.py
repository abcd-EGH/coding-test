def KnapSackFrac(wgt, val, W): # 각 물건들이 무게나 가치 등을 기준으로 '정렬되어 있지 않음'을 가정
    """
    wgt: 각 물건의 총 무게
    val: 각 물건의 총 가치
    W: 배낭의 제한 용량
    """
    bestVal = 0 # 최대 가치
    wgt_val = [[i,j] for i,j in zip(wgt, val)] # 각 물건의 무게와 가치를 리스트로 묶음
    wgt_val.sort(key = lambda x: x[1], reverse=True) # 가치 기준 내림차순으로 리스트를 정렬
    for i in wgt_val: # 가치가 높은 물건부터 분할 채우기
        if W <= 0: # 제한 용량이 0 이하일 경우 조기 종료
            break
        
        if i[0] < W: # 현재 물건의 총 무게보다 제한 용량이 클 경우
            bestVal += i[1]
            W -= i[0]
        else: # 현재 물건의 총 무게보다 제한 용량이 작을 경우 (현재 물건이 모두 들어가지 않을 경우)
            bestVal += i[1]/i[0] * W
            W = 0

    return bestVal

weight = [10, 8, 12]
value = [80, 60, 120]
W = 18
print(f"Fractional KnapSack({W}):", KnapSackFrac(weight, value, W))