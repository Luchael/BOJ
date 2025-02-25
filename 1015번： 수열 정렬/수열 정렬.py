#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1015                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1015                           #+#        #+#      #+#     #
#    Solved: 2025/02/25 14:03:40 by luchael       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
i=input
a=int(i())
s=sorted(b:=list(map(int,i().split())))
used,answer=[a]*a,[a]*a
for i in range(len(b)):
    k = s.index(b[i])
    while k in used:
        k+=1
    used[i] = k
    answer[i] = k

print(*answer)