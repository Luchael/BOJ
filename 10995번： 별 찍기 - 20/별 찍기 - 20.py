#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10995                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10995                          #+#        #+#      #+#     #
#    Solved: 2025/02/25 15:14:19 by luchael       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n = int(input())
for i in range(n): print((['* ',' *'][i%2]*n).rstrip())