#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 25304                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/25304                          #+#        #+#      #+#     #
#    Solved: 2025/02/25 15:43:20 by luchael       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
total = int(input())
n = int(input())
for i in range(n):
    value, count = list(map(int,input().split()))
    total-=value*count
print(["Yes","No"][total!=0])