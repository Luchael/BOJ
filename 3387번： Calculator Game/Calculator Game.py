#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 3387                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/3387                           #+#        #+#      #+#     #
#    Solved: 2025/02/25 14:46:39 by luchael       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
k = int(input())
if k%16==0 or k%25==0 or k%10==0: print("Impossible")
elif k<10: print(k, "1")
else:
    for j in range(1,501):
        a=int('1'*j)
        for i in range(1,10):
            if (a*i)%k==0: print(str(a*i)[0], len(str(a)));exit()