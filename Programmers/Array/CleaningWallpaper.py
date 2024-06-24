# 1. idx_row, idx_col을 활용해 파일들의 최소,최대 row와 column 찾기
# 2. 최대에서 최소를 뺀 값 return
# 2-1. 최대 row와 column은 1을 더한 값을 사용 -> 파일 드래그 시 row와 column이 한 칸씩 더 필요
def solution(wallpaper):
    min_row = 10e+6
    max_row = 0
    min_col = 10e+6
    max_col = 0
    for idx_row, row in enumerate(wallpaper):
        for idx_col, file in enumerate(row): 
            if file == '#':
                if idx_row < min_row: min_row = idx_row
                if idx_col < min_col: min_col = idx_col
                if idx_row + 1 > max_row: max_row = idx_row + 1
                if idx_col + 1 > max_col: max_col = idx_col + 1
    return [min_row, min_col, max_row, max_col]

if __name__ == "__main__":
    tests = [[".#...", "..#..", "...#."],["..........", ".....#....", "......##..", "...##.....", "....#....."],
             [".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."],["..", "#."]]
    results = [[0, 1, 3, 4],[1, 3, 5, 8],[0, 0, 7, 9],[1, 0, 2, 1]]

    for idx, (test, result) in enumerate(zip(tests,results)):
        if solution(test) == result:
            print(f'test{idx+1} 성공')
        else:
            print(f'test{idx+1} 실패')