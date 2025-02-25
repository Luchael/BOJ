#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 5376                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/5376                           #+#        #+#      #+#     #
#    Solved: 2025/02/25 14:48:55 by luchael       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
def gcd(n,m):
    while m:
        n, m = m, n%m
    return n

for i in range(int(input())):
    line = input().rstrip(')')
    if '.' in line:
        a = line.split('.')
        r = a[1].split('(')
        a = a[0]
        if len(r)==2:
            b = r[0]
            r = r[1]
            bunmo = int('9'*len(r) + '0'*len(b))
            if len(b) == 0: b = '0'
            bunja = int(r)+int(b+'0'*len(r))-int(b) + bunmo*int(a)
        else:
            r = r[0]
            bunmo = int('1'+'0'*len(r))
            bunja = int(r)+int(a)*bunmo
        g = gcd(bunja, bunmo)
        if bunja%bunmo == 0:print(str(int(a)+1)+'/1')
        else: print(bunja//g, '/', bunmo//g, sep = '')
    else:
        print(line+'/1')