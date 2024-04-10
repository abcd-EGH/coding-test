from LinkedList import LinkedList

class DNode:
    def __init__(self, data, prev=None, next=None) -> None:
        self.data = data
        self.prev = prev
        self.next = next

    def append(self, node):
        if node is not None: # 삽입할 node가 존재할 경우
            node.next = self.next # 현재 노드의 next를 삽입할 노드의 next로
            node.prev = self # 현재 노드를 삽입할 노드의 prev로
            self.next = node # 삽입할 노드를 현재 노드의 next로
            if node.next is not None: # 삽입할 노드의 next가 존재할 경우
                node.next.prev = node
        return
    
    def popNext(self):
        node = self.next # 삭제할 노드 = 현재 노드의 next
        if node is not None: # 삭제할 노드가 존재하면
            self.next = node.next
            if node.next is not None:
                node.next.prev = self
        return node
    
class DblLinkedList(LinkedList):
    def __init__(self) -> None:
        super().__init__()

    def insert(self, pos, e):
        node = DNode(e) # 삽입할 노드를 생성, link는 우선 None으로 설정 (e는 노드의 데이터)
        before = self.getNode(pos-1) # 삽입할 위치의 이전 노드를 탐색
        if before == None: # 이전 노드가 없을 경우 = 삽입할 위치가 head일 경우
            node.next = self.head # 현재 list의 head를 삽입할 노드의 link가 가리키도록 함
            if node.next is not None: # 삽입한 노드의 next가 존재할 경우 = 현재 list의 head가 존재했을 경우
                node.next.prev = node # 삽입한 노드의 next의 prev를 삽입한 노드로 변경
            self.head = node # 현재 list의 head를 삽입할 노드로 설정
        else: # 이전 노드가 존재할 경우
            before.append(node) # 이전 노드 뒤에 node를 추가
        self.count += 1
        return

    def delete(self, pos):
        before = self.getNode(pos-1) # 제거할 위치의 이전 노드를 탐색
        if before == None: # 이전 노드가 없을 경우
            before = self.head
            if self.head is not None: # head가 존재할 경우
                self.head = self.head.next # 현재 head의 next를 head로
            if self.head is not None: # self.head.next가 존재했을 경우
                self.head.prev = None # 현재 head의 prev를 None으로
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
            print(ptr.data, end = '<=>')
            ptr = ptr.next
        print("None")