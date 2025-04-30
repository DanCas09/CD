#include <stdio.h>
#include "../functions/count_zeros.c"

int main() {
    char *failMsg = "Test Failed";

    if (count_zeros(16) != 31) {
        printf("%s\n", failMsg);
        return 1;
    }

    if (count_zeros(23) != 28) {
        printf("%s\n", failMsg);
        return 1;
    }

    if (count_zeros(0xFFFFFFFF) != 0) {
        printf("%s\n", failMsg);
        return 1;
    }

    if (count_zeros(0x00000001) != 31) {
        printf("%s\n", failMsg);
        return 1;
    }

    printf("Test passed\n");
    return 0;
}