import time

# 문제 풀이 흐름
# 1. n x n 2차원 배열 생성
# 2. 반시계 방향의 나선형으로 배열을 채움
# 3. 배열의 끝에 닿으면 '방향을 바꿈'
# 4. 마지막으로 할당할 숫자가 0이 아닐 때/삼각형을 모두 채웠다면 정답을 제출
def solution(n):
    answer  = list()
    # n x n 2차원 삼각형 배열 생성
    arr = [[0]*(i+1) for i in range(n)]
    dx = [0,1,-1]
    dy = [1,0,-1]
    # dx[0],dy[0] -> (0,1) 아래 방향
    # dx[1],dy[1] -> (1,0) 오른쪽 방향
    # dx[2],dy[2] -> (-1,-1) 왼쪽위 대각선 방향
    x = y = angle = 0 # x,y: 현재 좌표
    cnt = 1
    limit = int((n+1)*n/2)
    while cnt <= limit:
        arr[y][x] = cnt
        ny = y + dy[angle] # nx, ny: 다음 좌표 (next x, next y)
        nx = x + dx[angle]
        cnt += 1
        if 0 <= ny < n and 0 <= nx <= ny and arr[ny][nx] == 0:
            # 0 <= ny < n: 다음 y 좌표는 n보다 작아야 한다.
            # 0 <= nx <= ny: 다음 x좌표는 다음 y좌표보다 작거나 같아야 한다.
            # arr[ny][nx] == 0: 다음 좌표에 값이 0이어야 한다.
            # 위 조건이 만족될 경우 현재 좌표를 다음 좌표로 변경한다.
            y, x = ny, nx
        else:
            # 위 조건이 만족하지 않을 경우 회전해야 한다.
            # 1. 각도를 바꾼다 (angle 값을 변경, 0->1, 1->2, 2->0).
            # 2. 바꾼 각도로 한 번 움직인다.
            angle = (angle + 1) % 3
            y += dy[angle]
            x += dx[angle]
    # for floor in arr:
    #     answer.extend(floor)
    # return answer
    return [i for j in arr for i in j]

startTime = time.time()
tests = [[4, [1,2,9,3,10,8,4,5,6,7]],
        [5, [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]],
        [6, [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]]]

for idx, test in enumerate(tests):
    if solution(test[0]) == test[1]:
        print(f"test{idx+1} 성공")
    else: print(f"test{idx+1} 실패")

print("time: ",(time.time()-startTime))