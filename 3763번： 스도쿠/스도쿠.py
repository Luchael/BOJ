#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 3763                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/3763                           #+#        #+#      #+#     #
#    Solved: 2025/02/27 14:27:16 by luchael       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
# A~P

def solution():
    for y in range(SIZE):
        for x in range(SIZE):
            if sudoku[y][x] == -20:
                for i in  check(y, x):
                    ExactCover[y][x][i] = True
            else:
                ExactCover[y][x][sudoku[y][x]] = True
    print(ExactCover)
    
    
    return sudoku

def check(y, x):
    return [v for v in range(SIZE) if v not in sudoku[y] and v not in [sudoku[i][x] for i in range(SIZE)] and v not in [sudoku[i][j] for i in range(y//4*4, y//4*4+4) for j in range(x//4*4, x//4*4+4)]]

SIZE = 16
sudoku = [*map(lambda x:[*map(lambda y:ord(y)-65,[*str.strip(x)])],[*open(0)])]
ExactCover = [[[False]*SIZE for _ in range(SIZE)] for _ in range(SIZE)]

print(*solution(), sep="\n")