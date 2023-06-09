#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;

    int result = 0;

    while (n != 0) {

        string input;
        cin >> input;

        if (input[0] == 'X' && input[1] == '+' && input[2] == '+')
            result++;
        else if (input[0] == '+' && input[1] == '+' && input[2] == 'X')
            result++;
        else if (input[0] == 'X' && input[1] == '-' && input[2] == '-')
            result--;
        else if (input[0] == '-' && input[1] == '-' && input[2] == 'X')
            result--;

        n--;
    }

    cout << result << endl;

    return 0;
}
