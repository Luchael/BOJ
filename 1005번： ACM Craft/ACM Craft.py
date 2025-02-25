#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1005                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1005                           #+#        #+#      #+#     #
#    Solved: 2025/02/25 13:53:16 by luchael       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque
input = sys.stdin.readline

# 위상정렬
def topologicalSort(W):
    time = [0]*(N+1)
    q = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
            time[i] = cost[i]
    
    while q:
        current = q.popleft()
        if current==W: # 중단점
            return time[W]
        for i in graph[current]:
            indegree[i] -= 1
            time[i] = max(time[current]+cost[i], time[i])
            if indegree[i] == 0:
                q.append(i)


for _ in range(int(input())):
    #입력
    N, K = map(int, input().split())
    cost = [0]+list(map(int,input().split())) # 비?용
    indegree = [0]*(N+1)
    graph = {i:[] for i in range(N+1)}
    for __ in range(K):
        X, Y = map(int,input().split())
        indegree[Y] += 1
        graph[X].append(Y)
    W = int(input())
    print(topologicalSort(W))