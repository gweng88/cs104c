#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = unused-import

# ------
# BFS.py
# ------

"""
https://en.wikipedia.org/wiki/Breadth-first_search
"""

from collections import deque
from typing      import Dict, List

def bfs1 (g: Dict[int, List[int]], s: int, t: int) -> List[int] :
    """
    breadth-first search
    g: adjacency list
    s: start vertex
    t: end   vertex
    returns search path
    """
    b    = [False] * len(g)          # type: List[bool]
    b[s] = True
    q    = deque([s])                # queue
    p    = []                        # type: List[int]
    while q :
        assert len(q) == len(set(q)) # check for duplicates
        u = q.popleft()              # pop queue
        p.append(u)                  # add to the path
        if u == t :                  # check the end
            return p
        for v in g[u] :
            if not b[v] :            # check visited BEFORE PUSH
                b[v] = True          # mark visited
                q.append(v)          # push queue
    return []

def bfs2 (g: Dict[int, List[int]], s: int, t: int) -> List[int] :
    """
    breadth-first search
    this implementation is still correct, BUT is inefficient
    duplicate elements are pushed onto the queue
    and the commented-out assertion will fail
    g: adjacency list
    s: start vertex
    t: end   vertex
    returns search path
    """
    b = [False] * len(g)             # type: List[bool]
    q = deque([s])                   # queue
    p = []                           # type: List[int]
    while q :
#       assert len(q) == len(set(q)) # check for duplicates
        u = q.popleft()              # pop queue
        if not b[u] :                # check visited AFTER POP
            p.append(u)              # add to the path
            if u == t :              # check the end
                return p
            b[u] = True              # mark visited
            for v in g[u] :
                q.append(v)          # push queue
    return []

def test (bfs) :
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

    assert bfs(g, 1,  2) == [1, 2]
    assert bfs(g, 1,  3) == [1, 2, 3]
    assert bfs(g, 1,  4) == [1, 2, 3, 4]
    assert bfs(g, 1,  5) == [1, 2, 3, 4, 5]
    assert bfs(g, 1,  7) == [1, 2, 3, 4, 5, 7]
    assert bfs(g, 1,  8) == [1, 2, 3, 4, 5, 7, 8]
    assert bfs(g, 1,  6) == [1, 2, 3, 4, 5, 7, 8, 6]
    assert bfs(g, 1,  9) == []
    assert bfs(g, 1, 11) == []

if __name__ == "__main__" : #pragma: no cover
    print("BFS.py")
    test(bfs1)
    print()
    test(bfs2)
    print("Done.")
