class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"(x,y)=({self.x},{self.y})"

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def describe(self):
        print(f'x={self.x}, y={self.y}')


p1 = Point(1, 2)
print(p1)
p0 = Point.zero()
print(p0)
