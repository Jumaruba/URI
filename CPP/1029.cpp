#include <iostream> 
#include <vector> 
#include <cstdlib> 
using namespace std ;


int main(){
	
	std::ios_base::sync_with_stdio(false);  
	int cases, value;  
	cin >> cases;  
	for (int j = 0; j < cases; j++){ 
		int actual_val = 1, prev_val = 0;  
		int actual_call = 1, prev_call = 1; 
		cin >> value;
		for (int i = 2; i < value+1; i++){    
			int temp = actual_val; 
			actual_val = temp + prev_val;  
			prev_val = temp; 
			
			temp = actual_call; 
			actual_call = temp + prev_call +1; 
			prev_call = temp; 
		}
		printf("fib(%d) = %d calls = %d\n", value, actual_call-1, actual_val) ;  
		
	}
		
	
} 
	
