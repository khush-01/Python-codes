#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int sum(int *marks, int n, char g) {
    int sum = 0;
    if (g == 'b')
        for (int i = 0; i < n; i += 2)
            sum += *(marks + i);
    else
        for (int i = 1; i < n; i += 2)
            sum += *(marks + i);
    return sum;
}

int main() {
    int n;
    char gender;
    int res;
    scanf("%d", &n);
    int *marks = (int *) malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        scanf("%d", (marks + i));
    }
    scanf(" %c", &gender);
    res = sum(marks, n, gender);
    printf("%d", res);
    free(marks);
    return 0;
}
