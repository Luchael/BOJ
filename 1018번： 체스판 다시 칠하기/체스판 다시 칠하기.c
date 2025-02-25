/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 1018                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/1018                           #+#        #+#      #+#    */
/*   Solved: 2025/02/25 14:06:33 by luchael       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

int main()
{
    int x, y, diff_x, diff_y, a = -2, b = -1;
    scanf("%d %d", &x, &y);
    char give[x][y], q;

    for (int i = 0; i < x; i++)
    {
        for (int j = 0; j < y; j++)
        {
            scanf(" %c", &give[i][j]);
        }
    }
    diff_x = x - 8, diff_y = y - 8;

    int cnt[(diff_x + 1) * (diff_y + 1) * 2];

    for (int i = 0; i < (diff_x + 1) * (diff_y + 1) * 2; i++)
        cnt[i] = 0;

    for (int xx = diff_x; xx >= 0; xx--)
    {
        for (int yy = diff_y; yy >= 0; yy--)
        {
            a += 2, b += 2;
            for (int i = xx; i < 8 + xx; i++)
            {
                for (int j = yy; j < 8 + yy; j++)
                {
                    int ii = i - xx, jj = j - yy;
                    if (ii % 2)
                    {
                        if (jj % 2)
                        {
                            if (give[i][j] != 'W')
                                cnt[a]++;
                            else
                                cnt[b]++;
                        }
                        else
                        {
                            if (give[i][j] != 'B')
                                cnt[a]++;
                            else
                                cnt[b]++;
                        }
                    }
                    else
                    {
                        if (jj % 2)
                        {
                            if (give[i][j] != 'B')
                                cnt[a]++;
                            else
                                cnt[b]++;
                        }
                        else
                        {
                            if (give[i][j] != 'W')
                                cnt[a]++;
                            else
                                cnt[b]++;
                        }
                    }
                }
            }
        }
    }
    int min = 100000000;
    for (int i = 0; i < (diff_x + 1) * (diff_y + 1) * 2; i++)
        if (cnt[i] < min)
            min = cnt[i];
    printf("%d", min);
}