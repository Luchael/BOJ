/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 1330                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/1330                           #+#        #+#      #+#    */
/*   Solved: 2025/02/25 14:14:07 by luchael       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>
int main()
{
    int a, b;
    scanf("%d %d", &a, &b);
    printf("%c", a > b ? '>' : a < b ? '<'
                                     : '=');
    if (a == b)
        printf("=");
}