#include <iostream>
#include <string>
#include <cctype>

using namespace std;

int main() {
    string string_a;
    string string_b;


    cin >> string_a >> string_b;

    for (size_t i = 0; i < string_a.length(); ++i) {
        string_a[i] = tolower(string_a[i]);
    }

    for (size_t i = 0; i < string_b.length(); ++i) {
        string_b[i] = tolower(string_b[i]);
    }


    if (string_a == string_b)
        cout << "0" << endl;
    else if (string_a < string_b)
        cout << "-1" << endl;
    else
        cout << "1" << endl;

    return 0;
}
