#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 27514                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/27514                          #+#        #+#      #+#     #
#    Solved: 2025/02/25 15:45:00 by luchael       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
input()
print(1<<len(bin(sum(map(int,input().split()))))-3)