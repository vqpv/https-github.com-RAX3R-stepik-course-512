class Buffer:
    def __init__(self):
        self.parts = []

    def add(self, *a):
        self.parts += a

        while len(self.parts) >= 5:
            print(sum(self.parts[:5]))
            self.parts = self.parts[5:]

    def get_current_part(self):
        return self.parts
