def evaluate(node):
    if node is None:
       return 0
    elif node.isLeaf():
       return node.data
    else:
        op1 = evaluate(node.left)
        op2 = evaluate(node.right)
        if node.data == '+' : return op1 + op2
        elif node.data == '-' : return op1 - op2
        elif node.data == '*' : return op1 * op2
        elif node.data == '/' : return op1 / op2

from BinaryTree import *
def buildETree(expr): # 후위표기 수식을 이용해 수식트리를 만들고 root를 반환
    if len(expr) == 0 :                 
        return None

    token = expr.pop() # 후위표기이므로 마지막부터 token으로 사용
    if token in "+-*/" :                
        node = BTNode(token)            
        node.right= buildETree(expr)    
        node.left = buildETree(expr)    
        return node
    else :                              
        return BTNode(float(token))     

def buildETree2( expr ): # 전위표기 수식을 이용해 수식트리를 만들고 root를 반환
    if len(expr) == 0:                 
        return None

    token = expr.pop(0) # 전위표기이므로 처음부터 token으로 사용
    if token in "+-*/":                
        node = BTNode(token)            
        node.left = buildETree2(expr)   
        node.right= buildETree2(expr)   
        return node
    else :                              
        return BTNode(float(token))

if __name__ == "__main__":
    str = input("입력(후위표기): ")		# 후위표기식 입력
    expr = str.split()			        # 토큰 리스트로 변환
    print("토큰분리(expr): ", expr)
    root = buildETree(expr)			    # 후위표기 --> 수식트리
    print('\n전위 순회: ', end=''); preorder(root)
    print('\n중위 순회: ', end=''); inorder(root)
    print('\n후위 순회: ', end=''); postorder(root)
    print('\n계산 결과 : ', evaluate(root))	# 수식트리 계산