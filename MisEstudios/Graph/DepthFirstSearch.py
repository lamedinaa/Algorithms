### DFS depth first search 
class Node:

    def __init__(self,name):
        self.name = name
        self.adjency_list = []
        self.visited = False



def DFS(start_node):

    stack = [start_node]

    while stack:
        actual_node = stack.pop()    ##this make the diference between DFS and BFS
        print(actual_node.name)
        for node in actual_node.adjency_list:
            if not node.visited:
                stack.append(node)
                node.visited = True

    





if __name__=="__main__":

    node1 = Node("a")
    node2 = Node("b")
    node3 = Node("c")
    node4 = Node("d")

    node1.adjency_list.append(node2)
    node2.adjency_list.append(node3)
    node2.adjency_list.append(node4)


    DFS(node2)



