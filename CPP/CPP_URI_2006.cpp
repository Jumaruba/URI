#include <iostream>

using namespace std;

int main() {
    int a, b, soma;
    soma = 0;
    cin >> a;
    for (int x = 0; x < 5; x++) {
        cin >> b;
        if (b == a) {
            soma++;
        }
    }
    cout << soma << endl;
}