#!/usr/bin/python3


def find_peak(list_of_integers):
        """
    Finds a peak
    """
    if not list_of_integers:
        return None

    for idx, i in enumerate(list_of_integers):
        if i == list_of_integers[0] and i > list_of_integers[1]:
            return i

        if i > list_of_integers[idx - 1] and i > list_of_integers[idx + 1]:
            return i

    return list_of_integers[len(list_of_integers) - 1]
