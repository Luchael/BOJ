/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 10991                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/10991                          #+#        #+#      #+#    */
/*   Solved: 2025/02/25 15:13:23 by luchael       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

int main()
{
    int a, i, j;
    scanf("%d", &a);
    for (i = 0; i < a; i++)
    {
        for (j = 0; j < a + i; j++)
        {
            if (i % 2 == a % 2)
            {
                if (j >= a - i - 1)
                {
                    if (j % 2)
                        printf("*");
                    else
                        printf(" ");
                }
                else
                    printf(" ");
            }
            else
            {
                if (j >= a - i - 1)
                {
                    if (!(j % 2))
                        printf("*");
                    else
                        printf(" ");
                }
                else
                    printf(" ");
            }
        }
        printf("\n");
    }
}