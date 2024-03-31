def solution(n, wires):
    min_diff = 10e+6
    for wire in wires: # 한 wire가 없는 모든 상황을 가정
        nwires = wires[:]
        nwires.remove(wire)
        con = [[nwires[0][0]], [nwires[0][1]]]
        print(con)
        for i in range(1,len(nwires)):
            if nwires[i][0] in con[0]:
                con[1].append(nwires[i][1])
            elif nwires[i][1] in con[1]:
                con[0].append(nwires[i][0])
            elif nwires[i][1] in con[0]:
                con[0] = nwires[i][0]
                con[1] = nwires[i][1]
            else:
                left = wires[:wires.index(wire)]
                right = wires[wires.index(wire)+1:]
                if len(left) + len(right) < min_diff:
                    min_diff = len(left) + len(right)
    return min_diff