#include <bits/stdc++.h>

using namespace std;
#define int int64_t

// #ifndef ONLINE_JUDGE
// #include "debug.h"
// #else
// #define dbg(...)
// #endif

/*
*/

int32_t main() {
	// #ifndef ONLINE_JUDGE
	// freopen("in.txt", "r", stdin);
	// freopen("out.txt", "w", stdout);
	// freopen("err.txt", "w", stderr);
	// #endif
    int n, q;
    cin >> n >> q;
    vector<int> a(n);
    vector<int> cnt(n + 1, 0);
    for(int i = 0; i < n; i++){
        cin >> a[i];
        cnt[a[i]]++;
    }
    set<int> unused;
    for(int i = 1; i <= n; i++){
        if(!cnt[i]) unused.insert(i);
    }
    while(q--){
        int t;
        cin >> t;
        if(t == 1){
            int x, y;
            cin >> x >> y;
            x--;
            int prev = a[x];
            cnt[prev]--;
            if(cnt[prev] == 0) unused.insert(prev);
            if(cnt[y] == 0) unused.erase(y);
            cnt[y]++;
            a[x] = y;
        } else {
            int l, r;
            cin >> l >> r;
            if(unused.size()) cout << *unused.begin() << '\n';
            else{
                cout << (l > 1 ? a[l - 2] : a[r]) << '\n';
            }
        }
    }
}


// def busy_beaver(N, Q, a, queries):
//     results = []
//     for query in queries:
//         if query[0] == 1:
//             x, y = query[1], query[2]
//             a[x - 1] = y  # Update the array (1-based to 0-based index)
//         elif query[0] == 2:
//             l, r = query[1], query[2]
//             present = set(a[l - 1:r])  # Get the unique elements in the range
//             for missing in range(1, N + 1):
//                 if missing not in present:
//                     results.append(missing)
//                     break
//     return results
// import sys
// input = sys.stdin.read
// data = input().splitlines()
// N, Q = map(int, data[0].split())
// a = list(map(int, data[1].split()))
// queries = [list(map(int, line.split())) for line in data[2:]]
// results = busy_beaver(N, Q, a, queries)
// sys.stdout.write('\n'.join(map(str, results)) + '\n')



// --
// #include <bits/stdc++.h>

// using namespace std;
// #define int int64_t

// int32_t main() {
//     int n, q;
//     cin >> n >> q;
//     vector<int> a(n);
//     vector<int> cnt(n + 1, 0);
//     for(int i = 0; i < n; i++){
//         cin >> a[i];
//         cnt[a[i]]++;
//     }
//     set<int> unused;
//     for(int i = 1; i <= n; i++){
//         if(!cnt[i]) unused.insert(i);
//     }
//     while(q--){
//         int t;
//         cin >> t;
//         if(t == 1){
//             int x, y;
//             cin >> x >> y;
//             x--;
//             int prev = a[x];
//             cnt[prev]--;
//             if(cnt[prev] == 0) unused.insert(prev);
//             if(cnt[y] == 0) unused.erase(y);
//             cnt[y]++;
//             a[x] = y;
//         } else {
//             int l, r;
//             cin >> l >> r;
//             if(unused.size()) cout << *unused.begin() << '\n';
//             else{
//                 cout << (l > 1 ? a[l - 2] : a[r]) << '\n';
//             }
//         }
//     }
// }