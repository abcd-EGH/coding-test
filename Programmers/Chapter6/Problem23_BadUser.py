# Example Solution 1
import re

def search(idx, visit, userId, answer, banPatterns):
    if idx == len(banPatterns):
        answer.add(visit)
        return
    
    for i in range(len(userId)):
        if (visit & (1 << i)) > 0 or not re.fullmatch(banPatterns[idx], userId[i]): continue
        
        search(idx + 1, visit | (1 << i), userId, answer, banPatterns)

def solution(userId, bannedId):
    answer = set()
    banPatterns = [x.replace('*', '.') for x in bannedId]
    search(0, 0, userId, answer, banPatterns)

    return len(answer)

# Example Solution 2 (with 순열)
from itertools import permutations
import re

def solution(user_id, banned_id):
    banned = ' '.join(banned_id).replace('*','.')
    answer = set()
    
    for i in permutations(user_id, len(banned_id)):
        if re.fullmatch(banned, ' '.join(i)):
            answer.add(''.join(sorted(i)))
    
    return len(answer)