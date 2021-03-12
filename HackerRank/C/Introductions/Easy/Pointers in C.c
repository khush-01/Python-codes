#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

void update(int *a, int *b) {
    int x = *a + *b;
    int y = *a - *b;
    *a = x;
    if (y < 0)
        *b = -y;
    else
        *b = y;
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    scanf("%d%d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);
    return 0;
}
