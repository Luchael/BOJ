/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 1065                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/1065                           #+#        #+#      #+#    */
/*   Solved: 2025/02/25 14:08:25 by luchael       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>
int a(int n)
{
    int c, b = n, d = n;
    for (n /= 10; n != 0; n /= 10, b /= 10)
    {
        if (b == d)
        {
            c = b % 10 - n % 10;
            continue;
        }
        if (c != b % 10 - n % 10)
            return 0;
    }
    return 1;
}
int main()
{
    int n, result = 0;
    scanf("%d", &n);
    for (int i = 1; i <= n; i++)
        a(i) ? result++ : i;
    printf("%d", result);
}