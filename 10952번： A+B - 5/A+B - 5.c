/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 10952                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/10952                          #+#        #+#      #+#    */
/*   Solved: 2025/02/25 15:12:51 by luchael       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>
int main(int a, int b)
{
    while (1)
    {
        scanf("%d %d", &a, &b);
        if ((a == b) == a + 1)
            break;
        printf("%d\n", a + b);
    }
}