#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1007                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1007                           #+#        #+#      #+#     #
#    Solved: 2025/02/26 13:09:37 by luchael       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys, math, itertools

input = sys.stdin.readline

def getTotalSub(v1,v2): # 벡터 x_1 - x_2, y_1 - y_2
    result = [0,0]
    for i in range(len(v1)):
        result[0] += v1[i][0] - v2[i][0]
        result[1] += v1[i][1] - v2[i][1]
    return result

for _ in range(int(input())):
    vector = []
    for i in range(N:=int(input())):
        vector.append(list(map(int, input().split())))
    res = math.inf
    vectorC = list(itertools.combinations(vector, N//2))
    for i in range(len_vectorC:=len(vectorC)//2):
        res = min(res, (a:=getTotalSub(vectorC[i], vectorC[~i]))[0] ** 2 + a[1] ** 2)
    print(math.sqrt(res))