#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1040                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1040                           #+#        #+#      #+#     #
#    Solved: 2025/02/25 14:08:05 by luchael       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
def solution(n):
    n = list(n)
    i =len(n)-1
    used = [j for j in '0123456789' if j in n]

    while k-len(used)<0 or k-len(used)>len(n)-(i+1):
        if n[i] == '9':
            if i!=0:
                n[i]='0';i-=1;n[i]=str(int(n[i])+1)
                while n[i]=='10' and i!=0:
                    n[i]='0';i-=1;n[i]=str(int(n[i])+1)
                if i==0:
                    break
            else:
                break
        else:
            n[i] = str(int(n[i])+1)
        used = [j for j in '0123456789' if j in n[:i+1]]
    used = [j for j in '0123456789' if j in n[:i+1]]
    if n[i] == '10':
        used = []
        used.append('0')
        used.append('1')
    nused = [j for j in '0123456789' if j not in used]
    nused = nused[:k-len(used)]
    if k>len(used):
        for j in range(1,k-len(used)+1):
            n[-j] = nused[-j]
    elif k==len(used):
        for j in range(i+1,len(n)):
            n[j] = min(used)
    print(''.join(n))


N, K = input().split()
n, k=N, int(K)
if len(n)<k:
    #* N의 길이가 K 보다 작을 때
    num = list(range(k))
    num[0],num[1] = num[1],num[0] # 맨 앞에 1로 바꾸기
    print(''.join(map(str, num)))

else:
    solution(n)