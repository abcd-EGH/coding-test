def solution(arr):
    answer = [0,0]
    comp(arr, answer)    
    return answer

# arr 배열과 answer 배열을 받아, arr 배열이 압축이 필요한지 확인
def comp(arr, answer):
    if sum([i for j in arr for i in j]) == 0: # 모두 0
        answer[0] += 1
    elif sum([i for j in arr for i in j]) == len(arr)**2: # 모두 1
        answer[1] += 1
    else: # 압축이 필요한 배열을 다시 comp에 answer 배열과 함께 입력
        half_side = int(len(arr)/2) # 한 변의 길이/2
        full_side = len(arr) # 한 변의 길이
        comp([arr[i][:half_side] for i in range(half_side)], answer) # arr를 4등분 후 '왼쪽 위' 배열을 comp에 다시 입력
        comp([arr[i][half_side:] for i in range(half_side)], answer) # arr를 4등분 후 '오른쪽 위' 배열을 comp에 다시 입력
        comp([arr[i][:half_side] for i in range(half_side, full_side)], answer) # arr를 4등분 후 '왼쪽 아래' 배열을 comp에 다시 입력
        comp([arr[i][half_side:] for i in range(half_side, full_side)], answer) # arr를 4등분 후 '오른쪽 아래' 배열을 comp에 다시 입력
        
tests = [[[1,0],[1,1]],
         [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]],
         [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]]
results = [[1,3],[4,9],[10,15]]

for idx, (test, result) in enumerate(zip(tests,results)):
    if solution(test) == result:
        print(f'test{idx+1} 성공')
    else:
        print(f'test{idx+1} 실패')
