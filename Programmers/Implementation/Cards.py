# 1. goal 리스트에서 순서대로 원소 뽑기
# 2. 각 cards 뭉치의 현재 인덱스에 해당 원소가 존재하는지 확인
# 3. 만약 없으면 "No" return
# 4. for문을 모두 돌았으면 "Yes" return
def solution(cards1, cards2, goal):
    idx1, idx2 = 0,0
    for word in goal: # 1. goal 리스트에서 순서대로 원소 뽑기
        if idx1 < len(cards1) and word == cards1[idx1]:
            idx1 += 1
        elif idx2 < len(cards2) and word == cards2[idx2]:
            idx2 += 1
        else:
            return "No"
        
    return "Yes"

if __name__ == "__main__":
    tests = [[["i", "drink", "water"],["want", "to"],["i", "want", "to", "drink", "water"]],
             [["i", "water", "drink"],["want", "to"],["i", "want", "to", "drink", "water"]]]
    results = ["Yes","No"]
    for idx, (test, result) in enumerate(zip(tests,results)):
        if solution(*test) == result:
            print(f'test{idx+1} 성공')
        else:
            print(f'test{idx+1} 실패')