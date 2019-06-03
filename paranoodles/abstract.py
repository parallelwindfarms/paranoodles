## ------ language="Python" file="paranoodles/abstract.py"
from typing import Callable
from abc import (ABC, abstractmethod)

## ------ begin <<abstract-types>>[0]
class Vector(ABC):
    """Abstract base class for state variable of a problem.
    This should support simple arithmatic operations."""
    @abstractmethod
    def __add__(self, other: Vector) -> Vector:
        """Summation of two result vectors."""
        pass

    @abstractmethod
    def __sub__(self, other: Vector) -> Vector:
        """Difference between two result vectors."""
        pass
    
    @abstractmethod
    def __mul__(self, other: float) -> Vector:
        """Scale vector with scalar."""
	pass

    def __rmul__(self, other: float) -> Vector
	return self * other
## ------ end
## ------ begin <<abstract-types>>[1]
Problem = Callable[[Vector, float], Vector]
## ------ end
## ------ begin <<abstract-types>>[2]
Solution = Callable[[Vector, float, float], Vector]
## ------ end
## ------ end