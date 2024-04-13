#!/usr/bin/env python3
"""
task 1
"""

import csv
import math
from typing import List, Any
from typing import Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns a start index and an end index
    corresponding to the range of indexes to return in a list
    for those particular pagination parameters.
    """
    return ((page - 1) * page_size, page * page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """return the appropriate page of the dataset
        """
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0
        ind = index_range(page, page_size)
        try:
            return self.dataset()[ind[0]:ind[1]]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """returns a dictionary containing the following key-value pairs:
        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer
        """
        total = math.ceil(len(self.dataset()) / page_size)
        next_page = page + 1 if page + 1 <= total else None
        prev_page = page - 1 if page > 1 else None
        data = self.get_page(page, page_size)
        hyper = {}
        hyper['page_size'] = len(data)
        hyper['page'] = page
        hyper['data'] = data
        hyper['next_page'] = next_page
        hyper['prev_page'] = prev_page
        hyper['total_pages'] = total
        return hyper
