/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 1929                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/1929                           #+#        #+#      #+#    */
/*   Solved: 2025/02/25 14:19:32 by luchael       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>
#include <math.h>
int main()
{
    int i, j, k;
    scanf("%d %d", &i, &j);
    for (; i <= j; i++)
    {
        if (i == 1)
            continue;
        for (k = round(sqrt((double)i)); k >= 1; k--)
        {
            if (!(k - 1))
                printf("%d\n", i);
            if (!(i % k))
                break;
        }
    }
}