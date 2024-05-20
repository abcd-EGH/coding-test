def quickSelect(A, left, right, k):
    '''
        A: 대상 리스트
        left: 맨 왼쪽 인덱스
        right: 맨 오른쪽 인덱스
        k: k번째로 작은 수, k는 1부터 시작
    '''
    pos = partition(A, left, right)
    
    if pos + 1 == left + k: # case 1: k가 pos + 1인 경우
        return A[pos]
    elif pos + 1 > left + k: # case 2: k가 pos + 1보다 클 경우
        return quickSelect(A, left, pos-1, k) # right를 pos - 1로 설정하여 피벗의 왼쪽 리스트에서 다시 찾기
    else: # case 3: k가 pos + 1보다 작을 경우
        return quickSelect(A, pos+1, right, k) # left를 pos + 1로 설정하여 피벗의 오른쪽 리스트에서 다시 찾기
    
def partition(A, left, right):
    pivot = A[left]
    
