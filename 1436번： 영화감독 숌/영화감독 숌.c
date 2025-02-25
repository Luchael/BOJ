/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 1436                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/1436                           #+#        #+#      #+#    */
/*   Solved: 2025/02/25 14:14:55 by luchael       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>
int check_six(int a);
int main()
{
    int get, devil = 666, is_six;
    scanf("%d", &get);
    for (; get > 1; get--)
    {
        is_six = check_six(devil);
        if (is_six)
        {
            devil++;
            if (!check_six(devil))
            {
                devil = devil - devil % 1000 + 666;
                if (check_six(devil))
                    devil += 1000;
            }
        }
        else
        {
            devil += 1000;
            is_six = check_six(devil);
            if (is_six)
                for (int i = 1; i < is_six; i *= 10)
                    devil -= i * 6;
        }
    }
    printf("%d", devil);
}

int check_six(int a)
{
    for (int i = 1000; i >= 10; i /= 10)
        if (a / i % 1000 == 666)
            return i;
    return 0;
}