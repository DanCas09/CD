#include <stdio.h>

#define n_bits_int sizeof(int) * 8

int count_ones(int val) {
	int res = 0;
	int mask = 1;
	
	while(mask != (1 << n_bits_int)){
		if((val & mask) != 0){
			res++;
		}
		mask = mask << 1;
	}
	return res;
}