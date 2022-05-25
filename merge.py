from typing import Iterable, Set, Dict, Generator


def merge(*args: Iterable) -> Generator:
    """
     Accepts as arguments an arbitrary number of iterables (lists, tuples),
     each of which generates sorted numbers, \
     function merges the outputs of the iterables
    :param args: Iterable
    :return: generator
    """
    iterators = []
    empty_iterators_indexes = []
    values = {}
    if not args:
        raise Exception(f"Function must have at least one iterable")
    for arg in args:
        if not isinstance(arg, Iterable):
            raise Exception(f'{arg} is not an Iterable.')
        if isinstance(arg, Set):
            raise Exception(f"{arg} is Set and cannot be used in the function "
                            f"as sets are unordered.")
        if isinstance(arg, Dict):
            raise Exception(f"{arg} is Dictionary and cannot be used in the function "
                            f"as dicts are unordered.")
        iterators.append(iter(arg))

    while len(empty_iterators_indexes) != len(args):
        for idx, iterator in enumerate(iterators):
            if idx in empty_iterators_indexes or idx in values:
                continue
            try:
                values[idx] = next(iterator)
                if not isinstance(values[idx], int):
                    type_of_value = type(values[idx])
                    raise Exception(f"Returned wrong type of data. "
                                    f"Expected int. "
                                    f"Actual {type_of_value}")
            except StopIteration:
                empty_iterators_indexes.append(idx)

        if values:
            yield values.pop(min(values, key=values.get))
