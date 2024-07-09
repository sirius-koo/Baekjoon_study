import sys

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])

    return parent[x]

def union(x, y):
    x_root, y_root = find(x), find(y)

    if x_root == y_root:
        return False

    if rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    elif rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    else:
        parent[x_root] = y_root
        rank[y_root] += 1

    return True

input = sys.stdin.readline

N, M = map(int, input().split())
edges = []

for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((C, A, B))

edges.sort()
parent = list(range(N + 1))
rank = [0] * (N + 1)
counts, total, max_cost = 0, 0, 0

for C, A, B in edges:
    if union(A, B):
        total += C
        max_cost = max(max_cost, C)
        counts += 1

        if counts == (N - 1):
            break

print(total - max_cost)
