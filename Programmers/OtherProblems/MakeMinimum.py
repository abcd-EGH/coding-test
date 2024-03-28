def solution(A,B):
    answer = 0

    A.sort()
    B.sort(reverse=True)
    
    for a, b in zip(A,B):
        answer += a*b
    return answer

tests = [[[1, 4, 2],[5, 4, 4]],[[1,2],[3,4]]]
results = [29, 10]

for idx, (test, result) in enumerate(zip(tests,results)):
    if solution(*test) == result:
        print(f'test{idx+1} 성공')
    else:
        print(f'test{idx+1} 실패')

############
# 완전 탐색 #
############
from itertools import permutations

def solution_brute_force(A, B):
    # 배열 A의 모든 순열을 생성
    perm_A = permutations(A)
    min_sum = float('inf')  # 가능한 최소값을 저장하기 위한 변수 초기화

    for a_perm in perm_A:
        # 현재 순열과 배열 B의 요소들을 곱하여 누적된 값을 계산
        current_sum = sum(a*b for a, b in zip(a_perm, B))
        # 최소 누적값 갱신
        if current_sum < min_sum:
            min_sum = current_sum
            
    return min_sum


