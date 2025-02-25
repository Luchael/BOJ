/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 1011                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/1011                           #+#        #+#      #+#    */
/*   Solved: 2025/02/25 14:00:59 by luchael       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>
#include <math.h>

int main()
{
    int T, output;
    double x, y;
    scanf("%d", &T);
    for (; T > 0; T--)
    {
        scanf("%lf %lf", &x, &y);
        y -= x;
        y = sqrt(y), x = round(y);
        output = y > x ? x * 2 : x * 2 - 1;
        printf("%d\n", output);
    }
}