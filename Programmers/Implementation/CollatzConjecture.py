# 1. 우박수 좌표 저장하기 (y가 1이 될 때까지)
# 2. 범위 정적분
def solution(k, ranges):
    
    answer = list() # result
    klist = list() # 우박수 좌표 리스트
    x = 0 # 초기 우박수의 x 좌표
    
    # 1. 우박수 좌표 저장하기
    while True:
        klist.append([x, k])
        x += 1
        if k == 1:
            break
        elif k % 2 == 0:
            k /= 2
        elif k % 2 == 1:
            k = k * 3 + 1
    
    # 2. 범위 정적분
    for rng in ranges:
        value = 0 # 정적분 값
        x1 = rng[0]
        x2 = rng[1] + klist[-1][0]
        if x1 > x2: # x1이 x2보다 클 때 -1을 저장
            answer.append(-1.)
        elif x1 == x2: # x1과 x2가 같으면 0을 저장
            answer.append(0.)
        else:
            if x1 < 0: # x1이 0보다 작을 경우 0으로 초기화
                x1 = 0
            if x2 > klist[-1][0]: #x2가 마지막 우박수의 x좌표보다 클 경우 마지막 우박수의 x좌표로 초기화
                x2 = klist[-1][0]
            for x in range(x1, x2): # 범위 정적분 -> y1, y2값을 더하고 2로 나누기
                value += (klist[x][1] + klist[x+1][1])/2
            answer.append(value)
    return answer
	
if __name__ == "__main__":
    tests = [[5,[[0,0],[0,-1],[2,-3],[3,-3]]],
            [3,[[0,0], [1,-2], [3,-3]]]]
    results = [[33.0,31.5,0.0,-1.0], [47.0,36.0,12.0]]

    for idx, (test, result) in enumerate(zip(tests,results)):
        if solution(*test) == result:
            print(f'test{idx+1} 성공')
        else:
            print(f'test{idx+1} 실패')