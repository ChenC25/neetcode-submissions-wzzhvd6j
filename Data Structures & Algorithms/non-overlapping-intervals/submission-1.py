class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals, key=lambda interval: interval[1])

        last_kept_end = float("-inf")
        removals = 0

        for start, end in sorted_intervals:
            if start < last_kept_end:
                # Reject this interval; keep the earlier-finishing choice.
                removals += 1
            else:
                # Equality is allowed: touching endpoints do not overlap.
                last_kept_end = end

        return removals