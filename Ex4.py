class Vector:

    def __init__(self, *args):
        self.values = sorted([i for i in args if isinstance(i, int)])

    def __str__(self):
        if self.values:
            return f"Вектор {tuple(self.values)}"
        return "Пустой вектор"

    def __add__(self, x):
        if isinstance(x, int):
            return Vector(*[i + x for i in self.values])
        if isinstance(x, Vector):
            return Vector(*[self.values[i] + x.values[i] for i in \
                            range(len(self.values))]) if len(self.values) == len(x.values) \
                            else "Сложение векторов разной длины недопустимо"
        print(f"Вектор нельзя сложить с {x}")

    def __mul__(self,x):
        if isinstance(x, int):
            return Vector(*[i * x for i in self.values])
        if isinstance(x, Vector):
            return Vector(*[self.values[i] * x.values[i] for i in \
                            range(len(self.values))]) if len(self.values) == len(x.values) \
                            else "Умножение векторов разной длины недопустимо"
        print(f"Вектор нельзя умножать с {x}")
