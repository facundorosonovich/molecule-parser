"""
    This module provide some utils
"""
import logging


def replicate_pattern(pattern, total):
    """ Concat the pattern by the total provided """

    logging.info(pattern * int(total or 1))
    return pattern * int(total or 1)
