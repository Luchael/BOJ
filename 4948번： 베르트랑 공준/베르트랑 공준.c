/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 4948                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/4948                           #+#        #+#      #+#    */
/*   Solved: 2025/02/25 14:48:39 by luchael       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>
int main()
{
    int n;
    while (1)
    {
        int p = 2, cnt = 0;
        scanf("%d", &n);
        if (n == 0)
            break;
        int prime[n * 2 + 1];
        for (int i = 0; i < n * 2 + 1; i++)
            prime[i] = 1;

        while (p * p <= n * 2 + 1)
        {
            if (prime[p] == 1)
                for (int i = p * 2; i < n * 2 + 1; i += p)
                    prime[i] = 0;
            p++;
        }
        prime[0] = 0, prime[1] = 0;
        for (int i = n + 1; i < n * 2 + 1; i++)
        {
            if (prime[i])
            {
                cnt++;
            }
        }
        printf("%d\n", cnt);
    }
}