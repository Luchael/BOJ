#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10997                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10997                          #+#        #+#      #+#     #
#    Solved: 2025/02/25 15:14:40 by luchael       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n = int(input())
N, cnt = (n-1)*4, 1
star, rStar = '* ', ' *'
if n==1: print('*');exit(0)
print('*'*((n-1)*4+1))
for i in range((n-1)*2):
    print(star*cnt, end='')
    if i%2:
        print('*'*((n-cnt)*4-1),end='')
        cnt+=1
        print(rStar*(cnt-2))
    else:
        if i==0: continue
        print(' '*(n-cnt)*4,end='')
        print(star*(cnt-1))
        #print(rStar*cnt)

cnt-=1
for i in range(n*2):
    print(star*cnt, end='')
    if i%2 or i==0:
        print('*'*((n-1-cnt)*4+1), end='')
        print(rStar*cnt)
    else:
        print(' '*((n-1-cnt)*4+1), end='')
        print(rStar*cnt)
        cnt-=1