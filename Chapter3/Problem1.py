# 교점에 별 만들기 - Level 2
# 문제 풀이 흐름
# 1. 주어진 직선에서 교점 구하기
# 2. 그중 정수 교점만 따로 변수로 저장
# 3. 교점을 모두 표현하는 최소한의 사각형 알아내기
# 4. 모든 교점을 *로 찍어 표현
# 5. 배열을 거꾸로 뒤집어 반환

# 1. 주어진 직선에서 교점 구하기
def solution(line):
    n = len(line)
    setStar = set() # 정수 교점이 중복될 경우 하나만 저장하기 위해 set을 사용
    x_max = y_max = -10e+10
    x_min = y_min = +10e+10
    for i in range(n):
        a,b,e = line[i]
        for j in range(j,n):
            c,d,f = line[j]
            if a*d - b*c == 0: continue
            # 2. 그중 정수 교점만 따로 변수로 저장
            x = (b*f-e*d)/(a*d-b*c)
            y = (e*c-a*f)/(a*d-b*c)
            if x.is_integer() and y.is_integer():
                x = int(x)
                y = int(y)
                setStar.add((x,y))
                if x > x_max : x_max = x
                if y > y_max : y_max = y
                if x < x_min : x_min = x
                if y < y_min : y_min = y
    # 3. 교점을 모두 표현하는 최소한의 사각형 알아내기
    x_len = abs(x_max - x_min) + 1 # ex. abs(4-2)+1 = 3 -> (4, #), (3, #), (2, #)
    y_len = abs(y_max - y_min) + 1 # ex. abs(4-2)+1 = 3 -> (#, 4), (#, 3), (#, 2)
    xy = [['.']*x_len for _ in range(y_len)]
    # 4. 모든 교점을 *로 찍어 표현
    for _ in range(len(setStar)):
        x, y = setStar.pop()
        xStar = x - x_min
        yStar = y - y_min
        xy[xStar][yStar] = '*'
    
    answer = list()
    for result in xy : answer.append(''.join(result))
    
    5. 배열을 거꾸로 뒤집어 반환
    return answer[::-1]
        
