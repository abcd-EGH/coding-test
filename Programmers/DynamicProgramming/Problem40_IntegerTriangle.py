def solution(triangle):
    for floor in range(1, len(triangle)):
        for i in range(len(triangle[floor])):
            if i == 0:
                triangle[floor][i] = triangle[floor][i] + triangle[floor-1][i]
            elif i == len(triangle[floor])-1:
                triangle[floor][i] = triangle[floor][i] + triangle[floor-1][i-1]
            else:
                triangle[floor][i] = max(triangle[floor][i]+triangle[floor-1][i-1], triangle[floor][i]+triangle[floor-1][i])
    
    return max(triangle[-1])

tests = [[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]], [[4], [3, 8], [8, 1, 0], [2, 7, 4, 4]]]
results = [30, 22]

for idx, (test, result) in enumerate(zip(tests,results)):
    if solution(test) == result:
        print(f'test{idx+1} 성공')
    else:
        print(f'test{idx+1} 실패')