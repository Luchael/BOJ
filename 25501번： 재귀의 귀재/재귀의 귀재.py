#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 25501                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/25501                          #+#        #+#      #+#     #
#    Solved: 2025/02/25 15:43:45 by luchael       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
def recursion(s, l, r):
    global k
    k+=1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)



for i in range(int(input())):
    k = 0
    s = input()
    print(isPalindrome(s), k)