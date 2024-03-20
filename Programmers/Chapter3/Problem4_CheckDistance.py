def solution(places):
    return [check(place) for place in places]

def check(place):
    for idx_row, row in enumerate(place):
        for idx_col, cell in enumerate(row):
            if cell != 'P':
                continue
            # 확인해야 할 경우의 수
            # 1. 밑에 사람이 있는 경우
            if idx_row != 4:
                if place[idx_row+1][idx_col] == 'P':
                    return 0
            # 2. 오른쪽에 사람이 있는 경우
            if idx_col != 4:
                if place[idx_row][idx_col+1] == 'P':
                    return 0
            # 3. 오른쪽 밑에 사람이 있는데 / 오른쪽과 밑에 파티션이 하나라도 없는 경우
            if idx_row != 4 and idx_col != 4:
                if place[idx_row+1][idx_col+1] == 'P' and (place[idx_row][idx_col+1] != 'X' or place[idx_row+1][idx_col] != 'X'):
                    return 0
            # 4. 왼쪽 밑에 사람이 있는데 / 왼쪽과 밑에 파티션이 하나라도 없는 경우
            if idx_row != 4 and idx_col != 0:
                if place[idx_row+1][idx_col-1] == 'P' and (place[idx_row][idx_col-1] != 'X' or place[idx_row+1][idx_col] != 'X'):
                    return 0
            # 5. 밑의 밑에 사람이 있는데 / 밑이 파티션이 아닌 경우
            if idx_row < 3:
                if place[idx_row+2][idx_col] == 'P' and place[idx_row+1][idx_col] != 'X':
                    return 0
            # 6. 오른쪽의 오른쪽이 사람이 있는데 / 오른쪽이 파티션이 아닌 경우
            if idx_col < 3:
                if place[idx_row][idx_col+2] == 'P' and place[idx_row][idx_col+1] != 'X':
                    return 0

    return 1

test = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
         ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
result = [1,0,1,1,1]

if solution(test) == result: print('test 성공')
else: print('test 실패')