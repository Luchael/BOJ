/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 2443                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/2443                           #+#        #+#      #+#    */
/*   Solved: 2025/02/25 14:26:00 by luchael       ###          ###   ##.kr    */
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
}