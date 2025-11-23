#include <stdio.h>
#include <string.h>

int main() {
    char kode[100];
    char pesan[100];
    int i, len1, len2;
    int bintang = 0;
    int pagar = 0;

    scanf("%[^\n]%*c", kode);
    scanf("%[^\n]%*c", pesan);

    len1 = strlen(kode);
    len2 = strlen(pesan);

    if (len1 != len2) {
        printf("Panjang kalimat berbeda, pesan palsu\n");
    } else {
        for (i = 0; i < len1; i++) {
            if (kode[i] == ' ' && pesan[i] == ' ') {
                printf(" ");
            } 
            else if (kode[i] == pesan[i]) {
                printf("*");
                bintang++;
            } 
            else {
                printf("#");
                pagar++;
            }
        }

        printf("\n* = %d", bintang);
        printf("\n# = %d", pagar);

        if (bintang >= pagar) {
            printf("\nPesan Asli\n");
        } else {
            printf("\nPesan Palsu\n");
        }
    }

    return 0;
}