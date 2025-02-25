#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 4056                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/4056                           #+#        #+#      #+#     #
#    Solved: 2025/02/25 14:46:58 by luchael       ###          ###   ##.kr     #
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
        return 1
    a = zero[ind]
    y,x=a[0],a[1]
    for k in range(1,10):
        if k not in board[y]:
            if X(x,k):
                if Square(x,y,k):
                    board[y][x]=k
                    if sudoku(ind+1):
                        return 1
                    board[y][x]=0
    

input = sys.stdin.readline
for _ in range(int(input())):
    error = 0
    board = [list(map(int,list(input().rstrip()))) for _ in range(9)]
    for i in range(9):
        ll=[0]*9
        ll2=[0]*9
        for j in range(9):
            n = board[i][j]
            n2 = board[j][i]
            if (n!=0 and n in ll) or (n2!=0 and n2 in ll2):
                print("Could not complete this grid.")
                print()
                error = 1
                break
            ll[j] = n
            ll2[j] = n2
        if error: break
    if error: continue
    for a in range(0,9,3):
        for b in range(0,9,3):
            ll=[0]*9
            for i in range(3):
                for j in range(3):
                    n = board[a+i][b+j]
                    if n != 0 and n in ll:
                        print("Could not complete this grid.")
                        print()
                        error = 1
                        break
                    ll[i]=n
                if error: break
            if error: break
        if error: break
    if error: continue
    zero = [(i,j) for i in range(9) for j in range(9) if board[i][j] == 0]
    if sudoku(0)==None: print("Could not complete this grid.")
    print()
