#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1010                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1010                           #+#        #+#      #+#     #
#    Solved: 2025/02/25 14:00:07 by luchael       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
def f(a,b=0):
    k = 1
    for i in range(b+1,a+1):
        k*=i
    return k


def C(n, r):
    return f(n,r)//f(n-r)


import sys
input = sys.stdin.readline
for i in range(int(input())):
    a = list(map(int,input().split()))
    print(C(a[1],a[0]))
