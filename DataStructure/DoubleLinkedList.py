from Node import Node

class DoubleLinkedList:
    def __init__(self, size):
        self.size = size
        self.num = 0        
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.pre = self.head

    def insert(self, value):
        if self.num >= self.size:
            return False

        node = Node(value)

        self.head.next.pre = node
        node.next = self.head.next
        self.head.next = node
        node.pre = self.head
        self.num += 1
        return True

    def traverse(self): # 모든 원소 출력
        cur = self.head.next

        while cur != self.tail:
            print(cur.data, end=" ")
            cur = cur.next
        print()

    def remove(self, value): # 원소 제거 (인덱스가 낮은 원소 우선 제거)
        cur = self.head.next

        while cur != self.tail:
            if cur.data == value:
                cur.next.pre = cur.pre
                cur.pre.next = cur.next
                self.num -= 1
                return True
            cur = cur.next

        return False

    def remove_at_last(self): # list.pop()과 동일
        if self.num == 0:
            return None
        node = self.tail.pre
        self.tail.pre.pre.next = self.tail
        self.tail.pre = self.tail.pre.pre
        self.num -= 1
        return node


linked_list = DoubleLinkedList(10)
linked_list.insert(2)
linked_list.insert(3)
linked_list.insert(2)
linked_list.insert(5)
linked_list.insert(4)
linked_list.insert(2)
linked_list.traverse()
linked_list.remove(2)
linked_list.remove_at_last()
linked_list.traverse()