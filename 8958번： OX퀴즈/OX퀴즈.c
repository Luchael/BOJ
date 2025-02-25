/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 8958                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/8958                           #+#        #+#      #+#    */
/*   Solved: 2025/02/25 14:55:30 by luchael       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

int main()
{
    int T, j = 0;
    char a;
    scanf("%d", &T);
    for (int i = 0; i <= T; i++)
    {
        int score = 0;
        while (1)
        {
            scanf("%c", &a);
            if (a == 'O')
                score += ++j;
            else
            {
                j = 0;
                if (a == '\n')
                    break;
            }
        }
        if (i == 0)
            continue;
        printf("%d\n", score);
    }
}