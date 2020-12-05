def depth_first_search(graph, root):
    visited_vertices = list()
    graph_stack = list()
    node = root
    while len(graph_stack) > 0:
        