import copy

class HillClimber():
    def __init__(self, railway) -> None:
        self.new_railway = copy.deepcopy(railway)

    def run(self) -> 'Railway':
        
