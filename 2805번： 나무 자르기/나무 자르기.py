#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2805                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2805                           #+#        #+#      #+#     #
#    Solved: 2025/02/25 14:39:10 by luchael       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys,math

input=sys.stdin.readline

N,M=map(int,input().split())

trees=list(map(int,input().split()))

trees.sort(reverse=True)

cut = 0

for i in range(N-1):

 if cut+(trees[i]-trees[i+1])*(i+1)<M:

  cut+=(trees[i]-trees[i+1])*(i+1)

 else: print(math.floor(trees[i]-(M-cut)/(i+1)));exit(0)

print(max(math.floor(trees[N-1]-(M-cut)/N),0))