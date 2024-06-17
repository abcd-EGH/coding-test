# 기능개발
def solution(progresses, speeds):
    times = []
    for progress, speed in zip(progresses, speeds):
        if (100 - progress) % speed == 0:
            times.append((100 - progress) / speed)
        else:
            times.append((100 - progress) // speed + 1)
    answer = [1]
    last_time = times[0]
    for time_index in range(1, len(times)):
        if last_time < times[time_index]:
            answer.append(1)
            last_time = times[time_index]
        else:
            answer[-1] += 1
    return answer

tests = [[[93, 30, 55], [1, 30, 5]], [[95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]]]
results = [[2,1],[1,3,2]]

for idx, (test, result) in enumerate(zip(tests,results)):
    if solution(*test) == result:
        print(f'test{idx+1} 성공')
    else:
        print(f'test{idx+1} 실패')