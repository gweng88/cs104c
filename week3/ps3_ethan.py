from collections import defaultdict

def bf(n, m, edges, vis=None, best=None):
    if vis is None:
        vis = [False]*n
        vis[0] = True
    if best is None:
        best = [0]*n
    for rnd in range(n - 1):
        for u, v, c in edges:
            if not vis[v] or (vis[u] and best[v] < best[u] + c):
                vis[v] = True
                best[v] = best[u] + c
    if not vis[n - 1]:
        return None, vis, best
    else:
        return best[n - 1], vis, best

t = int(raw_input())
for q in range(t):
    n, m, k = map(int, raw_input().split())
    edges = []
    for i in range(m):
        u, v, c = map(int, raw_input().split())
        edges.append((u - 1, v - 1, c))
    first, vis, best = bf(n, m, edges)
    if first is None:
        print -1
    else:
        second, vis, best = bf(n, m, edges, vis, best)
        if second > first:
            print 'infinity'
        else:
            print second + k
