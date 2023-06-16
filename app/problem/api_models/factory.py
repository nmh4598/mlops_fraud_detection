from abc import ABC, abstractmethod
from .base import ProblemBase
from .phase1 import Prob1Table, Prob2Table


class AbstractModelCreator(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def get_model(self, prob_id: int) -> ProblemBase:
        pass


class Phase1ModelCreator(AbstractModelCreator):
    def __init__(self) -> None:
        self.problems_dict = {1: Prob1Table, 2: Prob2Table}

    def get_model(self, prob_id: int) -> ProblemBase:
        return self.problems_dict[prob_id]


class Phase2ModelCreator(AbstractModelCreator):
    def __init__(self) -> None:
        self.problems_dict = {1: Prob1Table, 2: Prob2Table}

    def get_model(self, prob_id: int) -> ProblemBase:
        return self.problems_dict[prob_id]


class Phase3ModelCreator(AbstractModelCreator):
    def __init__(self) -> None:
        self.problems_dict = {1: Prob1Table, 2: Prob2Table}

    def get_model(self, prob_id: int) -> ProblemBase:
        return self.problems_dict[prob_id]


class ModelCreator:
    def __init__(self) -> None:
        self.creators_idx = {
            1: Phase1ModelCreator(),
            2: Phase2ModelCreator(),
            3: Phase3ModelCreator(),
        }

    def get_creator(self, phase_id: int) -> AbstractModelCreator:
        return self.creators_idx[phase_id]

    def create_model(self, phase_id: int, prob_id: int) -> ProblemBase:
        return self.get_creator(phase_id).get_model(prob_id)
