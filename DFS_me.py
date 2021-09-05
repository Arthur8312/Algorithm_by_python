# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 09:06:01 2021

@author: arthur
"""

def dfs(graph, start, visited):
    visited.add(start)
    print(start)
    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)
    

G={"A":{"B","D"},
    "B":{"C","E"},
    "C":{"E","F"},
    "D":{"G"},
    "E":{"D","F","G","H"},
    "F":{"H"},
    "G":{"H"},
    "H":{}}

visit = set()
print(dfs(G, 'A', visit))