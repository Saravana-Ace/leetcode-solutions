import heapq
from collections import defaultdict

def prim_mst(from_nodes, to_nodes, weights):
    # Build adjacency list
    graph = defaultdict(list)
    for u, v, w in zip(from_nodes, to_nodes, weights):
        graph[u].append((w, v))
        graph[v].append((w, u))
    
    start_node = from_nodes[0]  # Arbitrary starting node
    visited = set()
    min_heap = [(0, start_node, None)] # (weight, node, previous node)
    mst = []
    total_weight = 0
    
    while min_heap and len(visited) < len(graph):
        weight, u, prev_u = heapq.heappop(min_heap)
        if u not in visited:
            visited.add(u)
            total_weight += weight
            if prev_u is not None:  # Skip adding the initial 0-weight (starting node) edge
                mst.append((prev_u, u, weight))  # Add edge to MST
            for next_weight, v in graph[u]:
                if v not in visited:
                    heapq.heappush(min_heap, (next_weight, v, u))  # Pass current node as prev_u
    
    return mst, total_weight

def split_mst_to_k_subtrees(mst, k):
    # Sort edges in MST by weight in descending order
    mst.sort(key=lambda x: x[2], reverse=True)
    
    # Remove the k-1 largest edges to create k clusters
    removed_edges = []
    for _ in range(k - 1):
        removed_edges.append(mst.pop(0))  # Remove and store the largest edges
    
    # The smallest weight among the removed edges is the maximum minimum weight
    return min(removed_edges, key=lambda x: x[2])[2]

# Input graph data
from_nodes = [1, 2, 3, 4, 5, 6]
to_nodes = [2, 3, 1, 5, 6, 4]
weights = [4, 5, 3, 2, 7, 6]
k = 3  # We want at most 3 subtrees (networks)

# Step 1: Get the Minimum Spanning Tree (MST)
mst, total_weight = prim_mst(from_nodes, to_nodes, weights)

# Step 2: Split MST into k subtrees and get the maximum minimum total weight
max_min_weight = split_mst_to_k_subtrees(mst, k)

print("Maximum minimum weight after forming", k, "subtrees:", max_min_weight)
