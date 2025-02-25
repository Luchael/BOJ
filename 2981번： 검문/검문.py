#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2981                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2981                           #+#        #+#      #+#     #
#    Solved: 2025/02/25 14:41:20 by luchael       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
from math import gcd, sqrt

n=int(input())

a,g=int(input()),int(input())

g=g-a

if g<0:g*=-1

for _ in range(n-2):

    k=int(input())

    p=a-k

    if p<0:p*=-1

    g=gcd(g,p)

    a=k

result=set()

result.add(g)

for i in range(2,int(sqrt(g))+1):

    if(g%i==0): result.add(i);result.add(g//i)

print(' '.join(list(map(str,sorted(list(result))))))
