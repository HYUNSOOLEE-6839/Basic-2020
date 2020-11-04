class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add(self, x, y):
        self.x = x
        self.y = y
        return self.x + self.y
    def sub(self, x, y):
        self.x = x
        self.y = y
        return self.x - self.y
    def mul(self, x, y):
        self.x = x
        self.y = y
        return self.x * self.y
    def div(self, x, y):
        self.x = x
        self.y = y
        return self.x / self.y if self.y != 0 else None