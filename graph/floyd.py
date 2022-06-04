import math
from pprint import pprint


def get_path(parents_table, start_, end_):
    path = [end_]
    while end_ != start_:
        end_ = parents_table[end_][start_]
        path.append(end_)

    return list(reversed(path))


def floyd(graph_table):
    vertices_num = len(graph_table)
    parents_table = [[vx for vx in range(vertices_num)] for _ in range(vertices_num)]
    pprint(parents_table)
    for k in range(vertices_num):
        for i in range(vertices_num):
            for j in range(vertices_num):
                new_cost = graph_table[i][k] + graph_table[k][j]
                if new_cost < graph_table[i][j]:
                    graph_table[i][j] = new_cost
                    parents_table[i][j] = k

    return parents_table


if __name__ == "__main__":
    table = [[0, 2, math.inf, 3, 1, math.inf, math.inf, 10],
             [2, 0, 4, math.inf, math.inf, math.inf, math.inf, math.inf],
             [math.inf, 4, 0, math.inf, math.inf, math.inf, math.inf, 3],
             [3, math.inf, math.inf, 0, math.inf, math.inf, math.inf, 8],
             [1, math.inf, math.inf, math.inf, 0, 2, math.inf, math.inf],
             [math.inf, math.inf, math.inf, math.inf, 2, 0, 3, math.inf],
             [math.inf, math.inf, math.inf, math.inf, math.inf, 3, 0, 1],
             [10, math.inf, 3, 8, math.inf, math.inf, 1, 0],
             ]
    parents = floyd(table)
    pprint(table)
    pprint(parents)
    print(get_path(parents, 1, 4))

