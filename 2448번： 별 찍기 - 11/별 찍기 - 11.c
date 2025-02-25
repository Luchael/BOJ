/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 2448                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/2448                           #+#        #+#      #+#    */
/*   Solved: 2025/02/25 14:27:52 by luchael       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

int arr[3072][6144];

void star(int n, int r, int c)
{
    if (n == 3)
    {
        arr[r][c] = 1;
        arr[r + 1][c - 1] = 1;
        arr[r + 1][c + 1] = 1;
        arr[r + 2][c - 2] = 1;
        arr[r + 2][c - 1] = 1;
        arr[r + 2][c] = 1;
        arr[r + 2][c + 1] = 1;
        arr[r + 2][c + 2] = 1;
        return;
    }
    star(n / 2, r, c);
    star(n / 2, r + n / 2, c - n / 2);
    star(n / 2, r + n / 2, c + n / 2);
}

int main()
{
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n * 2; j++)
            arr[i][j] = 0;
    }

    star(n, 0, n - 1);

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n * 2; j++)
        {
            if (arr[i][j] == 1)
                printf("*");
            else if (arr[i][j] == 0)
                printf(" ");
        }
        printf("\n");
    }
}