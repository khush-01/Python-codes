#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int *books;
int **pages;

int main() {
    int n, q;
    scanf("%d%d", &n, &q);
    while (q--) {
        int type;
        scanf("%d", &type);
        if (type == 1) {
            int x, y;
            scanf("%d %d", &x, &y);
            if (!books)
                books = (int*) calloc(n, sizeof(int));
            if (!pages)
                pages = (int**) calloc(n, sizeof(int*));
            *(books + x) += 1;
            if (!pages[x])
                pages[x] = (int *) calloc(*(books + x), sizeof(int));
            else
                pages[x] = (int *) realloc(pages[x], sizeof(int) * *(books + x));

            int curr = (*(books + x) - 1);
            *(*(pages + x) + curr) = y;

        } else if (type == 2) {
            int x, y;
            scanf("%d %d", &x, &y);
            printf("%d\n", *(*(pages + x) + y));
        } else {
            int x;
            scanf("%d", &x);
            printf("%d\n", *(books + x));
        }
    }
    if (books)
        free(books);
    for (int i = 0; i < n; i++)
        if (*(pages + i))
            free(*(pages + i));
    if (pages)
        free(pages);
    return 0;
}
