class Node:
    def __init__(self, data, link = None) -> None:
        self.data = data # 데이터 멤버 생성 및 초기화
        self.link = link # 링크 생성 및 초기화
    
    def append(self, node):
        if node is not None:
            node.link = self.link # 현재 인스턴스 노드(self)가 가지는 link를 입력받은 노드(node)에게 전달
            self.link = node # 현재 인스턴스 노드(self)의 link를 입력받은 node와 연결

    def popNext(self):
        next = self.link # 다음 노드를 next 변수가 가리키게 함
        if next is not None: # 만약 next가 존재할 경우, (현재 노드가 마지막이 아닐 경우,)
            self.link = next.link # 다음 노드(next)의 그 다음 노드를 현재 인스턴스 노드(self)와 연결
        return next # 삭제된 next를 반환
    
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.count = 0

    def isEmpty(self):
        return self.head == None
    
    def isFull(self):
        return False # 연결된 구조는 포화 상태 X

    def getNode(self, pos): # pos번째 노드를 반환
        if pos < 0: return None
        ptr = self.head # ptr에 현재 확인하고 있는 노드를 가리킴
        for i in range(pos):
            # if ptr == None: return None # ptr이 None을 가리키게 되면 None을 반환, 그러나 위에서 사이즈를 확인하므로 필요 없는 구문
            ptr = ptr.link # 현재 확인하고 있는 노드의 다음 노드로 이동
        return ptr # pos만큼 이동 후 현재 가리키고 있는 노드를 반환
    
    def getEntry(self, pos): # pos번째 요소를 반환
        node = self.getNode(pos)
        if node == None: return None
        else: return node.data

    def insert(self, pos, e):
        node = Node(e, None) # 삽입할 노드를 생성, link는 우선 None으로 설정 (e는 노드의 데이터)
        before = self.getNode(pos-1) # 삽입할 위치의 이전 노드를 탐색
        if before == None: # 이전 노드가 없을 경우 = 삽입할 위치가 head일 경우
            node.link = self.head # 현재 list의 head를 삽입할 노드의 link가 가리키도록 함
            self.head = node # 현재 list의 head를 삽입할 노드로 설정
        else: # 이전 노드가 존재할 경우
            before.append(node) # 이전 노드 뒤에 node를 추가
        self.count += 1
        return

    def delete(self, pos):
        before = self.getNode(pos-1) # 제거할 위치의 이전 노드를 탐색
        if before == None: # 이전 노드가 없을 경우
            before = self.head
            if self.head is not None:
                self.head = self.head.link
            self.count -= 1
            return before
        else:
            self.count -= 1
            return before.popNext()

    def size(self):
        # ptr = self.head
        # count = 0
        # while ptr is not None:
        #     ptr = ptr.link
        #     count += 1
        # return count
        return self.count # self.count가 없을 경우 위 구문을 사용
    
    def display(self):
        ptr = self.head
        while ptr is not None:
            print(ptr.data, end = '->')
            ptr = ptr.link
        print("None")