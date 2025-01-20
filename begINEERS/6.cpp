// #include <bits/stdc++.h>
// using namespace std;

// // Counts the number of (B, A) inversions in a string where B appears before A.
// long long countInversions(const string &s) {
//     long long countB = 0;
//     long long inversions = 0;
//     for (char c : s) {
//         if (c == 'B') {
//             ++countB;
//         } else {
//             // c == 'A', all previously seen B's form inversions with this A
//             inversions += countB;
//         }
//     }
//     return inversions;
// }

// int main() {
//     ios::sync_with_stdio(false);
//     cin.tie(nullptr);

//     int T;
//     cin >> T;
//     while (T--) {
//         string S1, S2;
//         cin >> S1 >> S2;

//         // Quick check: if the strings have different lengths or different counts of 'A', it's impossible
//         if (S1.size() != S2.size() || count(S1.begin(), S1.end(), 'A') != count(S2.begin(), S2.end(), 'A')) {
//             cout << -1 << "\n";
//             continue;
//         }

//         // Compute inversions
//         long long inv1 = countInversions(S1);
//         long long inv2 = countInversions(S2);

//         // If the parity of the inversion counts doesn't match, it's impossible
//         if ((inv1 % 2) != (inv2 % 2)) {
//             cout << -1 << "\n";
//         } else {
//             // Otherwise, the minimum number of operations is half the absolute difference in inversion counts
//             cout << abs(inv1 - inv2) / 2 << "\n";
//         }
//     }

//     return 0;
// }


#include <bits/stdc++.h>
// # 6.cpp

#include <bits/stdc++.h>
using namespace std;

// Counts the number of (B, A) inversions in a string where B appears before A.
long long countInversions(const string &s) {
    long long countB = 0;
    long long inversions = 0;
    for (char c : s) {
        if (c == 'B') {
            ++countB;
        } else {
            // c == 'A', all previously seen B's form inversions with this A
            inversions += countB;
        }
    }
    return inversions;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        string S1, S2;
        cin >> S1 >> S2;

        // Quick check: if the strings have different lengths or different counts of 'A', it's impossible
        if (S1.size() != S2.size() || count(S1.begin(), S1.end(), 'A') != count(S2.begin(), S2.end(), 'A')) {
            cout << -1 << "\n";
            continue;
        }

        // Compute inversions
        long long inv1 = countInversions(S1);
        long long inv2 = countInversions(S2);

        // If the parity of the inversion counts doesn't match, it's impossible
        if ((inv1 % 2) != (inv2 % 2)) {
            cout << -1 << "\n";
        } else {
            // Otherwise, the minimum number of operations is half the absolute difference in inversion counts
            cout << abs(inv1 - inv2) / 2 << "\n";
        }
    }

    return 0;
}

// from collections import deque
// def get_all_transformations(s):
//     """
//     Generates all possible transformations of a string by swapping adjacent pairs of 'A' and 'B' within a substring of length 3.
//     Args:
//         s: The input string.
//     Returns:
//         A list of all possible transformed strings.
//     """
//     transformations = []
//     n = len(s)
//     for i in range(n - 2):
//         substring = s[i:i+3]
//         if substring in {"AAB", "BAA", "BBA", "ABB"}:
//             transformations.append(s[:i] + substring[::-1] + s[i+3:])
//     return transformations
// def min_operations(s1, s2):
//     """
//     Calculates the minimum number of operations required to transform string s1 into string s2.
//     Args:
//         s1: The initial string.
//         s2: The target string.
//     Returns:
//         The minimum number of operations, or -1 if it's not possible to transform s1 into s2.
//     """
//     if s1 == s2:
//         return 0
//     queue = deque([(s1, 0)])
//     visited = set([s1])
//     while queue:
//         current, ops = queue.popleft()
//         for next_string in get_all_transformations(current):
//             if next_string == s2:
//                 return ops + 1
//             if next_string not in visited:
//                 visited.add(next_string)
//                 queue.append((next_string, ops + 1))
//     return -1
// if __name__ == "__main__":
//     T = int(input())
//     for _ in range(T):
//         s1, s2 = input().split()
//         result = min_operations(s1, s2)
//         print(result)


using namespace std;

// Counts the number of (B,A) inversions in a string where B appears before A.
long long countInversions(const string &s) {
    long long countB = 0;
    long long inversions = 0;
    for (char c : s) {
        if (c == 'B') {
            ++countB;
        } else {
            // c == 'A', all previously seen B's form inversions with this A
            inversions += countB;
        }
    }
    return inversions;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        string S1, S2;
        cin >> S1 >> S2;

        // Quick check: same length and same count of A (and B) or impossible
        if (S1.size() != S2.size()) {
            cout << -1 << "\n";
            continue;
        }
        if (count(S1.begin(), S1.end(), 'A') != count(S2.begin(), S2.end(), 'A')) {
            cout << -1 << "\n";
            continue;
        }

        // Compute inversions
        long long inv1 = countInversions(S1);
        long long inv2 = countInversions(S2);

        // If parity doesn't match, impossible
        if ((inv1 % 2) != (inv2 % 2)) {
            cout << -1 << "\n";
            continue;
        }

        // Otherwise, minimum number of operations is half the difference in inversion counts
        long long diff = llabs(inv1 - inv2);
        cout << diff / 2 << "\n";
    }

    return 0;
}


// ----
// #include <bits/stdc++.h>
// using namespace std;

// // Counts the number of (B, A) inversions in a string where B appears before A.
// long long countInversions(const string &s) {
//     long long countB = 0;
//     long long inversions = 0;
//     for (char c : s) {
//         if (c == 'B') {
//             ++countB;
//         } else {
//             // c == 'A', all previously seen B's form inversions with this A
//             inversions += countB;
//         }
//     }
//     return inversions;
// }

// int main() {
//     ios::sync_with_stdio(false);
//     cin.tie(nullptr);

//     int T;
//     cin >> T;
//     while (T--) {
//         string S1, S2;
//         cin >> S1 >> S2;

//         // Quick check: if the strings have different lengths or different counts of 'A', it's impossible
//         if (S1.size() != S2.size() || count(S1.begin(), S1.end(), 'A') != count(S2.begin(), S2.end(), 'A')) {
//             cout << -1 << "\n";
//             continue;
//         }

//         // Compute inversions
//         long long inv1 = countInversions(S1);
//         long long inv2 = countInversions(S2);

//         // If the parity of the inversion counts doesn't match, it's impossible
//         if ((inv1 % 2) != (inv2 % 2)) {
//             cout << -1 << "\n";
//         } else {
//             // Otherwise, the minimum number of operations is half the absolute difference in inversion counts
//             cout << abs(inv1 - inv2) / 2 << "\n";
//         }
//     }

//     return 0;
// }