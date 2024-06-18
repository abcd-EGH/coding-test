# 문제: 완주하지 못한 선수
# https://school.programmers.co.kr/learn/courses/30/lessons/42576

'''
1. 정렬
2. 첫번째부터 하나씩 비교
3. 다르면 participant의 사람을 return
4. 마지막까지 나오지 않을 경우 마지막 participant의 사람을 return
'''

def solution(participant, completion):
    participant.sort() # 1. 정렬
    completion.sort() # 1. 정렬
    for p,c in zip(participant, completion): # 2. 첫번째부터 하나씩 비교
        if p != c: # 3. 다르면 participant의 사람을 return
            return p
    return participant[-1] # 마지막까지 나오지 않을 경우 마지막 participant의 사람을 return

if __name__ == "__main__":
    tests = [[["leo", "kiki", "eden"],["eden", "kiki"]],
             [["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"]],
             [["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]]]
    results = ["leo","vinko","mislav"]

    for idx, (test, result) in enumerate(zip(tests,results)):
        if solution(*test) == result:
            print(f'test{idx+1} 성공')
        else:
            print(f'test{idx+1} 실패')
            print(f'리턴값: {solution(*test)}')