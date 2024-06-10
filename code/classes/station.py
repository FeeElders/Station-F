class Station():
    def __init__(self, name, x, y) -> None:
        self._name = name
        self._x = x
        self._y = y

        self.connections: dict['Station': 'Connection'] = {}

#    def __repr__(self) -> str:
 #       return f"{self.name}"
