#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2920                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2920                           #+#        #+#      #+#     #
#    Solved: 2025/02/25 14:40:31 by luchael       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
a=input().split()
b=list('12345678')
if a==b:print('ascending')
elif a==list(reversed(b)):print('descending')
else: print('mixed')