#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2563                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2563                           #+#        #+#      #+#     #
#    Solved: 2025/02/25 14:31:21 by luchael       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
paper = [0 for i in range(10000)]
for i in range(int(input())):
    coor = list(map(int,input().split()))
    for x in range(coor[0],coor[0]+10):
        for y in range(coor[1],coor[1]+10):
            paper[x*100+y]=1
print(paper.count(1))