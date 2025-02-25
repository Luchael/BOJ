#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 27513                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/27513                          #+#        #+#      #+#     #
#    Solved: 2025/02/25 15:44:14 by luchael       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n, m = map(int, input().split())
length = n*m
length -= length%2
board = [[0]*(n+1) for _ in range(m+1)]

print(length)

for i in range(n):
    print(i+1, 1)
for i in range(1,m):
    print(n, i+1)
for i in range(m,3,-1):
    if (m-i)%2:
        for j in range(n-1):
            print(j+1, i)
    else:
        for j in range(n-1,0,-1):
            print(j, i)
if m%2:
    for i in range(n-1,1,-1):
        if (n-i)%2:
            print(i, 3)
            print(i, 2)
        else:
            print(i, 2)
            print(i, 3)
    if not n%2:
        print(1,3)
    print(1,2)
else:
    if m!=2:
        for i in range(n-1):
            print(i+1, 3)
    for i in range(n-1,0,-1):
        print(i,2)