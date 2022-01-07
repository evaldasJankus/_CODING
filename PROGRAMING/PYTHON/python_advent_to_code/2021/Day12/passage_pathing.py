from collections import Counter

def load_file(fname):
    caves_nodes = {}
    with open(fname) as f:
        for line in f:
            start, end = line.rstrip().split('-')
            if start == 'start':
                caves_nodes[start] = caves_nodes.get(start, []) + [end]
            elif end == 'start':
                caves_nodes[end] = caves_nodes.get(end, []) + [start]
            else:
                caves_nodes[start] = caves_nodes.get(start, []) + [end]
                caves_nodes[end] = caves_nodes.get(end, []) + [start]
    caves_nodes['end'] = []
    return caves_nodes

# -------------- FIRST PART --------------------
# Deapth First Search algorithm: https://neo4j.com/developer/graph-data-science/graph-search-algorithms/

def find_path(graph, visited, all_paths, start, end):
    visited.append(start)
    # print(visited)
    if visited and visited[-1] == end and not (visited in all_paths):
        all_paths.append(visited)
    else:
#
#         for u in graph[start]:
#             if (u.islower() and not(u in visited)) or (u.isupper()):
#                 find_path(graph, visited.copy(), all_paths, u, end)

# -------------- FIRST PART end --------------------
# -------------- SECOND PART --------------------
# Deapth First Search algorithm: https://neo4j.com/developer/graph-data-science/graph-search-algorithms/
def find_path_part2(graph, visited, all_paths, start, end):
    visited.append(start)
    c = Counter(visited)
    if visited and visited[-1] == end and not (visited in all_paths):
        all_paths.append(visited)
    else:

        for u in graph[start]:
            if (u.islower() and not(u in visited)) or (u.isupper()) or (u.islower() and (u in visited) and not([elem for elem in c if elem.islower() and c[elem] > 1])):
                find_path_part2(graph, visited.copy(), all_paths, u, end)
# -------------- SECOND PART end --------------------


def main():
    fname = 'data'
    caves_relation = load_file(fname)

    # print(caves_relation, type(caves_relation))

    all_paths = []
    find_path_part2(caves_relation, [], all_paths, 'start', 'end')
    print(f'Number of valid paths: {len(all_paths)}')
    # for path in all_paths: print(path)

if __name__ == '__main__':
    main()

# First part = *4*5
# Second part = 8*0*2

# Approach:
#
# The idea is to do Depth First Traversal of given directed graph.
# Start the DFS traversal from source.
# Keep storing the visited vertices in an array or HashMap say ‘path[]’.
# If the destination vertex is reached, print contents of path[].
