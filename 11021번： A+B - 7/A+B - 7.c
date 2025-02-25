#include <stdio.h>
int main(T, a, b)
{
    scanf("%d", &T);
    for (int i = 1; i <= T; i++)
    {
        scanf("%d %d", &a, &b);
        printf("Case #%d: %d\n", i, a + b);
    }
}