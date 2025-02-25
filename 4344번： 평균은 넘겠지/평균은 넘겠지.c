/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 4344                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/4344                           #+#        #+#      #+#    */
/*   Solved: 2025/02/25 14:47:39 by luchael       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>
int main()
{
    int C, N;
    scanf("%d", &C); // 테스트케이스 개수
    for (; C > 0; C--)
    {
        scanf("%d", &N); // 학생 수
        int a[N], p = 0;
        double avg = 0;
        for (int j = 0; j < N; j++)
            scanf("%d", &a[j]); // 점수 입력
        for (int j = 0; j < N; j++)
            avg += a[j];
        avg /= N;
        for (int j = 0; j < N; j++)
            if (a[j] > avg)
                p++;                              // 평균 넘는 사람 수
        printf("%.3lf%%\n", (double)p / N * 100); // 출력
    }
}