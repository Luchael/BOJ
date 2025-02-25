#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1019                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1019                           #+#        #+#      #+#     #
#    Solved: 2025/02/25 14:06:59 by luchael       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
num = [0]*10
n = input()
N = int(n)

for i in range(len(n)):
    j = len(n)-i-1
    d = int(n[i])
    if j!=0:
        for m in range(d):            
            num[m] += 10**j
            num = list(map(lambda x: x+j*int(10**(j-1)), num))
        num[0]-=10**j
        num[d]+=N%10**j+1
    else:
        for k in range(1,d+1):
            num[k]+=1

print(' '.join(map(str,num)))