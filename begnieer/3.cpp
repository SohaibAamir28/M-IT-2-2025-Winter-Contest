#include <iostream>
#include <vector>
#include <algorithm>
#include <climits> // Include this for LLONG_MAX and LLONG_MIN
using namespace std;
int main() {
    int T;
    cin >> T;
    while (T--) {
        int N;
        cin >> N;
        long long min_s = LLONG_MAX;
        long long max_s = LLONG_MIN;
        for (int i = 0; i < N; ++i) {
            long long x, y;
            cin >> x >> y;
            long long s = x + y;
            if (s < min_s) min_s = s;
            if (s > max_s) max_s = s;
        }
        cout << 2 * (max_s - min_s) << endl;
    }
    return 0;
}

// #include <iostream>
// #include <vector>
// #include <algorithm>
// #include <climits> // Include this for LLONG_MAX and LLONG_MIN
// using namespace std;
// int main() {
//     int T;
//     cin >> T;
//     while (T--) {
//         int N;
//         cin >> N;
//         long long min_s = LLONG_MAX;
//         long long max_s = LLONG_MIN;
//         for (int i = 0; i < N; ++i) {
//             long long x, y;
//             cin >> x >> y;
//             long long s = x + y;
//             if (s < min_s) min_s = s;
//             if (s > max_s) max_s = s;
//         }
//         cout << 2 * (max_s - min_s) << endl;
//     }
//     return 0;
// }