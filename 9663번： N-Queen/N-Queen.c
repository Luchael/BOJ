/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 9663                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/9663                           #+#        #+#      #+#    */
/*   Solved: 2025/02/25 14:56:45 by luchael       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>
int grid[14][14] = {0};
int many = 0;
int N_Queen(int num, int count);

int main()
{
    int num;
    scanf("%d", &num);
    printf("%d", N_Queen(num, 0));
}

int N_Queen(int num, int y)
{
    for (int x = 0; x < num; x++)
    {
        int tf = 0, min = y < x ? y : x, max = y < x ? x : y;
        grid[y][x] = 1;
        if (y != 0)
        {
            for (int i = 0; i < y; i++)
            {
                if (grid[i][x] == 1)
                {
                    tf = 1;
                    grid[y][x] = 0;
                    break;
                }
            }
            if (tf)
                continue;
            for (int i = min; i > 0; i--)
            {
                if (grid[y - i][x - i] == 1)
                {
                    tf = 1;
                    grid[y][x] = 0;
                    break;
                }
            }
            if (tf)
                continue;
            min = y > (num - x - 1) ? num - x - 1 : y;
            for (int i = min; i > 0; i--)
            {
                if (grid[y - i][x + i] == 1)
                {
                    tf = 1;
                    grid[y][x] = 0;
                    break;
                }
            }
            if (tf)
                continue;
        }
        if (num - 1 == y)
            many++;
        else
            N_Queen(num, y + 1);
        grid[y][x] = 0;
    }
    return many;
}