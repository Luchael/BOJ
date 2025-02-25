#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 4373                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/4373                           #+#        #+#      #+#     #
#    Solved: 2025/02/25 14:48:05 by luchael       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n==0: break

    num = [0]*n # 숫자를 담을 배열
    add = {}
    sub = {}
    # 숫자 입력
    for i in range(n):
        num[i] = int(input())
    
    for i in range(n):
        for j in range(i+1,n):
            M, m = num[i], num[j]
            try:
                add[M+m].append(M,m)
            except:
                add[M+m] = [(M,m)]
    for i in range(n):
        for j in range(n):
            if i==j: continue
            M, m = num[i],num[j]
            try:
                sub[M-m].append(M,m)
            except:
                sub[M-m] = [(M,m)]

    add = sorted(add.items(),reverse=True)
    answer = -536870913
    for i in add:
        try:
            sub[i[0]]
            for j in i[1]:
                for k in sub[i[0]]:
                    if j[0]!=k[0]!=j[1]!=k[1]!=j[0]:
                        answer = max(k[0], answer)
        except:
            continue

    print([answer,"no solution"][answer == -536870913])