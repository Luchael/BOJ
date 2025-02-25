/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 4153                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/4153                           #+#        #+#      #+#    */
/*   Solved: 2025/02/25 14:47:22 by luchael       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>
int main()
{
    int a, b, c, tmp;
    while (1)
    {
        scanf("%d %d %d", &a, &b, &c);
        if (a > c)
            tmp = c, c = a, a = tmp;
        if (b > c)
            tmp = c, c = b, b = tmp;
        if (!a && !b && !c)
            break;
        printf("%s\n", a * a + b * b == c * c ? "right" : "wrong");
    }
}