/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 2577                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/2577                           #+#        #+#      #+#    */
/*   Solved: 2025/02/25 14:32:02 by luchael       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>
int main(int a, int b, int c)
{
    scanf("%d %d %d", &a, &b, &c);
    int d[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    for (int i = a * b * c; i != 0; i /= 10)
        d[i % 10]++;
    for (int i = 0; i < 10; i++)
        printf("%d\n", d[i]);
}