/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 2581                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/2581                           #+#        #+#      #+#    */
/*   Solved: 2025/02/25 14:32:38 by luchael       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>
#include <math.h>
int main()
{
    int i, j, k, sum[2] = {0, 0};
    scanf("%d %d", &i, &j);
    for (; i <= j; i++)
    {
        if (i == 1)
            continue;
        for (k = round(sqrt((double)i)); k >= 1; k--)
        {
            if (!(k - 1))
            {
                sum[1] += i;
                if (!sum[0])
                    sum[0] = i;
            }
            if (!(i % k))
                break;
        }
    }
    if (sum[0])
        printf("%d\n%d", sum[1], sum[0]);
    else
        printf("%d", -1);
}