#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    int n;
    vector <string> magnets;

    cin >> n;

    while (n > 0) {
        string magnet;
        cin >> magnet;
        magnets.push_back(magnet);
        n--;
    }

    int groups = 1;

    for (int i = 0; i < magnets.size(); i++) {
        if (i != magnets.size() - 1) {
            if (magnets[i][1] == magnets[i+1][0])
                groups++;
        }
    }

    cout << groups << endl;

    return 0;
}
