#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 13015                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/13015                          #+#        #+#      #+#     #
#    Solved: 2025/02/25 15:19:06 by luchael       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n = int(input())
if n==1: print('*');exit(0)
print('*'*n+' '*((n-1)*2-1)+'*'*n)
for i in range(1,n-1):
    print(' '*i+(' '*((n-i-1)*2-1)).join(['*'+' '*(n-2)+'*']*2))
print(' '*(n-1)+'*'+' '*(n-2)+'*'+' '*(n-2)+'*')
for i in range(n-2,0,-1):
    print(' '*i+(' '*((n-i-1)*2-1)).join(['*'+' '*(n-2)+'*']*2))
print('*'*n+' '*((n-1)*2-1)+'*'*n)