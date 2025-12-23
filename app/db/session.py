class FakeDBSession:
    def __init__(self):
        self.connected = True

    def close(self):
        self.connected = False
