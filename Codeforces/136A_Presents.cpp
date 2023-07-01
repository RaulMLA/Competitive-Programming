#include <iostream>
#include <vector>

using namespace std;

int main() {
    
    int n;
    cin >> n;

    vector <int> gifts(n);
    vector <int> result(n);

    for (int i = 0; i < n; i++)
        cin >> gifts[i];

    for (int i = 0; i < gifts.size(); i++)
        result[gifts[i] - 1] = i + 1;
    
    for (int i = 0; i < result.size(); i++)
        cout << result[i] << " ";

    cout << endl;

    return 0;
}
