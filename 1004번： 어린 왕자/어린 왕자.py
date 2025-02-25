#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1004                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1004                           #+#        #+#      #+#     #
#    Solved: 2025/02/25 13:52:48 by luchael       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

d = lambda x1,y1,x2,y2: ((x2-x1)**2 + (y2-y1)**2)**0.5


for T in range(int(input())):
    x1,y1,x2,y2 = map(int,input().split())
    in_out = 0

    for i in range(int(input())):
        cx,cy,r = map(int,input().split())
        if (d(x1,y1,cx,cy)>r) != (d(x2,y2,cx,cy)>r): in_out +=1

    print(in_out)