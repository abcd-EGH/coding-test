def solution(numbers):
    if int(''.join([str(number) for number in numbers])) == 0:
        return '0'
    numbers.sort(key=lambda x: transform(str(x)), reverse=True)
    
    return ''.join([str(number) for number in numbers])

def transform(x):
    if len(x) == 1:
        return ''.join([x,x,x,x])
    if len(x) == 2:
        return ''.join([x,x])
    if len(x) == 3:
        return ''.join([x,x[0]])
    if len(x) == 4:
        return x
    
tests = [[6, 10, 2],[3, 30, 34, 5, 9],[0,0,0]]
results = ["6210","9534330","0"]

for idx, (test, result) in enumerate(zip(tests,results)):
    if solution(test) == result:
        print(f'test{idx+1} 성공')
    else:
        print(f'test{idx+1} 실패')
