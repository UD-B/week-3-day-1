class Point:
    def __init__(self, x, y):
        self.x = 0
        self.y = 0

class Line:
    count = 0
    def __init__(self, a, b):
        self.a = a
        self.b = b
        Line.count += 1
    def show(self):
        print(self.a, self.b)

    @classmethod
    def how_many(cls):
        print(cls.count)

    