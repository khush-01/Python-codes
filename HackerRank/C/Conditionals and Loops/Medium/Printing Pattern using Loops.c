#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int n;
    scanf("%d", &n);
    int len = 2 * n - 1;
    for (int i = 0; i < len; i++) {
        for (int j = 0; j < len; j++) {
            int d = i < j ? i : j;
            d = d < len-i ? d : len-i-1;
            d = d < len-j-1 ? d : len-j-1;
            printf("%d ", n-d);
        }
        printf("\n");
    }
    return 0;
}
