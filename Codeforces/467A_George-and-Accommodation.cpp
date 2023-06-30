#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;

    int result = 0;

    while (n != 0) {

        int p, q;

        cin >> p >> q;

        if (q - p >= 2)
            result++;

        n--;
    }

    cout << result << endl;

    return 0;
}
