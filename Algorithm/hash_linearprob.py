# 문자열 탐색키에 대한 해시 함수
def hashFn(key, M):
    if isinstance(key, str):
        sum = 0
        for c in key: # 문자열 내 모든 문자에 대해
            sum += ord(c) # 그 문자의 아스키 코드 값을 sum에 더함
        return sum % M # 제산 함수 적용
    elif isinstance(key, int) or isinstance(key, float):
        return round(key) % M
    else:
        raise TypeError("The type of input parameter should be string or number(integer, float, ...).")

# 선형 조사법의 삽입 연산
def lp_insert(key, table): # key: 삽입할 레코드
    count = M = len(table) # M, count 변수에 테이블 크기를 저장
    id = hashFn(key, M) # id: key의 해시값
    while count > 0 and (table[id] != None and table[id] != -1): # 계산된 주소부터 비어 있는 위치를 찾고, 비어 있지 않으면 다음 위치를 조사. 이 과정은 최대 M번 진행
        # 이때 -1은 삭제된 레코드임을 표시
        id = (id + 1 + M) % M
        count -= 1
    if count > 0: # 빈 버킷을 찾아 while문을 빠져나왔을 경우 해당 버킷(위치)에 레코드 저장
        table[id] = key
    return

# 선형 조사법의 탐색 연산
# 1. 탐색 키가 입력되면 해시 주소를 계산
# 2. 해당 주소에 같은 키의 레코드가 있으면 탐색 성공
# 3. 만일 레코드가 존재하지 않을 경우, 해당 키의 레코드가 삽입되지 않은 경우이므로 None을 반환
# 4. 만일 레코드가 존재하지만 다른 키의 레코드일 경우, 다음 주소로 넘어가 2-1번 과정부터 다시 진행
def lp_search(key, table): # key: 탐색할 레코드
    count = M = len(table)
    id = hashFn(key, M) # id: key의 해시값
    while count > 0:
        if table[id] == key:
            return True
        elif table[id] == None:
            return False
        else:
            id = (id + 1 + M) % M
            count -= 1
    return False

# 선형 조사법의 삭제 연산
# 선형 조사법에서 항목이 아예 삭제될 경우 탐색이 불가능해질 수 있음
# 그러므로 빈 버킷을 None, -1 두 가지로 분류함
#   -> None은 한 번도 사용되지 않은 버킷, -1은 사용되었다가 비워진 버킷
# 탐색 과정은 한 번도 사용되지 않은 버킷, 즉 None을 만나야 중단
def lp_delete(key, table):
    count = M = len(table)
    id = hashFn(key, M)
    while count > 0:
        if table[id] == None:
            return False
        elif table[id] != -1 and table[id] == key:
            table[id] = -1
            return
        else:
            id = (id + 1 + M) % M
            count -= 1

if __name__ == '__main__':
    # 실수, 문자열, 정수 탐색키에 대한 해시 함수
    M = 13
    table = [None] * M
    print(hashFn(4545.7,M))
    print(hashFn("faker",M))
    print(hashFn(34543, M))

    # 선형 조사법 테스트 프로그램
    print("   최초:", table)
    lp_insert(45, table); print("45 삽입:", table)
    lp_insert(27, table); print("27 삽입:", table)
    lp_insert(88, table); print("88 삽입:", table)
    lp_insert(9, table);  print(" 9 삽입:", table)
    lp_insert(71, table); print("71 삽입:", table)
    lp_insert(60, table); print("60 삽입:", table)
    lp_insert(46, table); print("46 삽입:", table)
    lp_insert(38, table); print("38 삽입:", table)
    lp_insert(24, table); print("24 삽입:", table)
    lp_delete(60, table); print("60 삽입:", table)
    print("46 탐색:", lp_search(46, table))
    print("8 탐색:", lp_search(8, table))

    lp_insert("faker", table); print("faker 삽입:", table)
    print("faker 탐색", lp_search("faker", table))



