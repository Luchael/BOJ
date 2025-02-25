#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2239                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2239                           #+#        #+#      #+#     #
#    Solved: 2025/02/25 14:22:36 by luchael       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

def X (x,num):
    global board
    for i in range(9):
        if board[i][x]==num:
            return False
    return True

def Square(x, y, num):
    global board
    x,y = x-x%3,y-y%3
    for i in range(3):
        for j in range(3):
            if board[y+i][x+j]==num:
                return False
    return True


def sudoku(ind):
    global board, zero
    if len(zero)==ind:        
        print('\n'.join(list(map(lambda x: ''.join(list(map(str,x))),board))))
        exit(0)
    a = zero[ind]
    y,x=a[0],a[1]
    for k in range(1,10):
        if k not in board[y]:
            if X(x,k):
                if Square(x,y,k):
                    board[y][x]=k
                    sudoku(ind+1)
                    board[y][x]=0
    

input = sys.stdin.readline
board = [list(map(int,list(input().rstrip()))) for _ in range(9)]
zero = [(i,j) for i in range(9) for j in range(9) if board[i][j] == 0]
sudoku(0)