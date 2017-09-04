#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = unused-import

# ------
# DFS.py
# ------

"""
https://en.wikipedia.org/wiki/Depth-first_search
"""

from collections import deque
from typing      import Dict, List

def dfs1 (g: Dict[int, List[int]], s: int, t: int) -> List[int] :
    """
    depth-first search
    g: adjacency list
    s: start vertex
    t: end   vertex
    returns path
    """
    b    = [False] * len(g) # type: List[bool]
    b[s] = True
    q    = deque([s])       # stack
    p    = []               # type: List[int]
    while q :
        u = q.pop()         # pop stack
        p.append(u)         # add to the path
        if u == t :         # check the end
            return p
        for v in g[u] :
            if not b[v] :   # check visited BEFORE PUSH
                b[v] = True # mark visited
                q.append(v) # push stack
    return []

def dfs2 (g: Dict[int, List[int]], s: int, t: int) -> List[int] :
    """
    depth-first search
    g: adjacency list
    s: start vertex
    t: end   vertex
    returns path
    """
    b = [False] * len(g)    # type: List[bool]
    q = deque([s])          # stack
    p = []                  # type: List[int]
    while q :
        u = q.pop()         # pop stack
        if not b[u] :       # check visited AFTER POP
            p.append(u)     # add to the path
            if u == t :     # check the end
                return p
            b[u] = True     # mark visited
            for v in g[u] :
                q.append(v) # push stack
    return []

def test (dfs) :
    """
    Algorithm Design by Kleinberg and Tardos
    page 79
    undirected
    four connected components
    """
    g = {0  : [],
         1  : [2, 3],
         2  : [1, 3, 4, 5],
         3  : [1, 2, 5, 7, 8],
         4  : [2, 5],
         5  : [2, 3, 4, 6],
         6  : [5],
         7  : [3, 8],
         8  : [3, 7],
         9  : [10],
         10 : [9],
         11 : [12],
         12 : [11, 13],
         13 : [12]}             # type: Dict[int, List[int]]

    assert dfs(g, 1,  1) == [1]
    assert dfs(g, 1,  3) == [1, 3]
    assert dfs(g, 1,  8) == [1, 3, 8]
    assert dfs(g, 1,  7) == [1, 3, 8, 7]
    assert dfs(g, 1,  5) == [1, 3, 8, 7, 5]
    assert dfs(g, 1,  6) == [1, 3, 8, 7, 5, 6]
    assert dfs(g, 1,  9) == []
    assert dfs(g, 1, 11) == []

if __name__ == "__main__" : #pragma: no cover
    print("DFS.py")
    test(dfs1)
    test(dfs2)
    print("Done.")
