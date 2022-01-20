### BreathFirstSearch BFS

class Node():

    def __init__(self,name):
        self.name = name 
        self.adjency_list = []
        self.visited = False


def Breath_First_Search(start_node):

    queue = [start_node]

    while queue:
        actual_node = queue.pop(0)
        print(actual_node.name)
        for adjency_node in actual_node.adjency_list:
            if not adjency_node.visited:
                queue.append(adjency_node)
                adjency_node.visited = True

if __name__ == "__main__":
    node1 = Node("a")
    node2 = Node("b")
    node3 = Node("c")
    node4 = Node("d")

    node1.adjency_list.append(node2)
    node2.adjency_list.append(node3)
    node3.adjency_list.append(node1)
    node1.adjency_list.append(node4)
    node4.adjency_list.append(node2)

    Breath_First_Search(node1)

