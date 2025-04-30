#include <stdio.h>
#include "../functions/count_ones.c"

int main() {
    char *failMsg = "Test Failed";

    if (count_ones(16) != 1) {
        printf("%s\n", failMsg);
        return 1;
    }

    if (count_ones(23) != 4) {
        printf("%s\n", failMsg);
        return 1;
    }

    if (count_ones(0xFFFFFFFF) != 32) {
        printf("%s\n", failMsg);
        return 1;
    }

    if (count_ones(0x00000001) != 1) {
        printf("%s\n", failMsg);
        return 1;
    }

    printf("Test passed\n");
    return 0;
}