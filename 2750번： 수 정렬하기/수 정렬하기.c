/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 2750                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/2750                           #+#        #+#      #+#    */
/*   Solved: 2025/02/25 14:37:31 by luchael       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>
void sort(int *a, int size);
int main()
{
    int k;
    scanf("%d", &k);
    int list[k];
    for (int i = 0; i < k; i++)
        scanf("%d", &list[i]);
    sort(list, k);
    for (int i = 0; i < k; i++)
        printf("%d\n", list[i]);
}

void sort(int *a, int size)
{
    int fill, tmp, h;
    for (fill = 0; fill < size; fill++)
    { // 정렬 시작
        tmp = a[fill];
        for (h = fill - 1; h >= 0; h--)
        {
            if (tmp < a[h])
                a[h + 1] = a[h];
            else
                break;
        }
        a[h + 1] = tmp;
    } // 끝
}