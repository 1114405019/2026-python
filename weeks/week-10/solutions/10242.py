import sys

# Increase recursion depth for Tarjan's SCC
sys.setrecursionlimit(1000000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    it = iter(input_data)
    
    try:
        n = int(next(it))
        m = int(next(it))
    except StopIteration: return

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
    
    val = [0] * (n + 1)
    for i in range(1, n + 1):
        val[i] = int(next(it))
    
    start_node = int(next(it))
    p_count = int(next(it))
    is_bar = [False] * (n + 1)
    for _ in range(p_count):
        is_bar[int(next(it))] = True

    dfn = [0] * (n + 1)
    low = [0] * (n + 1)
    scc = [0] * (n + 1)
    in_stack = [False] * (n + 1)
    stack = []
    timer = 0
    scc_cnt = 0
    scc_val = []
    scc_bar = []

    def tarjan(u):
        nonlocal timer, scc_cnt
        timer += 1
        dfn[u] = low[u] = timer
        stack.append(u)
        in_stack[u] = True
        
        for v in adj[u]:
            if not dfn[v]:
                tarjan(v)
                low[u] = min(low[u], low[v])
            elif in_stack[v]:
                low[u] = min(low[u], dfn[v])
        
        if low[u] == dfn[u]:
            scc_cnt += 1
            curr_val = 0
            curr_bar = False
            while True:
                v = stack.pop()
                in_stack[v] = False
                scc[v] = scc_cnt
                curr_val += val[v]
                if is_bar[v]: curr_bar = True
                if u == v: break
            scc_val.append(curr_val)
            scc_bar.append(curr_bar)

    for i in range(1, n + 1):
        if not dfn[i]: tarjan(i)

    # Reconstruct DAG
    dag_adj = [set() for _ in range(scc_cnt + 1)]
    in_degree = [0] * (scc_cnt + 1)
    for u in range(1, n + 1):
        for v in adj[u]:
            if scc[u] != scc[v] and scc[v] not in dag_adj[scc[u]]:
                dag_adj[scc[u]].add(scc[v])
                in_degree[scc[v]] += 1

    # DP on DAG
    dist = [-1] * (scc_cnt + 1)
    dist[scc[start_node]] = scc_val[scc[start_node]-1]
    
    queue = [i for i in range(1, scc_cnt + 1) if in_degree[i] == 0]
    head = 0
    while head < len(queue):
        u = queue[head]
        head += 1
        for v in dag_adj[u]:
            if dist[u] != -1:
                dist[v] = max(dist[v], dist[u] + scc_val[v-1])
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    ans = 0
    for i in range(1, scc_cnt + 1):
        if scc_bar[i-1]:
            ans = max(ans, dist[i])
    print(ans)

if __name__ == "__main__":
    solve()
