#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 21184                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/21184                          #+#        #+#      #+#     #
#    Solved: 2025/02/25 15:39:40 by luchael       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
s = str(input())

def carryless(a):
    arr = [0 for _ in range(len(a)*2-1)]
    for i in range(len(a)):
        for j in range(len(a)):
            arr[i+j] += int(a[i])*int(a[j])
            arr[i+j] %= 10
    return "".join(map(str,arr))

def dfs(b):
    g = carryless(b)
    if g == s:
        return b
    if len(g) >= len(s):
        return None
    if g[:len(b)] != s[:len(b)]:
        return None
    for i in range(10):
        x = dfs(b+str(i))
        if x:
            return x
    return None

print(dfs("") or "-1")