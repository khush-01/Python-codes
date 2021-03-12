#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int n, k, or = 0, and = 0, xor = 0;
    scanf("%d%d", &n, &k);
    for (int i = 1; i <= n; i++) {
        for (int j = i+1; j <= n; j++) {
            int res1 = i | j;
            int res2 = i & j;
            int res3 = i ^ j;
            if (res1 > or)
                or = (res1 >= k) ? or : res1;
            if (res2 > and)
                and = (res2 >= k) ? and : res2;
            if (res3 > xor)
                xor = (res3 >= k) ? xor : res3;
        }
    }
    printf("%d\n%d\n%d", and, or, xor);
    return 0;
}
