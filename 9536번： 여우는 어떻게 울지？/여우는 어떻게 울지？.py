#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9536                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9536                           #+#        #+#      #+#     #
#    Solved: 2025/02/25 14:56:10 by luchael       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
for _ in range(int(input())):
    B = ' '+'  '.join(input().split())+' '
    while True:
        i = input().split()[2]
        if i=='the': break
        B=B.replace(' '+i+' ','')
    
    print(' '.join(B.split()))