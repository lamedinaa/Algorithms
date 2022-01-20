### this solve the shortest path problem
import heapq

class vertex:

    def __init__(self,node_ini,node_fini,weight):
        self.node_ini = node_ini
        self.node_fini = node_fini
        self.weight = weight

class node:

    def __init__(self, name):
        self.name = name 
        self.visited = False
        self.min_distance = float('inf')
        self.predececessor = None
        self.adjency_list = []


    def __lt__(self,other_node):
        return self.min_distance < other_node.min_distance

class dijkstra:

    def __init__(self):
        self.heap = []

    def calculate(self,start_node):
        start_node.min_distance = 0
        heapq.heappush(self.heap,start_node)       ### transform list heap into heap

        while self.heap:
            actual_node = heapq.heappop(self.heap)  ### we pop the node with the lowest min_distance
            
            if actual_node.visited:
                continue
            
            for vertex in actual_node.adjency_list:
                u = vertex.node_ini
                v = vertex.node_fini
                new_distance = u.min_distance + vertex.weight

                if new_distance < v.min_distance:
                    v.predececessor = u
                    v.min_distance = new_distance
                    heapq.heappush(self.heap,v)
        

        start_node.visited = True

    @staticmethod
    def get_shortest_path(vertex):

        print("Shortest path to vertext is: %s"%str(vertex.min_distance))
        actual_vertex = vertex

        while actual_vertex.predecessor is not None:
            print("%s " % actual_vertex.name)
            actual_vertex = actual_vertex.predecessor







