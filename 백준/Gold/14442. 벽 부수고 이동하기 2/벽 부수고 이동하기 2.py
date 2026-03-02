from collections import deque
import sys; input=sys.stdin.readline
n,m,k=map(int,input().split())
dx,dy=[0,0,1,-1],[1,-1,0,0]
board=[list(input())[:-1] for _ in range(n)]
visited=[[[0 for _ in range(k+1)] for _ in range(m)] for _ in range(n)]
deq=deque()
deq.append((0,0,k))
visited[0][0][k]=1
def solve():
    while deq:
        cx,cy,dest=deq.popleft()
        if cx==n-1 and cy==m-1:
            return visited[cx][cy][dest]
        for i in range(4):
            nx,ny=cx+dx[i],cy+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if board[nx][ny]=='1' and dest:
                    if not visited[nx][ny][dest-1]:
                        deq.append((nx,ny,dest-1))
                        visited[nx][ny][dest-1]=visited[cx][cy][dest]+1
                elif board[nx][ny]=='0' and not visited[nx][ny][dest]:
                    deq.append((nx,ny,dest))
                    visited[nx][ny][dest]=visited[cx][cy][dest]+1
    return -1

print(solve())