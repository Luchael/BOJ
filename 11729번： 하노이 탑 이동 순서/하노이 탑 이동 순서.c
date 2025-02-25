/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 11729                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/11729                          #+#        #+#      #+#    */
/*   Solved: 2025/02/25 15:18:27 by luchael       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void hanoi_tower(int n, int from, int tmp, int to)
{
    if (n == 1)
        printf("%d %d\n", from, to);
    else
    {
        hanoi_tower(n - 1, from, to, tmp);
        printf("%d %d\n", from, to);
        hanoi_tower(n - 1, tmp, from, to);
    }
}

int main()
{
    int a, b = 1;
    scanf("%d", &a);
    for (int i = a; i > 0; i--)
        b *= 2;
    printf("%d\n", b - 1);
    hanoi_tower(a, 1, 2, 3);
}