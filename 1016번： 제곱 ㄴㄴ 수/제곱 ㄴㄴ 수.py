#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1016                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1016                           #+#        #+#      #+#     #
#    Solved: 2025/02/25 14:05:20 by luchael       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline
a,b=map(int,input().split())
table = [False]*(b-a+1)
i = 2
while i*i<=b:
    k = i*i
    plus = 1 if a%k else 0
    j = a//k+plus
    while k*j<=b:
        
        if not table[k*j-a]:
            table[k*j-a] = True
        j+=1
    i+=1
print(table.count(False))