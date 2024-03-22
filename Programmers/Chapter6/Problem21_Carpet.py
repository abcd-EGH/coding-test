def solution(brown, yellow):
    grid = brown + yellow
    for y in range(1, int(grid**0.5)+1):
        if grid % y == 0 and (int(grid/y)-2)*(y-2)==yellow:
            return [int(grid/y),y]