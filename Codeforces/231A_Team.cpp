#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;
    int count = 0;

    while (n > 0) {
        int problem = 0, a, b, c;
        cin >> a >> b >> c;
        if (a == 1)
            problem++;
        if (b == 1)
            problem++;
        if (c == 1)
            problem++;
        if (problem >= 2)
            count++;
        n--;
    }

    cout << count << endl;

    return 0;
}
