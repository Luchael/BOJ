#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1557                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1557                           #+#        #+#      #+#     #
#    Solved: 2025/03/02 23:15:37 by luchael       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
def count(n):
    result = 0
    nn = False
    x = [(1,-1,1)]
    while x:
        mul, start, pm = x.pop()
        for i in range(start + 1, p):
            mul_ = mul*prime[i]**2
            if mul_ > n:
                break
            nn |= not(n%mul_)
            result += n//mul_ * pm
            x.append((mul_, i, -pm))
    return n-result, nn
    

K = int(input())
prime = []
n_prime = [0]*50001

for i in range(2, 50001):
    if not n_prime[i]:
        prime.append(i)
    if i<100000**0.5:
        for j in range(1, 50000//i+1):
            n_prime[i*j] = 1

p = len(prime)

curr = 30
binary = 1<<31
while True:
    K_, nn = count(binary)
    if K_ < K:
        binary += 1 << curr
    elif K_ > K or (K_ == K and nn):
        binary -= 1 << curr
    else:
        break
    
    curr -= 1

print(binary)