#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1081                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1081                           #+#        #+#      #+#     #
#    Solved: 2025/02/25 14:09:23 by luchael       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
one = [0,1,3,6,10,15,21,28,36,45,0]
tensSum = lambda a,n: a*45*n*(10**(n-1)) + one[a-1]*10**n

def getSum(n):
    n.reverse()
    result = 0
    for i in range(len(n)):
        a = int(n[i])
        result += tensSum(a,i) + sum(map(int,n[i+1:]))*a*10**i
    return int(result)

L,U = map(list,input().split())
plus = 0
for i in U:
    plus+=int(i)

print(getSum(U)-getSum(L)+plus)