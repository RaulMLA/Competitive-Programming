#include <iostream>

using namespace std;

int main() {
    
    int n, h, cur = 0, count = 0;
    cin >> n >> h;

    while (n != 0) {
        cin >> cur;
        if (cur > h)
            count += 2;
        else
            count++;
        n--;
    }

    cout << count << endl;

    return 0;
}
