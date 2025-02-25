/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 2447                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/2447                           #+#        #+#      #+#    */
/*   Solved: 2025/02/25 14:27:10 by luchael       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int star(int x, int y);

int main(void)
{
    int a, x, y;
    scanf("%d", &a);
    for (x = 0; x < a; x++)
    {
        for (y = 0; y < a; y++)
        {
            printf("%c", star(x, y) ? '*' : ' ');
        }
        printf("\n");
    }
    return 0;
}

int star(int x, int y)
{
    while (1)
    {
        if (!((x - 1) % 3 || (y - 1) % 3))
            return 0;
        if (!x || !y)
            return 1;
        return star(x / 3, y / 3);
    }
}