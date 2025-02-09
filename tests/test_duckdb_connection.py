"""
This module contains tests for the duckdbConnection class.
"""
from backend.duckdb_connection import DuckdbConnection


def test_singleton_pattern(duckdb_connection):
    """
    Test the singleton pattern
    :param duckdb_connection:
    :return:
    """
    instance1 = DuckdbConnection()
    instance2 = DuckdbConnection()
    assert instance1 is instance2
