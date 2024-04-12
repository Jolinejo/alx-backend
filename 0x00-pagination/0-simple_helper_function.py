#!/usr/bin/env python3
"""
first task
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns a start index and an end index
    corresponding to the range of indexes to return in a list
    for those particular pagination parameters.
    """
    return ((page - 1) * page_size, page * page_size)
