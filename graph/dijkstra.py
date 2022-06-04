import math


def find_lowest_cost_node(ways_cost_array, explored):
    min_vertex = -1
    edge_cost = math.inf
    for vertex, cost in enumerate(ways_cost_array):
        if cost < edge_cost and vertex not in explored:
            edge_cost = cost
            min_vertex = vertex

    return min_vertex


def get_path_dijkstra(start_, end_, parents):
    path = [end_]
    while end_ != start_:
        end_ = parents[path[-1]]
        path.append(end_)
    return list(reversed(path))


def dijkstra(graph_table, initial_vertex=0):
    vertices_num = len(graph_table)
    ways_cost_array = [math.inf] * vertices_num

    vertex = initial_vertex
    explored = {vertex}
    ways_cost_array[vertex] = 0
    parents = [vertex] * vertices_num
    while vertex != -1:
        for vx, cost in enumerate(graph_table[vertex]):
            if vx not in explored:
                new_cost = ways_cost_array[vertex] + cost
                if new_cost < ways_cost_array[vx]:
                    ways_cost_array[vx] = new_cost
                    parents[vx] = vertex
        vertex = find_lowest_cost_node(ways_cost_array, explored)
        if vertex >= 0:
            explored.add(vertex)
    return ways_cost_array, parents


if __name__ == "__main__":
    table = ((0, 3, 1, 3, math.inf, math.inf),
             (3, 0, 4, math.inf, math.inf, math.inf),
             (1, 4, 0, math.inf, 7, 5),
             (3, math.inf, math.inf, 0, math.inf, 2),
             (math.inf, math.inf, 7, math.inf, 0, 4),
             (math.inf, math.inf, 5, 2, 4, 0))
    result = dijkstra(table)
    print(f"Costs: {result[0]}", f"Parents: {result[1]}", sep="\n")
    print("Path: ", get_path_dijkstra(0, 4, result[1]))
