/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 2522                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/2522                           #+#        #+#      #+#    */
/*   Solved: 2025/02/25 14:28:27 by luchael       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

int main()
{
    int a, i, j, ii;
    scanf("%d", &a);
    for (i = a - 1; i > 0; i--)
    {
        for (j = 0; j < a; j++)
        {
            if (j >= i)
                printf("*");
            else
                printf(" ");
        }
        printf("\n");
    }
    for (i = 0; i < a; i++)
    {
        for (j = 0; j < a; j++)
        {
            if (j >= i)
                printf("*");
            else
                printf(" ");
        }
        printf("\n");
    }
}