﻿#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1712                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1712                           #+#        #+#      #+#     #
#    Solved: 2025/02/25 14:17:27 by luchael       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
a,b,c=map(int, input().split(" "))
if b>=c:
    print(-1)
else:
    print(int(1+a/(c-b)))