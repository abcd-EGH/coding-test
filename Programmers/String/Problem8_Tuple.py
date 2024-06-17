def solution(s):
    if '},{' in s:
        s_list = s[2:-2].split('},{')
    else:
        s_list = [s[2:-2]]
        
    result = list()
    for element in s_list:
        if ',' in element:
            result.extend(element.split(','))
        else:
            result.append(element)
    
    answer = dict()
    for res in result:
        res = int(res)
        if res in answer:
            answer[res] += 1
        else:
            answer[res] = 1
    answer = sorted(answer.items(), key=lambda i: i[1], reverse = True)
    
    for i in range(len(answer)):
        answer[i] = answer[i][0]
    return answer

tests = ["{{2},{2,1},{2,1,3},{2,1,3,4}}", "{{1,2,3},{2,1},{1,2,4,3},{2}}",
         "{{20,111},{111}}", "{{123}}", "{{4,2,3},{3},{2,3,4,1},{2,3}}"]

results = [[2, 1, 3, 4], [2, 1, 3, 4], 	[111, 20], 	[123], [3, 2, 4, 1]]

for idx, (test, result) in enumerate(zip(tests, results)):
    if solution(test) == result:
        print(f'test {idx+1} 성공')
    else:
        print(f'test {idx+1} 실패')
        print('입력값:',test)
        print('출력값:',solution(test))