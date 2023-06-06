#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector <string> results;
    int n;
    cin >> n;

    while (n != 0){
        string word;
        cin >> word;

        if (word.length() > 10) {
            int count = word.length() - 2;
            string new_word = word[0] + to_string(count) + word.back();
            results.push_back(new_word);
        } else {
            results.push_back(word);
        }

        n--;
    }

    for (int i = 0; i < results.size(); i++)
        cout << results[i] << endl;

    return 0;
}
