def solution(operations):
    queue = list()
    for opt in operations:
        if opt[0] == 'D' and len(queue) == 0: # 빈 큐 데이터 삭제 시 해당 연산 무시
            continue
        # 숫자 확인
        num = opt[2:]
        # 입력 연산
        if opt[0] == 'I':
            queue.append(int(num))
        elif opt[0] == 'D':
            if num == "1":
                queue.pop(queue.index(max(queue)))
            elif num == "-1":
                queue.pop(queue.index(min(queue)))
    if len(queue) == 0:
        return [0,0]
    return [max(queue), min(queue)]

if __name__ == "__main__":
    tests = [["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"],
             ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]]
    results = [[0,0], [333,-45]]

    for idx, (test, result) in enumerate(zip(tests,results)):
        if solution(test) == result:
            print(f'test{idx+1} 성공')
        else:
            print(f'test{idx+1} 실패')