/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 2588                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/2588                           #+#        #+#      #+#    */
/*   Solved: 2025/02/25 14:33:53 by luchael       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
main(a, b)
{
    scanf("%d%d", &a, &b);
    printf("%d\n%d\n%d\n%d", a * (b % 10), a * (b / 10 % 10), a * (b / 100), a * b);
}