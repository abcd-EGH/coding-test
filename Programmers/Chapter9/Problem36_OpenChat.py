def solution(record):
    msg = []
    id = {}
    for rec in record: # record를 돌면서 Enter와 Leave의 경우 닉네임이 아닌 아이디를 대신 msg에 저장
        rec_list = rec.split(' ')
        if rec_list[0] == 'Enter':
            id[rec_list[1]] = rec_list[2]
            msg.append(f"{rec_list[1]}님이 들어왔습니다.")
        if rec_list[0] == 'Leave':
            msg.append(f"{rec_list[1]}님이 나갔습니다.")
        else: # Change는 id에 저장된 닉네임을 유저 아이디에 대응하여 변경
            id[rec_list[1]] = rec_list[2]
            
    for msg_index in range(len(msg)):
        m_find = msg[msg_index].find("님") # "[아이디]님이 들어왔습니다(혹은 나갔습니다)."에서 아이디를 추출하기 위해 '님'이 들어간 인덱스를 찾음
        m_id = msg[msg_index][:m_find] # '님' 인덱스를 활용하여 id를 추출
        msg_rest = msg[msg_index][m_find:] # 나머지 문자열인 "님이 들어왔습니다(혹은 나갔습니다)"를 추출
        msg[msg_index] = ''.join([id[m_id],msg_rest]) # id와 나머지 문자열을 병합하여 다시 저장

    return msg

tests = [["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]]
results = [["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]]

for idx, (test, result) in enumerate(zip(tests,results)):
    if solution(test) == result:
        print(f'test{idx+1} 성공')
    else:
        print(f'test{idx+1} 실패')