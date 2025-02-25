/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 2798                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/2798                           #+#        #+#      #+#    */
/*   Solved: 2025/02/25 14:38:44 by luchael       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
    int n = 1, max, sum, msum = 0, num[100];
    scanf("%d %d", &n, &max);
    for (int i = 0; i < n; i++)
        scanf("%d", &num[i]);
    for (int i = 0; i < n - 2; i++)
    {
        for (int j = i + 1; j < n - 1; j++)
        {
            for (int k = j + 1; k < n; k++)
            {
                sum = num[i] + num[j] + num[k];
                msum = msum < sum ? sum <= max ? sum : msum : msum;
            }
        }
    }
    printf("%d", msum);
}