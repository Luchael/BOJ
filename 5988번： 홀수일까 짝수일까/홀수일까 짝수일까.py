#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 5988                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/5988                           #+#        #+#      #+#     #
#    Solved: 2025/02/25 14:49:50 by luchael       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
print('\n'.join([["even","odd"][int(i)%2] for i in [*open(0)][1:]]))