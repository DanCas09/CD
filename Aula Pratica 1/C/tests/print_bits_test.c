#include <stdio.h>
#include <string.h>
#include "../functions/print_bits.c"

// The console output is redirected to a local file for content verification purposes
int main() {

    // Open a file to redirect the console output
    FILE* outFile = freopen("./testFiles/console_output.txt", "w", stdout);
    if (outFile == NULL) {
        freopen("CON", "w", stdout);
        printf("Failed to open file for console output.\n");
        return 1;
    }

    print_bits(16);

    fclose(outFile);

    // Restore output redirection to the console
    freopen("CON", "w", stdout);


    // Open the written output file to read its contents
    FILE* inFile = fopen("./testFiles/console_output.txt", "r");
    if (inFile == NULL) {
        printf("Failed to open file for console output.\n");
        return 1;
    }

    // Compare file number to expected one
    char buffer[100];
    fgets(buffer, sizeof(buffer), inFile);

    fclose(inFile);

    if(strcmp(buffer, "00000000000000000000000000010000\n") != 0) {
        printf("Test Failed, result was: %s", buffer);
        return 1;
    }


    printf("Test passed\n");
    return 0;
}