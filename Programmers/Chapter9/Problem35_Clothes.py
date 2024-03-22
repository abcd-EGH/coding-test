# from itertools import product

def solution(clothes):
    answer = 1
    clothes_dict = dict()
    for (value, key) in clothes:
        if key in clothes_dict:
            clothes_dict[key].append(value)
        else:
            clothes_dict[key] = [value, 'None']
    for key in clothes_dict:
        answer *= len(clothes_dict[key])
    # case 수가 아닌 case 조합까지 확인해야 할 경우
    # case_list = list(product(*clothes_dict.values()))
    
    return answer-1 # [None, None, ...]인 경우를 제외해야 하므로 -1

tests = [[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]],
         [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]]
results = [5,3]

for idx, (test, result) in enumerate(zip(tests,results)):
    if solution(test) == result:
        print(f'test{idx+1} 성공')
    else:
        print(f'test{idx+1} 실패')