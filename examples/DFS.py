#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = pointless-string-statement
# pylint: disable = redefined-outer-name
# pylint: disable = unused-import

# ------
# DFS.py
# ------

# https://en.wikipedia.org/wiki/Depth-first_search

from collections import deque
from typing      import Dict, List, Set

def dfs (g: Dict[int, Set[int]], u: int, v: int) -> List[int] :
    s = set()               # type: Set[int]
    q = deque([u])
    p = []                  # type: List[int]
    while q :
        t = q.pop()
        p.append(t)         # add to the path
        if t == v :         # check the goal
            return p
        s.add(t)            # mark visited
        for w in g[t] :
            if w not in s : # check visited BEFORE PUSH
                q.append(w)
    return []

def dfs2 (g: Dict[int, Set[int]], u: int, v: int) -> List[int] :
    s = set()               # type: Set[int]
    q = deque([u])
    p = []                  # type: List[int]
    while q :
        t = q.pop()
#       if t not in s :
        p.append(t)         # add to the path
        if t == v :         # check the goal
            return p
        if t not in s :     # check visited AFTER POP
            s.add(t)        # mark visited
            for w in g[t] :
                q.append(w)
    return []

def dfs3 (g: Dict[int, Set[int]], u: int, v: int) -> List[int] :
    s = set()               # type: Set[int]
    s.add(u)
    q = deque([u])
    p = []                  # type: List[int]
    while q :
        t = q.pop()
        p.append(t)         # add to the path
        if t == v :         # check the goal
            return p
        for w in g[t] :
            if w not in s : # check visited BEFORE PUSH
                s.add(w)    # mark visited
                q.append(w)
    return []

print("DFS.py")

# undirected graph
g = {0 : {1, 2, 4},
     1 : {0, 3, 5},
     2 : {0, 6},
     3 : {1},
     4 : {0, 5},
     5 : {1, 4},
     6 : {2}}       # type: Dict[int, Set[int]]

assert dfs(g, 0, 6) == [0, 4, 5, 1, 3, 2, 6]
assert dfs(g, 0, 7) == []

print(dfs2(g, 0, 6))
print(dfs2(g, 0, 7))

print(dfs3(g, 0, 6))
print(dfs2(g, 0, 7))

print("Done.")

""" #pragma: no cover
% DFS.py
DFS.py
[0, 4, 5, 4, 1, 5, 3, 1, 0, 0, 2, 6]
[]
[0, 4, 5, 2, 6]
[]
Done.
"""
