def solution(s):
    answer = [0, 0]
    while True: # s가 1이 될 때까지 이진 변환
        answer[0] += 1 # 변환을 시작하니 이진 변환의 횟수를 1 증가
        answer[1] += s.count('0') # 0의 개수를 count하여 더하기
        
        s = s.replace('0','') # 0을 모두 제거
        c = len(s) # s의 길이를 c에 저장
        
        nc = '' # s에 새로 저장할 c를 계산하기 위함
        if s == '1':
            break
        else:
            # while c != 1:
            while c // 2 != 0:
                pc = str(c % 2)
                nc = ''.join([nc,pc])
                c = c // 2
        s = ''.join(['1',nc[::-1]])
        
    return answer

tests = ["110010101001", "01110", "1111111"]
results = [[3,8],[3,3],[4,1]]

for idx, (test, result) in enumerate(zip(tests,results)):
    if solution(test) == result:
        print(f'test{idx} 성공')
    else:
        print(f'test{idx} 실패')
        print('입력값:',test)
        print('출력값:',solution(test))