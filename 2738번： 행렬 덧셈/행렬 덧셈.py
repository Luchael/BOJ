#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2738                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2738                           #+#        #+#      #+#     #
#    Solved: 2025/02/25 14:34:56 by luchael       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n,m = list(map(int,input().split()))
k=[]
for i in range(n):
    k.append(list(map(int,input().split())))

for h in range(n):
    for i,j in enumerate(list(map(int,input().split()))):
        k[h][i] = str(k[h][i]+j)
    k[h]=' '.join(k[h])
    
print('\n'.join(k))
