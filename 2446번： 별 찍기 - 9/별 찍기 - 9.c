/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 2446                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/2446                           #+#        #+#      #+#    */
/*   Solved: 2025/02/25 14:26:42 by luchael       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

int main()
{
    int a, i, j;
    scanf("%d", &a);
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
    for (i = 1; i < a; i++)
    {
        for (j = 1; j <= a + i; j++)
        {
            if (j >= a - i)
                printf("*");
            else
                printf(" ");
        }
        printf("\n");
    }
}