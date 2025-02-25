#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1469                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1469                           #+#        #+#      #+#     #
#    Solved: 2025/02/25 14:15:17 by luchael       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
N = int(input())
X = sorted(list(set(map(int, input().split()))))

def dfs(Shome, a):
    if -1 not in Shome: print(' '.join(map(str, Shome)));exit(0)
    for i in X:
        shome = Shome.copy()
        if i in shome: continue
        index = shome.index(-1)
        if index+i+1>=N*2: continue
        if shome[index+i+1] == -1:
            shome[index+i+1], shome[index] = i, i
            dfs(shome, a+1)


if len(list(filter(lambda x: x>(N-1)*2 ,X))): print(-1);exit(0)

for i in X:
    shome = [-1]*(N*2)
    shome[0], shome[i+1] = i, i
    dfs(shome.copy(), 1)
print(-1)
