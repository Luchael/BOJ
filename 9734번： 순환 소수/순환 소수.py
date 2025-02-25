#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9734                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9734                           #+#        #+#      #+#     #
#    Solved: 2025/02/25 14:57:01 by luchael       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
from sys import stdin
def gcd(n,m):
    while m:
        n, m = m, n%m
    return n

for line in stdin:
    line = line.rstrip(')\n')
    a = line.split('.')
    r = a[1].split('(')
    b = r[0]
    r = r[1]
    a = a[0]
    bunmo = int('9'*len(r) + '0'*len(b))
    if len(b) == 0: b = '0'
    bunja = int(r)+int(b+'0'*len(r))-int(b)
    bunja += bunmo*int(a)
    g = gcd(bunja, bunmo)
    print(line+')', '=', bunja//g, '/', bunmo//g)