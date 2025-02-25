#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1017                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1017                           #+#        #+#      #+#     #
#    Solved: 2025/02/25 14:05:42 by luchael       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

def dfs(n):
    if visited[num2.index(n)]:
        return False
    visited[num2.index(n)] = True
    for m in num2:
        if m+n in prime:
            if m not in primeSet or dfs(primeSet[m]):
                primeSet[m] = n
                return True
    return False

input()
num = list(map(int, input().split()))
odd, even = list(filter(lambda x:x%2==1,num)), list(filter(lambda x:x%2==0,num))
if len(odd)!=len(even): print(-1);exit()
k = num.pop(0)
[odd,even][k%2].sort()

prime = [True]*2001
prime[0], prime[1] = False,False
for i in range(2,45):
    if prime[i]:
        for j in range(i,int(2000/i)+1):
            prime[i*j] = False
prime = [i for i in range(2000) if prime[i]]

answer = []
for i in [odd,even][k%2]:
    primeSet = {}
    if k+i in prime:
        num2 = num.copy()
        del num2[num2.index(i)]
        if len(num2)==0: print(i);exit()
        for n in num2:
            visited = [False for _ in range(len(num2))]
            dfs(n)
    if len(primeSet) == len(num)-1 != 0:
        answer.append(i)
    

    
if not answer: print(-1)
else: print(' '.join(map(str,answer)))