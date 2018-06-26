

class Graph():
    '''
    find_path -> (takes graph, start_node, end_node)
    returns the path from start_node to end_node within the graph
    '''

    # Class init with the graph object
    def __init__(self, graph):
        self.graph = graph


    def find_path(self, start_node, end_node, path=[]):
        path = path + [start_node]
        if start_node == end_node:
            return path
        if not self.graph.has_key(start_node):
            return []
        for node in self.graph[start_node]:
            if node not in path:
                    newpath = self.find_path(node, end_node, path)
                    if newpath:
                        return newpath
        return None


    def find_all_path(self, start_node, end_node, path=[]):
        path = path + [start_node]
        if start_node == end_node:
            return [path]
        if not self.graph.has_key(start_node):
            return []
        paths = []
        for node in self.graph[start_node]:
            if node not in path:
                new_path = self.find_all_path(node, end_node, path)
                for each_new_path in new_path:
                    paths.append(each_new_path)
        return paths


    def find_shortest_path(self, start_node, end_node, path=[]):
        path = path + [start_node]
        if start_node == end_node:
            return path
        if not self.graph.has_key(start_node):
            return []
        shortest_path = None
        for node in self.graph[start_node]:
            if node not in path:
                new_path = self.find_shortest_path(node, end_node, path)
                if new_path:
                    if not shortest_path or len(new_path) < len(shortest_path):
                        shortest_path = new_path
        return shortest_path


# def main():
#     graph = {
#         "vann": ["dcterms", "rdfs", "rdf"],
#         "foaf": ["geo", "vs", "dce", "rdf", "owl", "geo", "skos", "con", "schema", "rdfs", "dcterms"],
#         "skos": ["rdf", "rdfs", "dcterms"],
#         "dcterms": ["rdf", "rdfs", "skos", "foaf", "dce", "dctypes"],
#         "dce": ["dcterms", "rdf", "skos"],
#         "cc": ["rdf", "rdfs", "dcterms", "xhv"],
#         "vs": ["dce", "rdf", "vann"],
#         "schema": ["rdf", "rdfs", "foaf", "mo", "void", "dctype", "dcterms", "bibo", "dcat"]
#     }
#     shortest_path_graph = Graph(graph).find_shortest_path('vann', 'skos')
#     print shortest_path_graph
#     print Graph(graph).find_path('vann', 'skos')
#     # all_paths = Graph(graph).find_all_path('A','D')
#     # print all_paths
    

# if __name__ == '__main__':
#     main()

        
    
