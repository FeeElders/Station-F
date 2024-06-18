class Station():
    def __init__(self, name, x, y) -> None:
        self._name = name
        self._x = x
        self._y = y

        self.connections: dict['Station': 'Connection'] = {}

    def __repr__(self) -> str:
        return f"Station({self._name}, {self._x}, {self._y})"

    def __eq__(self, other) -> bool:
        if type(other) is not type(self):
            return False

        return self._name == other._name

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    def __hash__(self) -> int:
        return hash(self._name)
