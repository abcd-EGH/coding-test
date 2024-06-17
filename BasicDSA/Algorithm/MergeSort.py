def mergeSort(A, left, right):
    if left < right:
        mid = (left + right) // 2 # mid: 리스트를 균등하게 나누기 위한 인덱스
        mergeSort(A, left, mid) # 왼쪽 부분 병합 정렬
        mergeSort(A, mid + 1, right) # 오른쪽 부분 병합 정렬
        merge(A, left, mid, right) # 마지막 병합

def merge(A, left, mid, right):
    k = left # 병합을 위한 임시 리스트의 인덱스
    i = left # 왼쪽 리스트의 인덱스
    j = mid + 1 # 오른족 리스트의 인덱스
    while i <= mid and j <= right:
        if A[i] <= A[j]: # 왼쪽 리스트의 원소가 오른쪽 리스트 원소보다 작다면
            sorted_[k] = A[i] # 임시 리스트에 복사
            i, k = i+1, k+1 # 인덱스 증가
        else: # 왼쪽 리스트의 원소가 오른쪽 리스트 원소보다 크다면
            sorted_[k] = A[j]
            j, k = j+1, k+1
    if i > mid: # 왼쪽 리스트의 남은 부분을 임시 리스트로 복사
        sorted_[k:k+right-j+1] = A[j:right+1]
    else:
        sorted_[k:k+mid-i+1] = A[i:mid+1]
    A[left:right+1] = sorted_[left:right+1]

if __name__ == "__main__":
    A = [4,5,7,6,3,8,1,9]
    sorted_ = [None for _ in range(len(A))] # 병합을 위한 임시 전역 리스트
    mergeSort(A, 0, len(A)-1)
    print(A)