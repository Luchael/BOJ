#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 5430                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/5430                           #+#        #+#      #+#     #
#    Solved: 2025/02/25 14:49:11 by luchael       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
for _ in range(int(input())):
    cmd=input();le=int(input())
    r, p = 0, [0, 0]
    if le!=0:
        l=input()[1:-1].split(',')
    else: input();l=[]
    for i in cmd:
        if i=='R':r+=1
        else: p[r%2]+=1
    else:
        if r%2: l.reverse();p[0],p[1]=p[1],le-p[0]
        else: p[1]=le-p[1]
        if p[0]>p[1]: print("error")
        else: print('['+','.join(l[p[0]:p[1]])+']')