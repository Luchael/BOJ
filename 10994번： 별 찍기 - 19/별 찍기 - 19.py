#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10994                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10994                          #+#        #+#      #+#     #
#    Solved: 2025/02/25 15:14:03 by luchael       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n = int(input())
N, cnt = (n-1)*4, 1
star, rStar = '* ', ' *'
print('*'*((n-1)*4+1))
for i in range((n-1)*2):
    print(star*cnt, end='')
    if i%2:
        print('*'*((n-1-cnt)*4+1), end='')
        print(rStar*cnt)
        cnt+=1
    else:
        print(' '*((n-1-cnt)*4+1), end='')
        print(rStar*cnt)

cnt-=1 
for i in range((n-1)*2):
    print(star*cnt, end='')
    if i%2:
        print('*'*((n-1-cnt)*4+1), end='')
        print(rStar*cnt)
    else:
        print(' '*((n-1-cnt)*4+1), end='')
        print(rStar*cnt)
        cnt-=1