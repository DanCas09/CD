#include <stdio.h>

#define n_bits_int sizeof(int) * 8

void print_bits(int val) {
	unsigned int mask = 1 << n_bits_int - 1;
	
	while(mask) {
		putchar(mask & val ? '1' : '0'); 
		mask = mask >> 1;
	}
	
	printf("\n");
}
