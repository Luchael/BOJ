/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 10993                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/10993                          #+#        #+#      #+#    */
/*   Solved: 2025/02/25 15:13:46 by luchael       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

int arr[1024][2048] = {0};
int h = 1, w = 1, maxh = 1, maxw = 1;

void star(int t, int x, int y)
{
    h = 1;
    w = 1;

    for (int i = 0; i < t; i++)
        h *= 2;

    h = h - 1;
    w = 2 * h - 1;

    if (t == 0)
    {
        return;
    }

    else if (t % 2 == 1)
    {
        for (int i = 0; i < h; i++)
        {
            arr[x + i][y - i] = 1;
            arr[x + i][y + i] = 1;

            if (i == h - 1)
            {
                for (int j = 0; j < (w + 1) / 2; j++)
                {
                    arr[x + i][y - j] = 1;
                    arr[x + i][y + j] = 1;
                }
            }
        }
        star(t - 1, x + h - 2, y);
    }

    else if (t % 2 == 0)
    {
        for (int i = 0; i < h; i++)
        {
            arr[x - i][y - i] = 1;
            arr[x - i][y + i] = 1;

            if (i == h - 1)
            {
                for (int j = 0; j < (w + 1) / 2; j++)
                {
                    arr[x - i][y - j] = 1;
                    arr[x - i][y + j] = 1;
                }
            }
        }
        star(t - 1, x - h + 2, y);
    }
}

int main()
{

    int n;
    scanf("%d", &n);

    for (int i = 0; i < n; i++)
        maxh *= 2;

    maxh = maxh - 1;
    maxw = maxh * 2 - 1;

    if (n % 2 == 1)
        star(n, 0, (maxw - 1) / 2);
    else
        star(n, maxh - 1, (maxw - 1) / 2);

    for (int i = 0; i < maxh; i++)
    {
        for (int j = 0; j < maxw; j++)
        {
            if (arr[i][j] == 1)
                printf("*");
            else if (arr[i][j] == 0)
                printf(" ");

            if (n % 2 == 1 && j == (maxw / 2) + i)
                break;
            else if (n % 2 == 0 && j == maxw - i - 1)
                break;
        }
        if (i == maxw - i - 1)
            break;
        else
            printf("\n");
    }
}