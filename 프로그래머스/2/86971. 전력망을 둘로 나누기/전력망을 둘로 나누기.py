def dfs(start_node, adj_list, n): 
    visited = set()
    stack = [start_node]

    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)

            for destination in adj_list[current]:
                if destination not in visited:
                    stack.append(destination)
    return abs(len(visited) * 2 - n)

def solution(n, wires):
    answer = 101
    adj_list = [[] for _ in range(n+1)]

    for start, end in wires:
        adj_list[start].append(end)
        adj_list[end].append(start)

    for n1, n2 in wires:
        cut1 = adj_list[n1].pop(adj_list[n1].index(n2))
        cut2 = adj_list[n2].pop(adj_list[n2].index(n1))
        answer = min(answer, dfs(n1, adj_list, n))
        adj_list[cut1].append(cut2)
        adj_list[cut2].append(cut1)

    return answer