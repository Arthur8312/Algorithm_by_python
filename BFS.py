# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 19:05:52 2021

@author: arthur
"""
def bfs(graph,start):
     queue, visited = [start],[start]
     while queue:
            vertex = queue.pop()
            for i in graph[vertex]:
                    if i not in visited:
                          visited.append(i)
                          queue.append(i)
     return visited
 
G={"A":{"B","D"},
    "B":{"C","E"},
    "C":{"E","F"},
    "D":{"G"},
    "E":{"D","F","G","H"},
    "F":{"H"},
    "G":{"H"},
    "H":{}}
queue = ['A']
# print(bfs(G,'A'  ))