#include <iostream>
#include <string>

using namespace std;

int main() {
    long long n;
    cin >> n;

    string s;
    cin >> s;
    
    char latin_alphabet[26] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                               'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                               'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                               'y', 'z'};
    
    string result = "YES";

    for (int i = 0; i < 26; i++) {
        if (s.find(latin_alphabet[i]) == string::npos && s.find(toupper(latin_alphabet[i])) == string::npos) {
            result = "NO";
            break;
        }
    }

    cout << result << endl;

    return 0;
}
