#include <iostream>
#include <cmath>

using namespace std;

int main() {
    long int n, m, a;
    cin >> n >> m >> a;
    
    int64_t result = floor(static_cast<double>(-n) / a) * floor(static_cast<double>(-m) / a);
    cout << result << endl;

    return 0;
}
