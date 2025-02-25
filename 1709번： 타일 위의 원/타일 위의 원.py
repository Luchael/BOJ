#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1709                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1709                           #+#        #+#      #+#     #
#    Solved: 2025/02/25 14:16:19 by luchael       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n = int(input())
n//=2
distance = lambda x,y: (x**2+y**2)
now = [0,n]
result = 0
while now[1]!=0:
    D, N = distance(now[0],now[1]), n**2
    if D<N: now[0]+=1
    elif D==N: now[0]+=1;now[1]-=1
    else: now[1]-=1
    result +=1
print(result*4)