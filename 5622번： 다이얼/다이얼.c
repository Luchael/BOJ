/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 5622                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/5622                           #+#        #+#      #+#    */
/*   Solved: 2025/02/25 14:49:38 by luchael       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>
int main()
{
    char a;
    int r = 0;
    while (1)
    {
        scanf("%c", &a);
        if (a == '\n')
            break;
        if (a >= 'S')
            a--;
        if (a == 'Y')
            a--;
        a = (a - 'A') / 3 + 3;
        r += a;
    }
    printf("%d", r);
}