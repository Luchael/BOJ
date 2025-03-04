/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 1978                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/1978                           #+#        #+#      #+#    */
/*   Solved: 2025/02/25 14:19:52 by luchael       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>
int main()
{
    int T, cnt = 0, i;
    scanf("%d", &T);
    for (; T > 0; T--)
    {
        scanf("%d", &i);
        for (int j = 2; j <= i; j++)
        {
            if (j == i)
                cnt++;
            if (!(i % j))
                break;
        }
    }
    printf("%d", cnt);
}