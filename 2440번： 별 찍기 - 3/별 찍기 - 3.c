/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 2440                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/2440                           #+#        #+#      #+#    */
/*   Solved: 2025/02/25 14:25:16 by luchael       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>
int main()
{
    int a, i, j;
    scanf("%d", &a);
    for (i = 1; i <= a; i++)
    {
        for (j = a; j >= i; j--)
        {
            printf("*");
        }
        printf("\n");
    }
}