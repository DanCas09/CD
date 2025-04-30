#include <stdio.h>
#include "../functions/negative_file.c"

int main() {

    negative_file("./TestFiles/inputTestFile.txt", "./TestFiles/outTestFile.txt");

    // Open the output file written by the function for further examination.
    FILE* outFile = fopen("./TestFiles/outTestFile.txt", "rb");
    if (outFile == NULL) {
        printf("Failed to open output file.\n");
        return 1;
    }

    // Read the inverted byte that was written by the function
    int byte = fgetc(outFile);
    fclose(outFile);

    /** 
     * Value in file is '1' with an ASCII code of 49.
    * We expect the inverted value to be 255 - 49, which equals the highest ASCII code minus the ASCII code of the value to invert (206).
    *
    **/
    if (byte != 206) {
        printf("Test Failed: Result was %c\n", byte);
        return 0;
    }

    printf("Test passed\n");
    return 0;
}