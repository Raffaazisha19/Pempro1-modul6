#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    int zetsu[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &zetsu[i]);
    }

    for (int i = 0; i < n; i++) {
        if (i > 0) printf(" "); 
        printf("%d", zetsu[i] * (i + 1)); 
    }
    printf("\n");

    return 0;
}