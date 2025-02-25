#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11082                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11082                          #+#        #+#      #+#     #
#    Solved: 2025/02/25 15:17:22 by luchael       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
from math import gcd

a = input()
if '.' not in a:
    print(a+'/1')
else: 
    num = a.split('.')
    natural = num[0]
    num = num[1].split('(')
    notR = num[0]
    if len(num)==2:
        r = num[1].replace(')','')
    else:
        r = '0'
    bunmo = int('9'*len(r)+'0'*len(notR))
    if notR=='':
        notR='0'
    bunja = int(notR+r)-int(notR)+int(natural)*bunmo
    g=gcd(bunmo, bunja)
    print(bunja//g,'/',bunmo//g,sep='')