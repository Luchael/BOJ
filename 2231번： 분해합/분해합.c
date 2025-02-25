/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 2231                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/2231                           #+#        #+#      #+#    */
/*   Solved: 2025/02/25 14:22:00 by luchael       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

int main()
{
    int a, b, time = 0;
    scanf("%d", &a);
    b = a;
    while (b)
    {
        b /= 10;
        time++;
    }
    b = 9 * time;
    if (b == 1)
    {
        printf("%d", b % 2 ? 0 : b / 2);
        return 0;
    }
    for (int i = a - b * 9; i <= a; i++)
    {
        int sum = 0, copy_i = i;
        while (copy_i)
        {
            sum += copy_i % 10;
            copy_i /= 10;
        }
        if (a == i + sum)
        {
            printf("%d", i);
            return 0;
        }
    }
    printf("%d", 0);
}