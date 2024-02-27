class SnapshotHelper:
    def __init__(self, page, snapshot):
        self.page = page
        self.snapshot = snapshot

    def assert_snapshot(self):
        return self.snapshot(self.page.screenshot())
