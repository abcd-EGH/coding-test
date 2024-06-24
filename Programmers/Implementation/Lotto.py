# 로또의 최고 순위와 최저 순위
# https://school.programmers.co.kr/learn/courses/30/lessons/77484
'''
1. 최저 당첨 개수, 최대 당첨 개수 찾기
2. 최저 당첨의 경우: 0이 모두 당첨 번호가 아닌 경우
3. 최대 당첨의 경우: 0이 모두 당첨 번호인 경우
4. 최저 당첨 개수 = lottos 원소 중 win_nums에 들어가 있는 원소의 개수 (0 제외)
5. 최대 당첨 개수 = 최저 당첨 개수 + lottos 원소 중 0이 들어가 있는 개수
'''
def solution(lottos, win_nums):
    answer = [0,0] # [최저 당첨 개수, 최대 당첨 개수]
    for win_num in win_nums:
        if win_num in lottos:
            answer[0] += 1
    answer[1] = lottos.count(0) + answer[0]
    return [min(6,7-answer[1]),min(6,7-answer[0])]

if __name__ == "__main__":
    tests = [[[44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]],
             [[0, 0, 0, 0, 0, 0],[38, 19, 20, 40, 15, 25],],
             [[45, 4, 35, 20, 3, 9],[20, 9, 3, 45, 4, 35]]]
    results = [[3,5],[1,6],[1,1]]

    for idx, (test, result) in enumerate(zip(tests,results)):
        if solution(*test) == result:
            print(f'test{idx+1} 성공')
        else:
            print(f'test{idx+1} 실패')