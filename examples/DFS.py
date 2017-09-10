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
from typing      import List

def dfs1 (g: List[List[int]], s: int, t: int) -> List[int] :
    """
    depth-first search
    this implementation does have DUPLICATES in the stack
    the commented-out assertion would fail
    g: adjacency list
    s: start vertex
    t: end   vertex
    returns path
    """
    b = [False] * len(g)             # type: List[bool]
    q = deque([s])                   # stack
    p = []                           # type: List[int]
    while q :
#       assert len(q) == len(set(q)) # DUPLICATES
        u = q.pop()                  # pop stack
        if not b[u] :                # check visited AFTER POP
            p.append(u)              # add to the path
            if u == t :              # check the end
                return p
            b[u] = True              # mark visited
            for v in g[u] :
                q.append(v)          # push stack
    return []

def dfs2 (g: List[List[int]], s: int, t: int) -> List[int] :
    """
    depth-first search
    this implementation does NOT have DUPLICATES in the stack, but is incorrect
    it does NOT visit the vertices in the correct order
    g: adjacency list
    s: start vertex
    t: end   vertex
    returns path
    """
    b    = [False] * len(g)          # type: List[bool]
    b[s] = True
    q    = deque([s])                # stack
    p    = []                        # type: List[int]
    while q :
        assert len(q) == len(set(q)) # NO DUPLICATES
        u = q.pop()                  # pop stack
        p.append(u)                  # add to the path
        if u == t :                  # check the end
            return p
        for v in g[u] :
            if not b[v] :            # check visited BEFORE PUSH
                b[v] = True          # mark visited
                q.append(v)          # push stack
    return []

def test (dfs) :
    """
    Algorithm Design by Kleinberg and Tardos
    page 79
    undirected
    three connected components
    """
    g = [[],                         #  0
         [ 2,  3],                   #  1
         [ 1,  3,  4,  5],           #  2
         [ 1,  2,  5,  7,  8],       #  3
         [ 2,  5],                   #  4
         [ 2,  3,  4,  6],           #  5
         [ 5],                       #  6
         [ 3,  8],                   #  7
         [ 3,  7],                   #  8
         [10, 11],                   #  9
         [ 9, 12],                   # 10
         [ 9, 12],                   # 11
         [13, 11, 10],               # 12
         [12]]                       # type: List[List[int]]

    assert dfs(g,  1,  0) == []
    assert dfs(g,  1,  1) == [1]
    assert dfs(g,  1,  2) == [1, 3, 8, 7, 5, 6, 4, 2]
    assert dfs(g,  1,  3) == [1, 3]
    assert dfs(g,  1,  4) == [1, 3, 8, 7, 5, 6, 4]
    assert dfs(g,  1,  5) == [1, 3, 8, 7, 5]
    assert dfs(g,  1,  6) == [1, 3, 8, 7, 5, 6]
    assert dfs(g,  1,  7) == [1, 3, 8, 7]
    assert dfs(g,  1,  8) == [1, 3, 8]
    assert dfs(g,  1,  9) == []
    assert dfs(g,  1, 10) == []
    assert dfs(g,  1, 11) == []
    assert dfs(g,  1, 12) == []
    assert dfs(g,  1, 13) == []

    assert dfs1(g, 11, 13) == [11, 12, 10, 9, 13]
    assert dfs2(g, 11, 13) == [11, 12, 10, 13]    # NOT DFS

if __name__ == "__main__" : #pragma: no cover
    print("DFS.py")
    test(dfs1)
    test(dfs2)
    print("Done.")
