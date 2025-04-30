#include <stdio.h>

void negative_file(char *input_file_name, char *output_file_name) {
	
	FILE *input_file = fopen(input_file_name,"rb");
	
	if(input_file == NULL) {
		 printf("Error openning the input file!");
		 return;
	 }

	FILE *output_file = fopen(output_file_name,"wb");
	
	if(output_file == NULL) {
		printf("Error creating the output file!");
		fclose(input_file);
		return;
	}
	
	char t;
	
	while((t = getc(input_file)) != EOF) {
		fputc(~t,output_file);
	}
	
	fclose(input_file);
	fclose(output_file);
}