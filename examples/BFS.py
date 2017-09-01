#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = redefined-outer-name
# pylint: disable = unused-import

# ------
# BFS.py
# ------

# https://en.wikipedia.org/wiki/Breadth-first_search

from collections import deque
from typing      import Dict, List, Set

def bfs (g: Dict[int, Set[int]], u: int, v: int) -> List[int] :
    s = set()               # type: Set[int]
    q = deque([u])
    p = []                  # type: List[int]
    while q :
        t = q.popleft()
        p.append(t)         # add to the path
        if t == v :         # check the goal
            return p
        s.add(t)            # mark visited
        for w in g[t] :
            if w not in s : # check visited BEFORE PUSH
                q.append(w)
    return []

print("BFS.py")

# undirected graph
g = {0 : {1, 2, 4},
     1 : {0, 3, 5},
     2 : {0, 6},
     3 : {1},
     4 : {0, 5},
     5 : {1, 4},
     6 : {2}}       # type: Dict[int, Set[int]]

assert bfs(g, 0, 0) == [0]
assert bfs(g, 0, 1) == [0, 1]
assert bfs(g, 0, 2) == [0, 1, 2]
assert bfs(g, 0, 4) == [0, 1, 2, 4]
assert bfs(g, 0, 3) == [0, 1, 2, 4, 3]
assert bfs(g, 0, 5) == [0, 1, 2, 4, 3, 5]
assert bfs(g, 0, 6) == [0, 1, 2, 4, 3, 5, 6]
assert bfs(g, 0, 7) == []

print("Done.")
