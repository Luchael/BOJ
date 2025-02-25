/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 2675                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/2675                           #+#        #+#      #+#    */
/*   Solved: 2025/02/25 14:34:40 by luchael       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>
int main()
{
    int T, a;
    char b;
    scanf("%d", &T);
    for (; T > 0; T--)
    {
        for (int i = 0;; i++)
        {
            if (i == 0)
            {
                scanf("%d", &a);
                continue;
            }
            scanf("%c", &b);
            if (i == 1)
                continue;
            if (b == '\n')
                break;
            for (int j = 0; j < a; j++)
                printf("%c", b);
        }
        printf("\n");
    }
}