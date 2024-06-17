# (x,y) 좌표에 퀸을 놓을 수 있는지 확인하는 함수
# 각 for문은 위쪽부터 순서대로 세로 방향, 왼쪽 대각선 방향, 오른쪽 대각선 방향에 퀸이 있는지 검사
def isSafe(board, x, y):
    N = len(board)

    for i in range(y): # 세로 방향은 (x,0)~(x,y-1)까지만 검사하면 됨
        if board[i][x] == 1:
            return False
    for i,j in zip(range(y-1,-1,-1), range(x-1,-1,-1)): # 왼쪽 대각선 검사
        # (i, j) = (y-1, x-1), (y-2, x-2), ..., (y-k, 0) 또는 (0, x-k)
        if board[i][j] == 1:
            return False
    for i,j in zip(range(y-1,-1,-1), range(x+1,N)): # 오른쪽 대각선 검사
        # (i, j) = (y-1, x+1),(y-2, x+2), ..., (0, x+k) 또는 (y-k, N-1)
        if board[i][j] == 1:
            return False
    
    return True # 모든 방향 검사를 통과하면 True를 반환

# 현재 보드에 0~y-1행까지는 퀸이 놓인 상태에서 y행부터 모든 행에 새로운 퀸을 놓는 알고리즘
def solve_N_Queen(board, y):
    N = len(board) # N x N board
    if y == N: # y가 N일 경우 모든 행의 Queen을 채운 것이므로 board를 출력
        printBoard(board)
        return
    for x in range(N):
        # 현재 y행의 모든 N개 열(x)에 대해, 유효한 열이면 다음을 처리하고 유효하지 않으면 백트래킹(다음 열로 이동)
        if isSafe(board, x, y): 
            board[y][x] = 1
            solve_N_Queen(board, y+1)
            board[y][x] = 0
    
def printBoard(board):
    N = len(board)
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()

if __name__ == "__main__":
    N = 5
    board = [[0 for _ in range(N)] for _ in range(N)]
    solve_N_Queen(board, 0)