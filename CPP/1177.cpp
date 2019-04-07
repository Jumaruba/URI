#include <iostream>


using namespace std; 

int main(){
    int intervalo;
 
    cin >> intervalo; 
    for(int i= 0; i< 1000; i++){
        cout << "N[" << i << "] = " << i%intervalo << endl;  
    }

    return 0;
}