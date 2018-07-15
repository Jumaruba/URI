#include <iostream>

using namespace std;

int main() {
    int soma = 0;
    int j;

    for (int x = 0; x < 3; x++) {
        cin >> j;
        soma += (j - 1);
    }

    cin >> j;
    soma += j;
    cout << soma << endl;
    return 0;
}