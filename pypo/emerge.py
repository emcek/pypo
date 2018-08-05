"""Python Portage."""
import re
from pprint import pprint
from typing import List, NamedTuple, Dict

EmergeRecord = NamedTuple('EmergeRecord', [('action', str),
                                           ('category', str),
                                           ('package', str),
                                           ('version', str),
                                           ('flags', Dict[str, str]),
                                           ('size', int)])


def parse(data: str) -> List[EmergeRecord]:
    """
    Parse portage data from string.

    :param data: emerge log data in string
    :return: List of emerge records
    """
    emerge_line = re.compile(r'\[ebuild\s*'
                             r'([NSUDrRFfIBb#*~]+)'  # action
                             r'\s*\]\s*'
                             r'([0-9a-z\-]*)'  # category
                             r'/'
                             r'([0-9A-Za-z.\-]*)'  # package
                             r'-'
                             r'([0-9.]*)'  # version
                             r'(?::?.*::gentoo\]?\s*)'
                             r'((?:[0-9A-Z_]*=".*")*)'  # flags
                             r'\s*'
                             r'([\d,]*\s+[KMiB]*)')  # size
    emerge_data = [list(emerge_datum) for emerge_datum in emerge_line.findall(data)]

    pprint(emerge_data, width=200)
    pprint(len(emerge_data))

    for i, emerge_datum in enumerate(emerge_data):
        for j, element in enumerate(emerge_datum):
            if j == 4:  # flags
                emerge_data[i][j] = dict(zip(element.split('"')[0::2], element.split('"')[1::2]))
                emerge_data[i][j] = {key.strip('='): val for key, val in emerge_data[i][j].items()}
            elif j == 5:  # size
                emerge_data[i][j] = convert2kib(element)

    database = [EmergeRecord(*emerge_datum) for emerge_datum in emerge_data]
    return database


def convert2kib(size: str) -> int:
    """
    Convert string representation of size in KiB, MiB or in GiB to KiB as integer.

    :param size: size with unit
    :return: size in KiB
    """
    match = re.search(r'([\d,]+)\s*([KMGiB]+)', size)
    size = match.group(1).replace(',', '')
    unit = match.group(2).upper()

    size_kib = 0
    if 'K' in unit:
        size_kib = int(size)
    elif 'M' in unit:
        size_kib = int(size) * 1024
    elif 'G' in unit:
        size_kib = int(size) * 1024 * 1024

    return size_kib
