class Station():
    def __init__(self, name, x, y) -> None:
        self._name = name
        self._x = x
        self._y = y

        self.connections: dict['Station': 'Connection'] = {}

    def __repr__(self) -> str:
        """ Represent station object in formatted string. """
        return f"Station({self._name}, {self._x}, {self._y})"

    def __eq__(self, other) -> bool:
        """ Check if self is the same object as other.

        Returns:
        bool
        """
        if type(other) is not type(self):
            return False

        return self._name == other._name

    def __ne__(self, other) -> bool:
        """ Check if self is not the same object as other.

        Returns:
        bool
        """

        return not self.__eq__(other)

    def __hash__(self) -> int:
        """ Make object hashable. """
        return hash(self._name)
