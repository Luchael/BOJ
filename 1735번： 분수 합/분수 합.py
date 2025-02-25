#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1735                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1735                           #+#        #+#      #+#     #
#    Solved: 2025/02/25 14:17:59 by luchael       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
gcd = lambda a, b: a if b==0 else gcd(b,a%b)
a,b=map(int,input().split())
c,d=map(int,input().split())
g=gcd(b,d)
a=a*d//g+c*b//g
b*=d//g
g=gcd(a,b)
print(a//g,b//g)