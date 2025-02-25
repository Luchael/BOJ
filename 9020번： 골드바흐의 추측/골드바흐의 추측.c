/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 9020                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/9020                           #+#        #+#      #+#    */
/*   Solved: 2025/02/25 14:55:43 by luchael       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>
int main()
{
    int p = 2, cnt = 0, n, T, prime[10001];
    for (int i = 0; i < 10001; i++)
        prime[i] = 1;
    while (p * p <= 10000)
    {
        if (prime[p] == 1)
            for (int i = p * 2; i < 10001; i += p)
                prime[i] = 0;
        p++;
    }
    prime[0] = 0, prime[1] = 0;
    scanf("%d", &T);
    for (; T > 0; T--)
    {
        scanf("%d", &n);
        int up = n / 2, down = n / 2;
        for (; down > 1; down--, up++)
        {
            if (prime[down] && prime[up])
            {
                printf("%d %d\n", down, up);
                break;
            }
        }
    }
}