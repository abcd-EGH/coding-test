def sequential_search(A, key, low, high): # 순차 탐색
    for i in range(low, high+1):
        if A[i] == key:
            return i # 인덱스 반환
    return -1 # 탐색 실패 시 -1 반환

def sequential_search_transpose(A, key, low, high): # 순차 탐색 + 교환 전략
    for i in range(low, high+1):
        if A[i] == key: # 탐색 성공 시
            if i > low: # 맨 처음 요소가 아니면
                A[i], A[i-1] = A[i-1], A[i] # 교환 (transpose)
                i = i-1 # 탐색 대상 요소가 한 칸 앞으로 이동함
            return i
    return -1

def binary_search(A, key, low, high): # 이진 탐색 (A가 오름차순으로 정렬되어 있어야 함)
    if low <= high:
        middle = (low + high) // 2
        if key == A[middle]:
            return middle
        elif key < A[middle]: # 중앙값보다 작을 시
            return binary_search(A, key, low, middle - 1) # 재귀를 활용하여 앞 레코드들만 확인
        else: # 중앙값보다 클 시
            return binary_search(A, key, middle + 1, high) # 재귀를 활용하여 뒤 레코드들만 확인
    return -1

def binary_search_iter(A, key, low, high): # 이진 탐색 without 재귀
    while low <= high: # 재귀 대신 while문 활용
        middle = (low + high) // 2
        if key == A[middle]:
            return middle
        elif key < A[middle]:
            high = middle - 1 # high를 middle - 1로 바꾸어 재탐색
        else:
            low = middle + 1 # low를 middle + 1로 바꾸어 재탐색
    return -1