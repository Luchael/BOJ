#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2581                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2581                           #+#        #+#      #+#     #
#    Solved: 2025/02/25 14:33:08 by luchael       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
i = int(input())
j = int(input())
s = [0, 0]
for i in range(i,j+1):
    if i==1: continue
    for k in range(round(i**0.5), 0, -1):
        if (k-1)==0:
            s[1]+=i
            if s[0]==0: s[0] = i
        if i%k==0: break

if s[0]!=0:
    print(s[1])
    print(s[0])
else: print(-1)