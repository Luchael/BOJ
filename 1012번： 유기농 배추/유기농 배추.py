#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1012                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1012                           #+#        #+#      #+#     #
#    Solved: 2025/02/26 17:28:10 by luchael       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
sys.setrecursionlimit(10000)

m='[*map(int,input().split())]'

def dfs(x,y):
    if[x,y]in baechu:
        baechu.remove([x,y])
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)

for T in range(int(input())):
    answer=0
    baechu=[eval(m)for _ in range(eval(m)[2])]
    while baechu:
        dfs(*baechu[0])
        answer+=1
    print(answer)

# 숏코딩, 사실상 salt2000님의 코드에서 날먹했음
# 7년 전과의 버전 차이로 인해서 가능했던 날먹
# n=input;t=int
# for r in[0]*t(n()):
#  d={(*map(t,n().split()),)for _ in[0]*t(n().split()[2])}
#  while d:
#   s=[d.pop()];r+=1
#   while s:
#    x,y=s.pop()
#    for e in-2,0,2,4:
#     if{p:=(x+e//3,y+e%3-1,)}<=d:d-={p};s+=p,
#  print(r)