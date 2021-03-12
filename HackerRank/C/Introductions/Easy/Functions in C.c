#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int max_of_four(int, int, int, int);

int main() {
    int a, b, c, d;
    scanf("%d%d%d%d", &a, &b, &c, &d);
    printf("%d", max_of_four(a, b, c, d));
    return 0;
}

int max_of_four(int a, int b, int c, int d) {
    int big1 = a > b ? a : b;
    int big2 = c > d ? c : d;
    int big = big1 > big2 ? big1 : big2;
    return big;
}
