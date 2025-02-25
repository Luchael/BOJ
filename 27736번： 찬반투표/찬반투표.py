#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 27736                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/27736                          #+#        #+#      #+#     #
#    Solved: 2025/02/25 15:47:48 by luchael       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
students = int(input())
result = [0,0,0]
for i in [*map(int,input().split())]: result[i]+=1
if result[0]>=students/2: print("INVALID")
elif result[1]>result[-1]: print("APPROVED")
else: print("REJECTED")