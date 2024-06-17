def solution(n):
    answer = []
    hanoi(n, 1, 3, 2, answer)
    return answer

def hanoi(n, start, to, mid, answer):
    if n == 1:
        return answer.append([start, to])
    hanoi(n-1, start, mid, to, answer)
    answer.append([start,to])
    hanoi(n-1, mid, to, start, answer)
        
tests = [2,3,4]
results = [[[1, 2], [1, 3], [2, 3]], [[1, 3], [1, 2], [3, 2], [1, 3], [2, 1], [2, 3], [1, 3]],
           [[1, 2], [1, 3], [2, 3], [1, 2], [3, 1], [3, 2], [1, 2], [1, 3], [2, 3], [2, 1], [3, 1], [2, 3], [1, 2], [1, 3], [2, 3]]]

for idx,(test,result) in enumerate(zip(tests,results)):
    if solution(test) == result:
        print(f'test{idx+1} 성공')
    else:
        print(f'test{idx+1} 실패')
        print('입력값:',test)
        print('출력값:',solution(test))