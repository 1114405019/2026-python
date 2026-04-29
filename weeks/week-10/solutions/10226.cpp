#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int N, p[16], last[16];
bool used[16], bad[16][17];
bool first_perm;

void dfs(int d) {
    if (d == N) {
        int i = 0;
        if (!first_perm) {
            while (i < N && p[i] == last[i]) i++;
        }
        for (int j = 0; j < i; j++) cout << ' ';
        for (int j = i; j < N; j++) {
            cout << (char)(p[j] + 'A');
            last[j] = p[j];
        }
        cout << '\n';
        first_perm = false;
        return;
    }
    for (int i = 0; i < N; i++) {
        if (!used[i] && !bad[i][d + 1]) {
            used[i] = true;
            p[d] = i;
            dfs(d + 1);
            used[i] = false;
        }
    }
}

int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    while (cin >> N) {
        for (int i = 0; i < N; i++) {
            for (int j = 1; j <= N; j++) bad[i][j] = false;
            int pos;
            while (cin >> pos && pos) bad[i][pos] = true;
        }
        first_perm = true;
        for (int i = 0; i < N; i++) used[i] = false, last[i] = -1;
        dfs(0);
    }
    return 0;
}
