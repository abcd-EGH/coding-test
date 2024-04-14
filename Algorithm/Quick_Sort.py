def quick_sort(iteration, left, right):
    if left < right:
        q = partition(iteration, left, right)
        quick_sort(iteration, left, q - 1)
        quick_sort(iteration, q + 1, right)

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
    print("left:", left, "right:", right)
    print("low:", low, "high:", high)
    print("iteration:", iteration)
    return high

if __name__ == '__main__':
    a = [1,2,7,4,3,5,6,4]
    quick_sort(a, 0, len(a)-1)
    print(a)
