#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;
    double total = 0, p = 0;

    for (int i = 0; i < n; i++) {
        p = 0;
        cin >> p;
        total += p;
    }

    cout << total / n << endl;

    return 0;
}
