/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 4673                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/4673                           #+#        #+#      #+#    */
/*   Solved: 2025/02/25 14:48:23 by luchael       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>
int d(int n)
{
    int result = n;
    for (; n != 0; n /= 10)
    {
        result += n % 10;
    }
    return result;
}
int main()
{
    int a[9999 + 37];
    for (int i = 1; i < 10000; i++)
        a[i] = 0;
    for (int i = 1; i < 10000; i++)
        a[d(i)]++;
    for (int i = 1; i < 10000; i++)
        !a[i] ? printf("%d\n", i) : a[i];
}