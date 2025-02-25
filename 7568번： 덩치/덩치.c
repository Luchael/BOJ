/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 7568                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/7568                           #+#        #+#      #+#    */
/*   Solved: 2025/02/25 14:55:05 by luchael       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

int main(void)
{
    int n, w[50], h[50], score[50];
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d %d", &w[i], &h[i]);
        score[i] = 1;
    }
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            if (w[i] < w[j] && h[i] < h[j])
                score[i]++;

    for (int i = 0; i < n; i++)
    {
        printf("%d", score[i]);
        if (i != n - 1)
            printf(" ");
    }

    return 0;
}