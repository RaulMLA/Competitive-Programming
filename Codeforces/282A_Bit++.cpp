#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;

    int result = 0;

    while (n != 0) {

        string input;
        cin >> input;

        if (input == "++X" || input == "X++")
            result++;
        else if (input == "--X" || input == "X--")
            result--;

        n--;
    }

    cout << result << endl;

    return 0;
}
