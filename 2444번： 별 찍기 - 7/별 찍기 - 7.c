/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 2444                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/2444                           #+#        #+#      #+#    */
/*   Solved: 2025/02/25 14:26:17 by luchael       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

int main()
{
    int a, i, j;
    scanf("%d", &a);
    for (i = 0; i < a - 1; i++)
    {
        for (j = 0; j < a + i; j++)
        {
            if (j >= a - i - 1)
                printf("*");
            else
                printf(" ");
        }
        printf("\n");
    }
    for (i = a; i > 0; i--)
    {
        for (j = 0; j < a + i - 1; j++)
        {
            if (j >= a - i)
                printf("*");
            else
                printf(" ");
        }
        printf("\n");
    }
}