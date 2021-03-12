#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct triangle {
	int a, b, c;
};
typedef struct triangle triangle;

float area(triangle t) {
    float p = (t.a + t.b + t.c) / 2.0;
    float ar;
    ar = sqrt(p * (p - t.a) * (p - t.b) * (p - t.c));
    return ar;
}

void sort_by_area(triangle* tr, int n) {
	for (int i = 0; i < n; i++) {
        for (int j = 0; j < n - 1 - i; j++) {
            if (area(tr[j]) > area(tr[j+1])) {
                int tmp;
                tmp = tr[j].a;
                tr[j].a = tr[j+1].a;
                tr[j+1].a = tmp;
                tmp = tr[j].b;
                tr[j].b = tr[j+1].b;
                tr[j+1].b = tmp;
                tmp = tr[j].c;
                tr[j].c = tr[j+1].c;
                tr[j+1].c = tmp;
            }
        }
	}
}

int main() {
	int n;
	scanf("%d", &n);
	triangle *tr = malloc(n * sizeof(triangle));
	for (int i = 0; i < n; i++) {
		scanf("%d%d%d", &tr[i].a, &tr[i].b, &tr[i].c);
	}
	sort_by_area(tr, n);
	for (int i = 0; i < n; i++) {
		printf("%d %d %d\n", tr[i].a, tr[i].b, tr[i].c);
	}
	return 0;
}
