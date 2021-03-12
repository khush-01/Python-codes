#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    char s[1000], a[10];
    for (int i = 0; i < 10; i++) {
        a[i] = 0;
    }
    scanf("%s", &s);
    for (int i = 0; i < strlen(s); i++) {
        int x = s[i] - '0';
        if (x >= 0 && x<= 9)
            a[x]++;
    }
    for (int i = 0; i < 10; i++) {
        printf("%d ", a[i]);
    }
    return 0;
}
