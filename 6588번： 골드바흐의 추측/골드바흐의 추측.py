#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 6588                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/6588                           #+#        #+#      #+#     #
#    Solved: 2025/02/25 14:50:09 by luchael       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

input = sys.stdin.readline

prime = [True]*1000001

for i in range(3,1001,2):

    if prime[i]:

        for j in range(i,1000000//i+1,2):

            prime[i*j]=False

while True:

    num=int(input())

    if num==0: break

    a,b=3,num-3

    while b>=a:

        if(prime[a] and prime[b]):

            print(num,'=',a,'+',b)

            break

        a+=2

        b-=2

