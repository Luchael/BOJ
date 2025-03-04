/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 2445                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/2445                           #+#        #+#      #+#    */
/*   Solved: 2025/02/25 14:26:30 by luchael       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

int main()
{
    int a, i, j, ii;
    scanf("%d", &a);
    for (i = 1; i <= a * 2 - 1; i++)
    {
        ii = i <= a ? i - 1 : 2 * a - i - 1;
        for (j = 0; j < a * 2; j++)
        {
            if ((j < a && j <= ii) || (j >= a && a - (j - a) <= ii + 1))
                printf("*");
            else
                printf(" ");
        }
        printf("\n");
    }
}