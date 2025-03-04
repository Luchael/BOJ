/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 1316                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/1316                           #+#        #+#      #+#    */
/*   Solved: 2025/02/25 14:13:47 by luchael       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

int main()
{
    int T, a[26], result = 0, nf = 0;
    char in = '\n', before;
    scanf("%d", &T); // 테스트 케이스 개수
    for (int i = 0; i <= T; i++)
    {
        for (int i = 0; i < 26; i++)
            a[i] = 0; // 배열 전부 0으로 채우기
        while (1)
        {
            before = in;      // 이전문자 검사용 변수
            scanf("%c", &in); // 문자 입력
            if (in == '\n')
            {
                (nf == 0 && i != 0) ? result++ : nf; // nf가 0이고 맨 처음에 숫자 땜에 들어온 줄바꿈 아니면 출력값에 1을 더함
                nf = 0;                              // nf 다시 0 으로
                break;                               // 줄바꿈 문자 나오면 빠져나옴
            }
            if (nf)
                continue; // nf 가 참이면 건너뛰기, in이 줄바꿈이면 건너뛰기
            if (!a[in - 'a'] || before == in)
                a[in - 'a'] = 1;
            // a 부터 z 까지 인덱스 번호 주고 한번이라도 나왔으면 1로 만들기
            // 만약 그 값이 1이면, 한번이라도 나왔다는 뜻이므로, 이전거랑 다르고, 그 값이 1이면 연속되지 않은게 나왔다는 뜻
            else
                nf = 1;
            // 연속된게 아닐 때 nf 를 1로 올림
        }
    }
    printf("%d", result); // 출력
}