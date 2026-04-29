#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

long long dp[2][1 << 12];
int grid[12][12];
const int MOD = 1000000007;

void solve(int t) {
    int N, M;
    cin >> N >> M;
    for (int i = 0; i < N; i++)
        for (int j = 0; j < M; j++) cin >> grid[i][j];

    memset(dp, 0, sizeof(dp));
    dp[0][0] = 1;
    int cur = 0;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            int next = cur ^ 1;
            memset(dp[next], 0, sizeof(dp[next]));
            for (int mask = 0; mask < (1 << (M + 1)); mask++) {
                if (!dp[cur][mask]) continue;
                int up = (mask >> j) & 1;
                int left = (mask >> (j + 1)) & 1;
                if (grid[i][j] == 0) {
                    if (!up && !left) {
                        dp[next][mask] = (dp[next][mask] + dp[cur][mask]) % MOD;
                    }
                } else {
                    // 1: Connect up and left
                    if (up && left) dp[next][mask ^ (1 << j) ^ (1 << (j + 1))] = (dp[next][mask ^ (1 << j) ^ (1 << (j + 1))] + dp[cur][mask]) % MOD;
                    // 2: Up to down/right, Left to right/down
                    if (up && !left) {
                        dp[next][mask] = (dp[next][mask] + dp[cur][mask]) % MOD; // up to down
                        dp[next][mask ^ (1 << j) ^ (1 << (j + 1))] = (dp[next][mask ^ (1 << j) ^ (1 << (j + 1))] + dp[cur][mask]) % MOD; // up to right
                    }
                    if (!up && left) {
                        dp[next][mask] = (dp[next][mask] + dp[cur][mask]) % MOD; // left to right
                        dp[next][mask ^ (1 << j) ^ (1 << (j + 1))] = (dp[next][mask ^ (1 << j) ^ (1 << (j + 1))] + dp[cur][mask]) % MOD; // left to down
                    }
                    if (!up && !left) {
                        dp[next][mask ^ (1 << j) ^ (1 << (j + 1))] = (dp[next][mask ^ (1 << j) ^ (1 << (j + 1))] + dp[cur][mask]) % MOD; // down and right
                    }
                }
            }
            cur = next;
        }
        // Shift mask for next row
        int next = cur ^ 1;
        memset(dp[next], 0, sizeof(dp[next]));
        for (int mask = 0; mask < (1 << M); mask++) {
            dp[next][mask << 1] = dp[cur][mask];
        }
        cur = next;
    }

    cout << "Case " << t << ": " << dp[cur][0] << "\n";
}

int main() {
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) solve(i);
    return 0;
}
