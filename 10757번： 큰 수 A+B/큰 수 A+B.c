/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 10757                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/10757                          #+#        #+#      #+#    */
/*   Solved: 2025/02/25 15:09:41 by luchael       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>
int abs(int a)
{
    return a > 0 ? a : -a;
}
int main()
{
    int a[10001], b[10001], e[10001];
    int c, d;
    for (int i = 0; i < 10001; i++)
    {
        scanf("%c", &a[i]);
        if (a[i] == ' ')
        {
            c = i;
            break;
        }
        a[i] -= '0';
    }
    for (int i = 0; i < 10001; i++)
    {
        scanf("%c", &b[i]);
        if (b[i] == '\n')
        {
            d = i;
            break;
        }
        b[i] -= '0';
    }
    int ab = abs(c - d);
    if (c > d)
    {
        for (int i = 0; i < c; i++)
        {
            if (i < ab)
                e[i] = 0;
            else
                e[i] = b[i - c + d];
        }
    }
    else if (c < d)
    {
        for (int i = 0; i < d; i++)
        {
            if (i < ab)
                e[i] = 0;
            else
                e[i] = a[i - d + c];
        }
    }
    int max = c > d ? c : d;
    for (int i = 0; i < max; i++)
    {
        if (c > d)
            e[i] += a[i];
        else if (c < d)
            e[i] += b[i];
        else
            e[i] = a[i] + b[i];
    }
    for (int i = max; i > 0; i--)
        if (i != max)
            if (e[i] > 9)
                e[i] -= 10, e[i - 1]++;

    for (int i = 1; i <= max; i++)
    {
        printf("%d", e[i - 1]);
    }
}