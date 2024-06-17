def solution(n):
    ans = 1
    while True:
        if n == 1:
            break
        if n % 2 == 0:
            n /= 2
        elif n % 2 == 1:
            ans += 1
            n = (n - 1)/2
    return ans

if __name__ == "__main__":
    tests = [5,6,5000]
    results = [2,2,5]

    for idx, (test, result) in enumerate(zip(tests,results)):
        if solution(test) == result:
            print(f'test{idx+1} 성공')
        else:
            print(f'test{idx+1} 실패')