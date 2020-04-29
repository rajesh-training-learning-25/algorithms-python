# https://en.wikipedia.org/wiki/Bresenham's_line_algorithm

from typing import Tuple, List, Callable, Any

#                (x,   y)
Vector2D = Tuple[int, int]
Vectors2D = List[Vector2D]

# returns 1 or -1, value is used to increment x or y in a given direction
get_increment_value: Callable[[int], int] = lambda delta: int((delta > 0) - (delta < 0))


class BresenhamLine:
    """
    This implementation yields a list of 2-dimensional vectors, which can be used
    to plot a close approximation to a straight line between two points

    Variables start_vec and end_vec are set to private to have full control of getters/setters
    The vectors in self.vectors should always be updated when start_vec or end_vec are changed
    """

    def __init__(self, start_vec: Vector2D, end_vec: Vector2D) -> None:
        """
            start_vec: start vector of the line
            end_vec  : end   vector of the line

        >>> line = BresenhamLine((0, 0), (7, 5))
        >>> line.vectors
        [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 4), (6, 4), (7, 5)]

        >>> line.end_vec
        (7, 5)

        >>> line.end_vec = (7, 12)
        >>> line.vectors
        [(0, 0), (1, 1), (1, 2), (2, 3), (2, 4), (3, 5), (4, 6), (4, 7), (5, 8), (5, 9), (6, 10), (6, 11), (7, 12)]

        >>> line.end_vec = 100
        Traceback (most recent call last):
        TypeError: "end_vec" must be an indexable type, not type <class 'int'>

        >>> line.start_vec = (2, "a")
        Traceback (most recent call last):
        ValueError: "start_vec" must contain two integers, not (2, 'a')

        """
        self.__validate_input(start_vec, end_vec)
        self.vectors: Vectors2D = []
        self.__start_vec: Vector2D = start_vec
        self.__end_vec: Vector2D = end_vec
        self.__set_private_variables()
        self.__append_line_vectors()

    @property
    def start_vec(self) -> Vector2D:
        return self.__start_vec

    @start_vec.setter
    def start_vec(self, new_start_vec: Vector2D) -> None:
        self.__validate_input(new_start_vec, self.__end_vec)
        self.__start_vec = new_start_vec
        self.__set_private_variables()
        self.vectors.clear()
        self.__append_line_vectors()

    @property
    def end_vec(self) -> Vector2D:
        return self.__end_vec

    @end_vec.setter
    def end_vec(self, new_end_vec: Vector2D) -> None:
        self.__validate_input(self.__start_vec, new_end_vec)
        self.__end_vec = new_end_vec
        self.__set_private_variables()
        self.vectors.clear()
        self.__append_line_vectors()

    def __validate_input(self, first_arg: Any, second_arg: Any) -> None:
        """
        Valdidate the input by making sure we have two indexable types with two integers each
 
            first_arg : first  argument of the BresenhamLine(first_arg, second_arg) call
            second_arg: second argument of the BresenhamLine(first_arg, second_arg) call
        """

        def test_arg(arg: Any, arg_name: str) -> None:
            try:
                int(arg[0])
                int(arg[1])
            except TypeError:
                raise TypeError(
                    f'"{arg_name}" must be an indexable type, not type {type(arg)}'
                )
            except ValueError:
                raise ValueError(f'"{arg_name}" must contain two integers, not {arg}')

        test_arg(first_arg, "start_vec")
        test_arg(second_arg, "end_vec")

    def __set_private_variables(self) -> None:
        """
        Sets private variables each time start or end vec is changed
        These variables are only for internal usage
        """
        self.__x0: int = int(self.start_vec[0])
        self.__y0: int = int(self.start_vec[1])
        self.__x1: int = int(self.end_vec[0])
        self.__y1: int = int(self.end_vec[1])
        self.__delta_x: int = self.__x1 - self.__x0
        self.__delta_y: int = self.__y1 - self.__y0
        self.__x_inc: int = get_increment_value(self.__delta_x)
        self.__y_inc: int = get_increment_value(self.__delta_y)

        self.__delta_x = abs(self.__delta_x) * 2
        self.__delta_y = abs(self.__delta_y) * 2

    def __append_line_vectors(self) -> None:
        """
        Initiates the algorithm, by appending the first vector
        and finding the appropriate axis to follow by comparing deltas
        """
        self.vectors.append((self.__x0, self.__y0))
        decision: int
        if self.__delta_x >= self.__delta_y:
            decision = self.__delta_y - int(self.__delta_x / 2)
            self.__move_along_x(decision)
        else:
            decision = self.__delta_x - int(self.__delta_y / 2)
            self.__move_along_y(decision)

    def __move_along_x(self, decision: int) -> None:
        while self.__x0 != self.__x1:
            if decision >= 0:
                decision -= self.__delta_x
                self.__y0 += self.__y_inc
            decision += self.__delta_y
            self.__x0 += self.__x_inc
            self.vectors.append((self.__x0, self.__y0))

    def __move_along_y(self, decision: int) -> None:
        while self.__y0 != self.__y1:
            if decision >= 0:
                decision -= self.__delta_y
                self.__x0 += self.__x_inc
            decision += self.__delta_x
            self.__y0 += self.__y_inc
            self.vectors.append((self.__x0, self.__y0))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
