class Station():
    def __init__(self, name, x, y) -> None:
        self.name = name
        self.x = x
        self.y = y

        self.connections: dict['Station': 'Connection'] = {}

#    def __repr__(self) -> str:
 #       return f"{self.name}"
