from collections import defaultdict
import time
from utils.visualization import draw_plot

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start, plot_area):
        visited = set()
        queue = [start]
        visited.add(start)

        while queue:
            node = queue.pop(0)
            draw_plot(list(self.graph.keys()), [node], plot_area)
            time.sleep(1)

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

    def dfs(self, start, visited=None, plot_area=None):
        if visited is None:
            visited = set()

        visited.add(start)
        draw_plot(list(self.graph.keys()), [start], plot_area)
        time.sleep(1)

        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited, plot_area)
