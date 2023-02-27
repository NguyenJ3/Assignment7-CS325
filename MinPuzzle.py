
import heapq

def minEffort(puzzle):
    m, n = len(puzzle), len(puzzle[0])
    dist = [[float('inf') for _ in range(n)] for _ in range(m)]
    dist[0][0] = 0
    pq = [(0, 0, 0)]  # priority queue of (distance, row, col) tuples
    while pq:
        d, i, j = heapq.heappop(pq)
        if i == m-1 and j == n-1:
            return d