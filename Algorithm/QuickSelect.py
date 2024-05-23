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
        return quickSelect(A, pos+1, right, k-(pos+1-left)) # left를 pos + 1로 설정하여 피벗의 오른쪽 리스트에서 다시 찾기

def partition(iteration, left, right):
    pivot = iteration[left]
    low = left + 1
    high = right

    while low <= high: # while low < high 시 제대로 정렬되지 않음
        while low <= right and iteration[low] <= pivot:
            low += 1
        while high >= left and iteration[high] > pivot:
            high -= 1
        
        if low < high:
            iteration[low], iteration[high] = iteration[high], iteration[low]
        
    iteration[left], iteration[high] = iteration[high], iteration[left]
    return high

if __name__ == "__main__":
    A = [1,3,5,2,6,7]
    print(quickSelect(A,0,len(A)-1,3))