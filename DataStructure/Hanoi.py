def hanoi_tower(n, start, temp, end):
    if n == 1:
        print("원판 1: %s -> %s"%(start, end))
    else:
        hanoi_tower(n-1, start, end, temp)
        print("원판 %d: %s -> %s"%(n, start, end))
        hanoi_tower(n-1, temp, start, end)

hanoi_tower(4, 'A', 'B', 'C')