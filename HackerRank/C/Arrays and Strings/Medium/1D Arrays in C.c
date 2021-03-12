#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int n, x, sum = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; i ++) {
        scanf("%d", &x);
        sum += x;
    }
    printf("%d", sum);
    return 0;
}
