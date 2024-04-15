from collections import deque
import random

def selection_sort(iteration):
    for i in range(len(iteration)-1):
        least_idx = i
        for j in range(i+1, len(iteration)):
            if iteration[j] < iteration[least_idx]:
                least_idx = j
        iteration[i], iteration[least_idx] = iteration[least_idx], iteration[i]

def insertion_sort(iteration):
    for i in range(1, len(iteration)):
        key = iteration[i]
        j = i - 1
        while j >= 0 and iteration[j] > key:
            iteration[j+1] = iteration[j]
            j -= 1
        iteration[j+1] = key

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
    if __name__ == '__main__':
        print("left:", left, "right:", right)
        print("low:", low, "high:", high)
        print("iteration:", iteration)
    return high

def radix_sort(iteration, buckets, digits):
    queues = [deque() for _ in range(buckets)]
    # queues = [deque()] * buckets # 모든 요소가 같은 deque 객체를 참조함, 따라서 한 큐에 대해 popleft() 등의 작업을 수행하면 모든 queues 리스트 내의 요소가 영향을 받음
    print(queues)
    n = len(iteration)
    factor = 1
    for d in range(digits):
        for i in range(n):
            queues[(iteration[i]//factor) % buckets].append(iteration[i])

        i = 0
        for b in range(buckets):
            while queues[b]:
                iteration[i] = queues[b].popleft()
                i += 1
        factor *= buckets
        if __name__ == '__main__':
            print("step", d+1, iteration)

if __name__ == '__main__':
    a = [1,2,7,4,3,5,6,4]
    b = [random.randint(1,9999) for _ in range(10)]
    radix_sort(b, 10, 4)
    print(b)