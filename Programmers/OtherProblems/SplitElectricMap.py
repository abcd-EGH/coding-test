def solution(n, wires):
    for wire in wires:
        new_wires = wires[:].remove(wire) # 한 wire가 없는 모든 상황을 가정
        con = [0,1]
        for new_wire in new_wires:
            if con[1] == new_wire[0]:
                con[0], con[1] = new_wire[0], new_wire[1]
            elif con[1] == new_wire[1]:
                continue
            else:
                pass
    return wires