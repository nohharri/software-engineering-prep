class DirectedGraph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, n, v):
        self.graph[n].append(v)
    
    def BFS(self, s):
        visited = {}
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            removed = queue.pop(0)
            for edgeNode in self.graph[removed]
                if edgeNode not in visited:
                    queue.append(edgeNode)
                    visited[edgeNode] = True
    
    def DFS(self, s):
        visited = {}

        def _DFS(s, visited):
            visited[s] = True
            for edgeNode in self.graph[s]
                if edgeNode not in visited:
                    _DFS(edgeNode, visited)
        
        _DFS(s)