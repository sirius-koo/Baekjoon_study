# 최소 스패닝 트리
import sys

input = sys.stdin.readline

def find(x):
    # 종료 조건 -> 자기 자신이 루트가 아니라면
    if x != parent[x]:
        parent[x] = find(parent[x])

    return parent[x]

def union(x, y):
    x_root = find(x)
    y_root = find(y)

    # Union이 안 된 경우 False 반환
    if x_root == y_root:
        return False

    if rank[x_root] > rank[y_root]:
        # 랭크가 작은 집합을 큰 집합에 붙이기
        parent[y_root] = x_root
    elif rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    else:
        # 랭크가 같은 경우
        parent[y_root] = x_root

        # 랭크 붙였기 때문에 x의 랭크를 1 더해주기
        rank[x_root] += 1

    # Union이 되면 True 반환
    return True
v, e = map(int, input().split())
edges = []

for _ in range(e):
    a, b, c = map(int, input().split())

    # (가중치, 노드1, 노드2)
    edges.append((c, a, b))

# 가중치(맨 앞 원소)가 적은 순으로 정렬
edges.sort()

total = 0
counts = 0 # 간선의 갯수 세기
parent = list(range(v + 1))
rank = [0] * (v + 1)

for c, a, b in edges:
    # 합쳐진다 = 최소스패닝트리가 될 수 있다.
    if union(a, b):
        # 간선의 가중치 합산
        total += c
        counts += 1
        
        if counts == v - 1:
            break

print(total)