class SnapshotArray:
    def __init__(self, length: int):
        self.array = [[(0, 0)] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.array[index].append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        # Binary search to find the nearest snapshot
        snapshots = self.array[index]
        left, right = 0, len(snapshots) - 1
        while left <= right:
            mid = (left + right) // 2
            if snapshots[mid][0] <= snap_id:
                left = mid + 1
            else:
                right = mid - 1
        return snapshots[right][1] if right >= 0 else 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)