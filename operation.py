
class Operation:
    def __init__(self) -> None:
        pass

    def add(self, a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            raise ValueError("Inputs must be integers")
        return a + b


# x = Operation().add(1, 2)
# print(x)
