#include <iostream>
#include <cstring>
#include <algorithm>
#include <utility>
#include <vector>
#include <queue>
#include <stack>

using namespace std;

const int MAXN = 100005;

int num_nodes, num_edges;
vector<int> graph[MAXN];

bool dfs_visit[MAXN];
bool bfs_visit[MAXN];

void dfs(int node) {
    dfs_visit[node] = true;

    for (int next_node : graph[node]) {
        if (!dfs_visit[next_node]) {
            dfs(next_node);
        }
    }
}

void iter_dfs(int node) {
    stack<int> s;
    s.push(node);
    dfs_visit[node] = true;

    while (!s.empty()) {
        int cur = s.top();
        s.pop();

        for (int next_node : graph[cur]) {
            if (!dfs_visit[next_node]) {
                dfs_visit[next_node] = true;
                s.push(next_node);
            }
        }
    }
}

int count_components() {
    int ans = 0;
    memset(dfs_visit, 0, sizeof(dfs_visit));

    for (int i = 1; i <= num_nodes; ++i) {
        if (!dfs_visit[i]) {
            ++ans;
            // Replace with iter_dfs for speed + safety
            dfs(i);
        }
    }

    return ans;
}

int count_near(int start, int max_dist) {
    memset(bfs_visit, 0, sizeof(bfs_visit));

    queue<int> q;
    q.push(start);
    bfs_visit[start] = true;

    int ans = 0;
    for (int level = 0; level <= max_dist; ++level) {
        int level_size = q.size();
        ans += level_size;

        for (int i = 0; i < level_size; ++i) {
            int node = q.front();
            q.pop();

            for (int next_node : graph[node]) {
                if (!bfs_visit[next_node]) {
                    bfs_visit[next_node] = true;
                    q.push(next_node);
                }
            }
        }
    }

    return ans;
}

int main() {
    // The following 3 lines speed up input reading. With these lines, you
    // cannot mix cin and cout with scanf and printf.
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int num_cases;
    cin >> num_cases;

    int start, max_dist;

    while (num_cases-- > 0) {
        cin >> num_nodes >> num_edges >> start >> max_dist;
        for (int i = 1; i <= num_nodes; ++i) {
            graph[i].clear();
        }

        int u, v;
        for (int i = 0; i < num_edges; ++i) {
            cin >> u >> v;
            graph[u].push_back(v);
            graph[v].push_back(u);
        }

        int num_components = count_components();
        int reachable = count_near(start, max_dist);

        cout << num_components << ' ' << reachable << '\n';
    }

    return 0;
}
