# 모의고사
# https://school.programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    scores = [0,0,0] # 각 수포자의 점수를 저장하는 리스트
    best = [] # 가장 많이 맞힌 사람이 누구인지 담을 리스트
    pick = {1: [1,2,3,4,5], 2:[2,1,2,3,2,4,2,5], 3:[3,3,1,1,2,2,4,4,5,5]} # 찍는 방법을 저장한 딕셔너리

    for idx, answer in enumerate(answers): # 답을 순환하여 확인하고 각 수포자의 찍는 방법에 따라 답과 일치하면 scores에 저장
        for i in range(3):
            if answer == pick[i+1][idx%len(pick[i+1])]:
                scores[i] += 1
                
    for idx, score in enumerate(scores): # 제일 높은 score를 가진 수포자만 best에 저장
        if score == max(scores):
            best.append(idx+1)
            
    return best

if __name__ == "__main__":
    tests = [[1,2,3,4,5],[1,3,2,4,2]]
    results = [[1],[1,2,3]]

    for idx, (test, result) in enumerate(zip(tests,results)):
        if solution(test) == result:
            print(f'test{idx+1} 성공')
        else:
            print(f'test{idx+1} 실패')