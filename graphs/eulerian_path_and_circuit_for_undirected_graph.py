# Eulerian Path is a path in graph that visits every edge exactly once.
# Eulerian Circuit is an Eulerian Path which starts and ends on the same
# vertex.
# time complexity is O(V+E)
# space complexity is O(VE)


def dfs(u, graph, visited_edge, path=None):
    """
    Using dfs for finding eulerian path traversal
    Args:
        u: The start_node
        graph: The graph to check
        visited_edge: Specify if a node has been visited or not
        path: Optional path parameter

    Returns:
        Path

    Example:
        >>> visited_edge = [[False] * 11 for _ in range(11)]
        >>> dfs(1, {1: [2, 3], 2: [1, 3], 3: [1, 2]}, visited_edge)
        [1, 2, 3, 1]
        >>> dfs(5, {1: [2, 3, 4], 2: [1, 3], 3: [1], 4: [1, 5], 5: [4]}, visited_edge)
        [5, 4, 1]
        >>> dfs(1, {1: [], 2: [], 3: [1, 2]}, visited_edge)
        [1]
        >>> dfs(1, {1: [], 2: []}, visited_edge)
        [1]
        >>> dfs(1, {1: [], 2: []}, visited_edge, [1, 3])
        [1, 3, 1]
    """
    path = (path or []) + [u]
    for v in graph[u]:
        if visited_edge[u][v] is False:
            visited_edge[u][v], visited_edge[v][u] = True, True
            path = dfs(v, graph, visited_edge, path)
    return path


def check_circuit_or_path(graph, max_node):
    """
    For checking in graph has euler path or circuit

    Args:
        graph: The graph to check
        max_node: The maximum node to check

    Returns:
        Type of graph, and its circuit or path

    Example:
        >>> check_circuit_or_path({1: [2, 3], 2: [1, 3], 3: [1, 2]}, 10)
        (1, -1)
        >>> check_circuit_or_path({1: [2, 3, 4], 2: [1, 3], 3: [1, 2], 4: [], 5: [4]}, 10)
        (2, 5)
        >>> check_circuit_or_path({1: [2, 3, 1], 2: [2], 3: [1, 3], 4: [1], 5: []}, 10)
        (3, 4)
        >>> check_circuit_or_path({1: [], 2: [], 3: [1, 2]}, 10)
        (1, -1)
        >>> check_circuit_or_path({1: [], 2: []}, 10)
        (1, -1)
    """
    odd_degree_nodes = 0
    odd_node = -1
    for i in range(max_node):
        if i not in graph:
            continue
        if len(graph[i]) % 2 == 1:
            odd_degree_nodes += 1
            odd_node = i
    if odd_degree_nodes == 0:
        return 1, odd_node
    if odd_degree_nodes == 2:
        return 2, odd_node
    return 3, odd_node


def check_euler(graph, max_node):
    """
    Args:
        graph: The graph to check
        max_node: The maximum node to check

    Example:
        >>> check_euler({1: [2, 3], 2: [1, 3], 3: [1, 2]}, 10)
        graph has a Euler cycle
        [1, 2, 3, 1]
        >>> check_euler({1: [2, 3, 4], 2: [1, 3], 3: [1, 2], 4: [1, 5], 5: [4]}, 10)
        graph has a Euler path
        [5, 4, 1, 2, 3, 1]
        >>> check_euler({1: [2, 3, 1], 2: [2, 3, 4], 3: [1, 3], 4: [1], 5: []}, 10)
        graph is not Eulerian
        no path
        >>> check_euler({1: [], 2: [], 3: [1, 2]}, 10)
        graph has a Euler cycle
        [1]
        >>> check_euler({1: [], 2: []}, 10)
        graph has a Euler cycle
        [1]
    """
    visited_edge = [[False for _ in range(max_node + 1)] for _ in range(max_node + 1)]
    check, odd_node = check_circuit_or_path(graph, max_node)
    if check == 3:
        print("graph is not Eulerian")
        print("no path")
        return
    start_node = 1
    if check == 2:
        start_node = odd_node
        print("graph has a Euler path")
    if check == 1:
        print("graph has a Euler cycle")
    path = dfs(start_node, graph, visited_edge)
    print(path)


def main():
    g1 = {1: [2, 3, 4], 2: [1, 3], 3: [1, 2], 4: [1, 5], 5: [4]}
    g2 = {1: [2, 3, 4, 5], 2: [1, 3], 3: [1, 2], 4: [1, 5], 5: [1, 4]}
    g3 = {1: [2, 3, 4], 2: [1, 3, 4], 3: [1, 2], 4: [1, 2, 5], 5: [4]}
    g4 = {1: [2, 3], 2: [1, 3], 3: [1, 2]}
    g5 = {
        1: [],
        2: [],
        # all degree is zero
    }
    max_node = 10
    check_euler(g1, max_node)
    check_euler(g2, max_node)
    check_euler(g3, max_node)
    check_euler(g4, max_node)
    check_euler(g5, max_node)


if __name__ == "__main__":
    main()

    import doctest

    doctest.testmod()
