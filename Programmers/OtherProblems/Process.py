def solution(priorities, location):
    processes = [i for i in range(len(priorities))]
    answer = dict()
    execute_order = 1
    while len(processes) != 0:
        max_priorites = max(priorities)
        priority = priorities[0]
        process = processes[0]
        if priority != max_priorites:
            priorities.append(priority)
            priorities.remove(priority)
            processes.append(process)
            processes.remove(process)
        else:
            answer[process] = execute_order
            execute_order += 1
            priorities.remove(priority)
            processes.remove(process)
                
    return answer[location]

tests = [[[2, 1, 3, 2],2],[[1, 1, 9, 1, 1, 1],0]]
results = [1,5]

for idx, (test, result) in enumerate(zip(tests,results)):
    if solution(*test) == result:
        print(f'test{idx+1} 성공')
    else:
        print(f'test{idx+1} 실패')