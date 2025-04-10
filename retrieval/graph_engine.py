# Optional bonus: handle graph traversal of relationships
class GraphEngine:
    def __init__(self, graph_data):
        self.graph = graph_data  # Assume it's a dict with relationships

    def traverse(self, keyword: str):
        """
        Very basic: retrieve directly connected nodes from graph.
        """
        return self.graph.get(keyword, [])
