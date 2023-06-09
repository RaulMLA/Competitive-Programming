#include <iostream>
#include <vector>

using namespace std;

int main() {
    
    int n, k, count = 0;
    cin >> n >> k;

    vector<int> scores(n);

    for (int i = 0; i < n; i++)
        cin >> scores[i];
    
    int item_k = scores[k - 1];

    for (int i = 0; i < n; i++) {
        if (scores[i] >= scores[k - 1] && scores[i] != 0)
            count++;
    }

    cout << count << endl;    

    return 0;
}
