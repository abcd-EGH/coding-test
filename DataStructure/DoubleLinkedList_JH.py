from Node import Node

class DoubleLinkedList_JH:
    def __init__(self):
        self.size = 0       
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.pre = self.head

    def insert(self, value, reverse = False):
        '''
        리스트 맨 뒤에 값 입력
        reverse = True: 리스트 맨 '앞'에 값 입력
        '''
        node = Node(value)

        if reverse == False:            
            self.tail.pre.next = node
            node.pre = self.tail.pre
            self.tail.pre = node
            node.next = self.tail
            self.size += 1
        
        else:
            self.head.next.pre = node
            node.next = self.head.next
            self.head.next = node
            node.pre = self.head
            self.size += 1
        
        return True

    def traverse(self): # 모든 원소 출력
        cur = self.head.next

        while cur != self.tail:
            print(cur.data, end=" ")
            cur = cur.next
        print()

    def remove(self, value, reverse = False):
        '''
        원소 제거 (인덱스가 낮은 원소 우선 제거)
        reverse = True: 인덱스가 높은 원소 우선 제거
        '''
        if self.size == 0:
            raise IndexError("remove from empty list")
        
        cur = self.head.next if reverse == False else self.tail.pre
        while cur != self.tail if reverse == False else self.head:
            if cur.data == value:
                cur.next.pre = cur.pre
                cur.pre.next = cur.next
                # self.num -= 1
                self.size -= 1
                return True
            cur = cur.next if reverse == False else cur.pre

        if cur == self.tail if reverse == False else self.head:
            raise ValueError("DoubleLinkedList.remove(x): x not in DoubleLinkedList")

        return

    def remove_at_last(self): # list.pop()과 동일
        if self.size == 0:
            raise IndexError("pop from empty list")
        
        node = self.tail.pre
        self.tail.pre.pre.next = self.tail
        self.tail.pre = self.tail.pre.pre
        # self.num -= 1
        self.size -= 1
        return node

    def __len__(self):
        return self.size

# linked_list = DoubleLinkedList_JH()
# insert_list = [2,3,2,5,2]
# for i in insert_list:
#     linked_list.insert(i)
# linked_list.traverse()
# print(len(linked_list))
# print()

# linked_list.remove(2)
# linked_list.remove_at_last()
# linked_list.traverse()
# linked_list.insert(2, reverse=True)
# linked_list.traverse()
# linked_list.remove(2, reverse=True)
# linked_list.traverse()
# print(len(linked_list))