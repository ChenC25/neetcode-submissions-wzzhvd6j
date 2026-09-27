import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # Each entry is (earliest possible time, row, column).
        heap = [(grid[0][0], 0, 0)]
        visited = set()
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while heap:
            time, row, col = heapq.heappop(heap)

            # A square may have been added through multiple routes.
            if (row, col) in visited:
                continue
            visited.add((row, col))

            # The first time we remove the destination is optimal.
            if row == n - 1 and col == n - 1:
                return time

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    # We may need to wait for the neighbor to become submerged.
                    next_time = max(time, grid[nr][nc])
                    heapq.heappush(heap, (next_time, nr, nc))