#include <iostream>

using namespace std;

int main() {
    
    int k, n, w;
    int total = 0;

    cin >> k >> n >> w;

    int i = 1;

    while (w != 0) {
        total += i * k;
        i++;
        w--;
    }

    if (total - n >= 0) 
        cout << total - n << endl;
    else
        cout << "0" << endl;

    return 0;
}
