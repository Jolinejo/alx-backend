#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        init
        """
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """eturn a dictionary with the following key-value pairs:
        index: the current start index of the return page.
        next_index: the next index to query with.
        page_size: the current page size
        data: the actual page of the dataset"""
        indexed_data = self.indexed_dataset()
        assert index >= 0
        assert index < len(indexed_data)

        next_index = index
        data = []
        return_dict = {}

        for i in range(page_size):
            while not indexed_data.get(next_index):
                next_index += 1
            data.append(indexed_data[next_index])
            next_index += 1

        return_dict['index'] = index
        return_dict['next_index'] = next_index
        return_dict['page_size'] = len(data)
        return_dict['data'] = data
        return return_dict
