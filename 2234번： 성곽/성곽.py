#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2234                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2234                           #+#        #+#      #+#     #
#    Solved: 2025/02/25 14:22:21 by luchael       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
from collections import deque
import sys

input = sys.stdin.readline
dx = [-1,0,1,0]
dy = [0,-1,0,1]
def bfs(ay,ax): #* 서 1  북 2  동 4  남 8
    q = deque()
    q.append((ay,ax))
    visited[ay][ax] = True
    size = 1
    while q:
        cy,cx = q.popleft()
        for a in range(4):
            if (1<<a) & castle[cy][cx] == 0:
                gx, gy = dx[a] + cx, dy[a] + cy
                if 0<=gx<x and 0<=gy<y and not visited[gy][gx]:
                    visited[gy][gx] = True
                    q.append((gy,gx))
                    size+=1
    return size

x,y = map(int, input().split())
castle = [list(map(int,input().split())) for _ in range(y)]
visited = [[False]*x for _ in range(y)]
roomN = 0
roomS = 0

# 안 간 곳 찾기
for i in range(y):
    for j in range(x):
        if not visited[i][j]:
            roomN += 1
            roomS = max(roomS, bfs(i,j))

new_room_size = 0
for i in range(y):
    for j in range(x):
        for k in range(4):
            if (1<<k) & castle[i][j] != 0:
                visited = [[False]*x for _ in range(y)]
                castle[i][j] -= (1<<k)
                new_room_size = max(new_room_size, bfs(i,j))
                castle[i][j] += (1<<k)
print(roomN)
print(roomS)
print(new_room_size)