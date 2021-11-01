from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def __str__(self):
        return str(self.graph)

    def add_edge(self, start, end):
        self.graph[start].append(end)
        self.graph[end].append(start)
        self.graph[end].remove(start)
    
    def _dps(self, start, visited):
        visited[start] = True
        print(start)

        for vertice in self.graph[start]:
            if not visited[vertice]:
                self._dps(vertice, visited)
    
    def depth_search(self, start):
        visited = {key: False for key, _ in self.graph.items()}
        print(self.graph)
        self._dps(start, visited)

    def wide_search(self, start):
        visited = {key: False for key, _ in self.graph.items()}
        queue = [start]
        print(self.graph)

        while queue:
            start = queue.pop(0)
            visited[start] = True
            print(start)

            for vertice in self.graph[start]:
                if not visited[vertice]:
                    queue.append(vertice)
                    visited[vertice] = True



