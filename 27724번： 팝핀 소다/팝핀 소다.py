#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 27724                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/27724                          #+#        #+#      #+#     #
#    Solved: 2025/02/25 15:47:19 by luchael       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
M,N,K=map(int,input().split())
print(min(len(bin(M))-3,len(bin(K))-3+N))