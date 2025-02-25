/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 1157                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/1157                           #+#        #+#      #+#    */
/*   Solved: 2025/02/25 14:13:14 by luchael       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
    char str;
    int tf = -1, i, max = 0, a[26];
    for (i = 0; i < 26; i++)
        a[i] = 0;
    while (1)
    {
        scanf("%c", &str);
        if (str == '\n')
            break;
        if (str >= 'a' && str <= 'z')
            a[str - 'a']++;
        else if (str >= 'A' && str <= 'Z')
            a[str - 'A']++;
    }
    for (i = 0; i < 26; i++)
    {
        if (a[i] > max)
            tf = i, max = a[i];
        else if (a[i] == max)
            tf = -1;
    }
    printf("%c\n", tf == -1 ? '?' : (tf + 'A'));
}