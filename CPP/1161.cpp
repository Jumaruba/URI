#include <iostream>
#include <stdio.h>
using namespace std;

int main(){
    long long int a, b, fat1, fat2;
    fat1 = 1;
    fat2 = 1;
    while ((scanf("%lld %lld",&a,&b) != EOF)) {
        for (int i=2; i<=a; i++){
            fat1*=i;
        }
        for (int j=2; j<=b; j++){
            fat2*=j;
        }
        long long int soma = fat1 + fat2;
        cout << soma << endl;
        fat1 = 1;
        fat2 = 1;

    }
}