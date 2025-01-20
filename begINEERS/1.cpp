// 1-MIT Time (C 11)

#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int T;
    cin >> T;
    while (T--) {
        int N;
        cin >> N;
        int k = 1;
        while (pow(5, k) < N) {
            k++;
        }
        if (k == 1) {
            cout << "MIT time" << endl;
        } else {
            cout << "MIT^" << k << " time" << endl;
        }
    }
    return 0;
}