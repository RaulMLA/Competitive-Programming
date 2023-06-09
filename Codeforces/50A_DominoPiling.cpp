#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int m, n;
    cin >> m >> n;

    cout << floor(static_cast<double>(m * n) / 2) << endl;

    return 0;
}
