#include <stdio.h>
#include <stdlib.h>

char most_frequent_symbol(char* file_name) {
    FILE* file;
    if(!(file = fopen(file_name, "r"))) {
        printf("No such file.");
        exit(1);
    }

    int arr[256] = {0};

    char ch;
    int maxCount = 0;
    char res;

    while((ch = fgetc(file)) != EOF) {
        arr[ch]++;
        if (maxCount < arr[ch]) {
            maxCount = arr[ch];
            res = ch;
        }
    }
    fclose(file);
    return res;
}