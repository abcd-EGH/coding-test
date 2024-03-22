def solution(numbers, hand):
    answer = ''
    
    l = [0, 0]
    r = [0, 2]
    num = dict()
    for i in range(1,9+1):
        num[i] = [3-int((i-1)//3), (i-1)%3]
    num[0] = [0, 1]
    
    for number in numbers:
        if number in [1, 4, 7]:
            answer = answer + 'L'
            l = num[number]
        elif number in [3, 6, 9]:
            answer = answer + 'R'
            r = num[number]
        else:
            sol, l, r = check(number, l, r, hand, num)
            answer = answer + sol
            # if sol == 'L':
            #     l = num[number]
            # else:
            #     r = num[number]
    return answer

def check(number, l, r, hand, num):
    # 유클리드 거라
    # l_distance = ((l[0]-num[number][0])**2+(l[1]-num[number][1])**2)**0.5
    # r_distance = ((r[0]-num[number][0])**2+(r[1]-num[number][1])**2)**0.5
    
    # 맨해튼 거리
    l_distance = abs(l[0]-num[number][0]) + abs(l[1]-num[number][1])
    r_distance = abs(r[0]-num[number][0]) + abs(r[1]-num[number][1])
    if l_distance < r_distance:
        return 'L', num[number], r
    elif l_distance > r_distance:
        return 'R', l, num[number]
    elif l_distance == r_distance:
        if hand == 'right':
            return 'R', l, num[number]
        else:
            return 'L', num[number], r
        
tests = [[[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"],
         [[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"],
         [[1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"]]
results = ["LRLLLRLLRRL", "LRLLRRLLLRR", "LLRLLRLLRL"]

for idx, (test, result) in enumerate(zip(tests,results)):
    if solution(*test) == result:
        print(f'test{idx+1} 성공')
    else:
        print(f'test{idx+1} 실패')