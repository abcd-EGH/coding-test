def solution(data, ext, val_ext, sort_by):
    result = list()
    sort_dict = {'code':0, 'date':1, 'maximum':2, 'remain':3}
    
    for d in data:
        if d[sort_dict[ext]] < val_ext:
            result.append(d)
            
    result.sort(key=lambda i: i[sort_dict[sort_by]])
    return result

data = [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]
ext = 'date'
val_ext = 20300501
sort_by = 'remain'

if solution(data, ext, val_ext, sort_by) == [[3,20300401,10,8],[1,20300104,100,80]]:
    print('test 성공')
else : print('test 실패')