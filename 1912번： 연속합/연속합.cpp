/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 1912                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/1912                           #+#        #+#      #+#    */
/*   Solved: 2025/02/25 14:19:07 by luchael       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
#include <iostream>
using namespace std;

int a = 0;
int num[100001];

int main()
{
    cin >> a;
    int i = 0, j = 0;
    for (i = 0; i < a; i++)
    {
        cin >> num[i];
    }
    int M = num[0];
    int answer = M;
    for (i = 1; i < a; i++)
    {
        M = max(num[i], M + num[i]);
        answer = max(answer, M);
    }
    cout << answer << '\n';
}