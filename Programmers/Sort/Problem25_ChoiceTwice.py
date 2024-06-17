def solution(numbers):
    answer = []
    numbers.sort()
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                answer.append(numbers[i]+numbers[j])
    answer = list(set(answer))
    answer.sort()
    return answer

tests = [[2,1,3,4,1], [5,0,2,7]]
results = [[2,3,4,5,6,7], [2,5,7,9,12]]

for idx, (test, result) in enumerate(zip(tests,results)):
    if solution(test) == result:
        print(f'test{idx+1} 성공')
    else:
        print(f'test{idx+1} 실패')