#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>

using namespace std;

const int MAXN = 500005;
vector<int> adj[MAXN], dag_adj[MAXN];
int val[MAXN], dfn[MAXN], low[MAXN], scc[MAXN], timer, scc_cnt;
long long scc_val[MAXN], dist[MAXN];
bool in_stack[MAXN], is_bar[MAXN], scc_bar[MAXN];
stack<int> st;

void tarjan(int u) {
    dfn[u] = low[u] = ++timer;
    st.push(u);
    in_stack[u] = true;
    for (int v : adj[u]) {
        if (!dfn[v]) {
            tarjan(v);
            low[u] = min(low[u], low[v]);
        } else if (in_stack[v]) {
            low[u] = min(low[u], dfn[v]);
        }
    }
    if (low[u] == dfn[u]) {
        scc_cnt++;
        while (true) {
            int v = st.top();
            st.pop();
            in_stack[v] = false;
            scc[v] = scc_cnt;
            scc_val[scc_cnt] += val[v];
            if (is_bar[v]) scc_bar[scc_cnt] = true;
            if (u == v) break;
        }
    }
}

int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    int n, m;
    if (!(cin >> n >> m)) return 0;
    for (int i = 0; i < m; i++) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v);
    }
    for (int i = 1; i <= n; i++) cin >> val[i];
    int start, p;
    cin >> start >> p;
    for (int i = 0; i < p; i++) {
        int b; cin >> b; is_bar[b] = true;
    }

    for (int i = 1; i <= n; i++) if (!dfn[i]) tarjan(i);

    for (int u = 1; u <= n; u++) {
        for (int v : adj[u]) {
            if (scc[u] != scc[v]) dag_adj[scc[u]].push_back(scc[v]);
        }
    }

    for (int i = 1; i <= scc_cnt; i++) {
        sort(dag_adj[i].begin(), dag_adj[i].end());
        dag_adj[i].erase(unique(dag_adj[i].begin(), dag_adj[i].end()), dag_adj[i].end());
    }

    vector<int> topo;
    vector<int> in_degree(scc_cnt + 1, 0);
    for (int i = 1; i <= scc_cnt; i++) {
        for (int v : dag_adj[i]) in_degree[v]++;
    }

    vector<int> q;
    for (int i = 1; i <= scc_cnt; i++) if (in_degree[i] == 0) q.push_back(i);
    int head = 0;
    while(head < q.size()){
        int u = q[head++];
        topo.push_back(u);
        for(int v : dag_adj[u]){
            if(--in_degree[v] == 0) q.push_back(v);
        }
    }

    fill(dist, dist + scc_cnt + 1, -1);
    dist[scc[start]] = scc_val[scc[start]];

    for (int u : topo) {
        if (dist[u] == -1) continue;
        for (int v : dag_adj[u]) {
            dist[v] = max(dist[v], dist[u] + scc_val[v]);
        }
    }

    long long ans = 0;
    for (int i = 1; i <= scc_cnt; i++) {
        if (scc_bar[i]) ans = max(ans, dist[i]);
    }
    cout << ans << endl;

    return 0;
}
