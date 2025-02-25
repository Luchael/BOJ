#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1038                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1038                           #+#        #+#      #+#     #
#    Solved: 2025/02/25 14:07:36 by luchael       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
num=[0]*10

le=1

n=int(input())

while n:

    if n>=1023:print(-1);exit(0)

    num[-1]+=1

    for i in range(1,le):

        if num[-i]>=num[-i-1]:

            num[-i-1]+=1

            num[-i]=i-1

    if num[-le]==10: num[-le]=le-1;le+=1;num[-le]=le-1

    n-=1

print(int(''.join(map(str,num))))