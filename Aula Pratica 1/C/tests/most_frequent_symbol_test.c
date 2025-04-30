#include <stdio.h>
#include "../functions/most_frequent_symbol.c"

int main() {

    // This file contains the character 'a' the most number of times.
    if (most_frequent_symbol("./TestFiles/testFile.txt") != 'a') {
        printf("Test Failed: Result was: %c\n", most_frequent_symbol("./TestFiles/testFile.txt"));
        return 1;
    }

    printf("Test passed\n");
    return 0;
}