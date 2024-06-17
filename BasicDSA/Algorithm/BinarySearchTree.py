class BSTNode: # 이진 탐색 트리 노드
    def __init__(self, key, value) -> None:
        self.key = key # 이진 탐색 트리는 key값으로 정렬됨 & 중복 허용 X
        self.value = value
        self.left = None
        self.right = None

def search_bst(n, key): # self.key가 key인 노드를 찾는 재귀 함수
    if n == None:
        return None
    elif key == n.key:
        return n
    elif key < n.key:
        return search_bst(n.left, key)
    else:
        return search_bst(n.right, key)

def search_value_bst(n, value): # self.value가 value인 노드를 찾는 재귀 함수
    if n == None:
        return None
    elif value == n.value:
        return n
    res = search_value_bst(n.left, value)
    if res:
        return res
    else:
        return search_value_bst(n.right, value)
    
def insert_bst(root, node): # 삽입 연산
    if root == None: # 공백 노드에 도달 시 이 위치에 노드를 삽입
        return node # node를 반환(이 노드가 현재 root 위치에 감)
    
    if node.key == root.key:
        return root # root는 변화 없음
    
    if node.key < root.key:
        root.left = insert_bst(root.left, node) # 왼쪽 서브 트리 갱신
    else:
        root.right = insert_bst(root.right, node) # 오른쪽 서브 트리 갱신

    return root

def delete_bst (root, key) : # 삭제 연산
    if root == None :       # 공백 트리
        return root

    # key가 루트보다 작으면 왼쪽 서브트리에서 삭제하고, left를 갱신
    if key < root.key :
        root.left = delete_bst(root.left, key)

    # key가 루트보다 크면 오른쪽 서브트리에서 삭제하고, right를 갱신
    elif key > root.key :
        root.right= delete_bst(root.right, key)

    # key가 루트와 같으면 root를 삭제
    else : 
        if root.left== None :   # 단말 노드이거나 오른쪽 자식만 가진 노드 삭제
            return root.right   # root 대신에 right로 대체

        if root.right== None :  # 왼쪽 자식만 가진 노드 삭제
            return root.left    # root 대신에 left로 대체


        # 2개의 자식을 모두 가진 경우
        succ = root.right
        while succ.left != None:
            succ = succ.left

        root.key = succ.key                     # 후계자의 데이터를 root에 복사
        root.value = succ.value                 
        root.right = delete_bst(root.right, succ.key)

    return root