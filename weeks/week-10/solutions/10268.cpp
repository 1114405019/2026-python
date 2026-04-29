#include <iostream>

using namespace std;

typedef unsigned long long ull;
ull dp[101][64];

int main() {
    for (int j = 1; j <= 63; j++) {
        for (int i = 1; i <= 100; i++) {
            dp[i][j] = dp[i - 1][j - 1] + 1 + dp[i][j - 1];
        }
    }
    ull k, n;
    while (cin >> k >> n && k) {
        int ans = -1;
        if (k > 100) k = 100;
        for (int j = 1; j <= 63; j++) {
            if (dp[k][j] >= n) {
                ans = j;
                break;
            }
        }
        if (ans == -1) cout << "More than 63 trials needed.\n";
        else cout << ans << "\n";
    }
    return 0;
}
