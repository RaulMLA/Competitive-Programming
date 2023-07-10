#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    vector<int> colors(4);
    vector<int> checked;
    int result = 0;

    for (int i = 0; i < 4; i++) {
        cin >> colors[i];
    }

    for (int i = 0; i < 4; i++) {
        if (find(checked.begin(), checked.end(), colors[i]) == checked.end() && count(colors.begin(), colors.end(), colors[i]) > 1)
            result += count(colors.begin(), colors.end(), colors[i]) - 1;
        checked.push_back(colors[i]);
    }

    cout << result << endl;

    return 0;
}
