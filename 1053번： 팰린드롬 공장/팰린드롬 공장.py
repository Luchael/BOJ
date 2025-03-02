#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1053                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1053                           #+#        #+#      #+#     #
#    Solved: 2025/03/02 20:56:15 by luchael       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
from itertools import *
string = [*input()]
length = len(string)
def solution(l, r, dp):
    for i, j in [(1,0),(0,1),(1,1)]:
        if dp[l+i][r-j] == length:
            solution(l+i, r-j, dp)
        dp[l][r] = min(dp[l][r], dp[l+i][r-j]+int(not(i and j and string[l] == string[r])))

def solve():
    if length==1: return 0
    dp = [[length * int(i<j) for j in range(length)] for i in range(length)]
    solution(0, length-1, dp)
    return dp [0][-1]

answer = solve()

for i, j in combinations(range(length), 2):
        string[i], string[j] = string[j], string[i]
        answer = min(answer, solve()+1)
        string[i], string[j] = string[j], string[i]

print(answer)