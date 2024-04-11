from CircularQueue import CircularQueue

class BTNode:
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right
        
    def isLeaf(self):
        return self.left is None and self.right is None

def preorder(n): # 전위 순회
    if n is not None:
        print(n.data, end=' ')
        preorder(n.left)
        preorder(n.right)

def inorder(n): # 중위 순회
    if n is not None:
        inorder(n.left)
        print(n.data, end=' ')
        inorder(n.right) 

def postorder(n): # 후위 순회
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=' ')

def levelorder(root): # 레벨 순회
    queue = CircularQueue()
    queue.enqueue(root)
    while not queue.isEmpty():
        n = queue.dequeue()
        if n is not None:
            print(n.data, end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)

def count_node(n): # 이진 트리의 노드 수 구하기
    if n is None:
        return 0
    else:
        return count_node(n.left) + count_node(n.right) + 1

def calc_height(n): # 이진 트리의 높이 구하기 height = max(h_left, h_right) + 1
    if n is None:
        return 0
    hleft = calc_height(n.left)
    hright = calc_height(n.right)
    # if hleft > hright: return hleft + 1
    # else:              return hright + 1
    return max(hleft, hright) + 1

if __name__ == "__main__":
    d = BTNode('D', None, None)
    e = BTNode('E', None, None)
    b = BTNode('B', d, e)
    f = BTNode('F', None, None)
    c = BTNode('C', f, None)
    root = BTNode('A', b, c)

    print('\n   In-Order : ', end=''); inorder(root)
    print('\n  Pre-Order : ', end=''); preorder(root)
    print('\n Post-Order : ', end=''); postorder(root)
    print('\nLevel-Order : ', end=''); levelorder(root)
    print()
    
    print(" 노드의 개수 = %d개" % count_node(root))
    print(" 트리의 높이 = %d" % calc_height(root))
