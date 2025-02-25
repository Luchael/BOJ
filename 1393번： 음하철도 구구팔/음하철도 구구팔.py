#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1393                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1393                           #+#        #+#      #+#     #
#    Solved: 2025/02/25 14:14:24 by luchael       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

def gcd(n,m):
    while m:
        n, m = m, n%m
    return n


def d(x,y):
    return ((x-xs)**2 + (y-ys)**2)**0.5

input = sys.stdin.readline
xs, ys = map(int,input().split())
xe, ye, dx, dy = map(int, input().split())

g = gcd(dx,dy)
dx,dy = dx//g,dy//g
while d(xe,ye)>d(xe+dx, ye+dy):
    xe+=dx
    ye+=dy

print(xe,ye)
