def solution(want, number, discount):
    answer = 0
    want_number = dict()
    for w, n in zip(want, number):
        want_number[w] = n
    for i in range(len(discount)-10 + 1):
        discount_10 = discount[i:i+10]
        # print(discount_10.count("chicken"))
        for w in want:
            if want_number[w] != discount_10.count(w):
                break
            if w == want[-1]:
                answer += 1
    return answer

tests = [[["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1],
          ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]],
         [["apple"], [10], ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]]]
results = [3,0]

for idx, (test, result) in enumerate(zip(tests,results)):
    if solution(*test) == result:
        print(f'test{idx+1} 성공')
    else:
        print(f'test{idx+1} 실패')