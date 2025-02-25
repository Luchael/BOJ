#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2480                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2480                           #+#        #+#      #+#     #
#    Solved: 2025/02/25 14:28:12 by luchael       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
dice = list(map(int,input().split()))
gold,g=[0,0,1000,10000],0
for i in range(6):
    i+=1
    if dice.count(i)>1:g=gold[dice.count(i)];big=i;break
    elif dice.count(i)==1:big=i
print(g+big*100 if g<10000 else g+big*1000)