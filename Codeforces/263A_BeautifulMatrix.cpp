#include <iostream>

using namespace std;

int main() {
    int x, y, number;

    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            cin >> number;
            if (number == 1) {
                x = i;
                y = j;
            }
        }
    }

    cout << abs(2 - x) + abs(2 - y) << endl;

    return 0;
}
