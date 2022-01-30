from collections import namedtuple, defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, start, end, cost=1):
        self.graph[start].append([end, cost])
        self.graph[end].append([start, cost])

    def _create_ways_list(self, start, prev_v, distances):
        ways = {}

        for vertice, _ in prev_v.items():
            curr_vertice = vertice
            curr_path = [vertice]

            while curr_vertice != start:
                last_vertice = prev_v[curr_vertice]
                curr_path.insert(0, last_vertice)
                curr_vertice = last_vertice

            ways[vertice]= {
                "path": curr_path,
                "distance": distances[vertice]
            }
        
        return ways

    def dijkstra(self, start):
        distances = {vertice: float("inf") for vertice, _ in self.graph.items()}
        prev_v = {vertice: None for vertice, _ in self.graph.items()}

        distances[start] = 0
        prev_v[start] = start

        vertices = list(self.graph.keys())

        while vertices:
            vertice = min(vertices, key=lambda v: distances[v])
            vertices.remove(vertice)
            
            if distances[vertice] == float("inf"):
                break

            for neighbor, cost in self.graph[vertice]:

                if distances[vertice] + cost < distances[neighbor]:
                    distances[neighbor] = distances[vertice] + cost
                    prev_v[neighbor] = vertice

        return self._create_ways_list(start, prev_v, distances)





if __name__ == "__main__":
    # TEST

    graph = Graph()
    graph.add_edge("S", "A", 20)
    graph.add_edge("S", "D", 10)
    graph.add_edge("A", "B", 20)
    graph.add_edge("B", "D", 25)
    graph.add_edge("B", "C", 10)
    graph.add_edge("C", "D", 50)

    print(graph.dijkstra("S"))
