#include <iostream>

using namespace std;


int algarismos(int n){   //figuring out how many numbers the input has
    int contador = 1;

    while (n/10 != 0){
        n = n/10;
        contador ++;
    }
	return contador;
	
        
}

int main(){
    int x, quantidade, numero, resto, contador;
    while (cin >> x){ 
        numero = 1;
        quantidade = algarismos(x);
        for (int i = 0; i< quantidade; i++ ){  // creating a number called "numero" formed only by "1" numbers and numero> x (input)
            numero = numero*10+1;
        }

        resto = numero%x;    // numero divided by x (input), has rest resto
        contador = quantidade +1;  //quantity of "1" in numero

        while (resto != 0){   
            resto = resto*10+1;   // acrescenting "1" to the number
            resto = resto%x;  //figuring out the new rest
            contador ++;      // increasing the number of "1"'s at the number
        }

        cout << contador << endl;
        
    }
return 0;
}


//https://www.urionlinejudge.com.br/judge/pt/problems/view/1213
