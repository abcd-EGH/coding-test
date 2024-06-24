# 행렬의 덧셈
# https://school.programmers.co.kr/learn/courses/30/lessons/12950

def solution(arr1, arr2):
    for row_idx in range(len(arr1)):
        for col_idx in range(len(arr1[0])):
            arr1[row_idx][col_idx] += arr2[row_idx][col_idx]
    # answer = [[c+d for c,d in zip(a,b)] for a,b in zip(arr1,arr2)]
    return arr1

if __name__ == "__main__":
    tests = [[[[1,2],[2,3]],[[3,4],[5,6]]], [[[1],[2]],[[3],[4]]]]
    results = [[[4,6],[7,9]],[[4],[6]]]

    for idx, (test, result) in enumerate(zip(tests,results)):
        if solution(*test) == result:
            print(f'test{idx+1} 성공')
        else:
            print(f'test{idx+1} 실패')