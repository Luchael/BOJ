/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 1546                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/1546                           #+#        #+#      #+#    */
/*   Solved: 2025/02/25 14:15:37 by luchael       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>
#include <math.h>
int main()
{
    int a, b = 0, i, j, he_is_fool = 0;
    scanf("%d", &j);
    for (i = j; i > 0; i--)
        scanf("%d", &a), b += a, he_is_fool < a ? he_is_fool = a : a;
    printf("%lf", (double)b / he_is_fool * 100 / j);
}