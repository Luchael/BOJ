// ************************************************************************** //
//                                                                            //
//                                                      :::    :::    :::     //
//   Problem Number: 1002                              :+:    :+:      :+:    //
//                                                    +:+    +:+        +:+   //
//   By: luchael <boj.kr/u/luchael>                  +#+    +#+          +#+  //
//                                                  +#+      +#+        +#+   //
//   https://boj.kr/1002                           #+#        #+#      #+#    //
//   Solved: 2025/02/25 13:49:31 by luchael       ###          ###   ##.kr    //
//                                                                            //
// ************************************************************************** //

#include <stdio.h>
#include <math.h>

int main()
{
    int T, x1, y1, r1, x2, y2, r2, i, R;
    float d;
    scanf("%d", &T);
    for (i = 0; i < T; i++)
    {
        scanf("%d %d %d %d %d %d", &x1, &y1, &r1, &x2, &y2, &r2);
        if (x1 == x2 && y1 == y2)
        {
            if (r1 == r2)
                printf("-1\n");
            else
                printf("0\n");
        }
        else
        {
            d = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2)), R = r1 - r2 > 0 ? r1 - r2 : -(r1 - r2);
            if (r1 + r2 < d)
                printf("0\n");
            else if (d == r1 + r2)
                printf("1\n");
            else if (d == R)
                printf("1\n");
            else if (R < d)
                printf("2\n");
            else
                printf("0\n");
        }
    }
}