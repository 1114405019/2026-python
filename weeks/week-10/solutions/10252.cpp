#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long ll;

void solve() {
    int N;
    if (!(cin >> N)) return;
    vector<ll> x(N), y(N);
    for (int i = 0; i < N; i++) cin >> x[i] >> y[i];
    sort(x.begin(), x.end());
    sort(y.begin(), y.end());

    ll mid_x1 = x[(N - 1) / 2];
    ll mid_x2 = x[N / 2];
    ll mid_y1 = y[(N - 1) / 2];
    ll mid_y2 = y[N / 2];

    ll sum_dist = 0;
    for (int i = 0; i < N; i++) {
        sum_dist += abs(x[i] - mid_x1) + abs(y[i] - mid_y1);
    }

    ll count = (mid_x2 - mid_x1 + 1) * (mid_y2 - mid_y1 + 1);
    cout << sum_dist << " " << count << "\n";
}

int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    int T;
    if (!(cin >> T)) return 0;
    while (T--) solve();
    return 0;
}
