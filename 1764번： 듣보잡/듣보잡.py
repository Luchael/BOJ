#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1764                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1764                           #+#        #+#      #+#     #
#    Solved: 2025/02/25 14:18:28 by luchael       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input=sys.stdin.readline
m, n = map(int,input().split())
saw={}
NotSawListen=[]
a=0
for _ in range(m):
    saw[input()]=True
for _ in range(n):
    name=input()
    try:
        if saw[name]:
            a+=1
            NotSawListen.append(name)
    except: pass
NotSawListen.sort()
print(a)
print(''.join(NotSawListen))