"""
This module is responsible for creating a database connection and returning the session.
The session is used to interact with the database.
"""

import duckdb


class DuckdbConnection:
    """
    Singleton class to create a Duckdb connection
    """
    _instance = None

    def __new__(cls):
        """
        Creates a singleton instance of the database connection
        :return: database connection instance
        """
        if cls._instance is None:
            cls._instance = super(DuckdbConnection, cls).__new__(cls)
            cls._instance._session = cls._create_session()
        return cls._instance

    @property
    def session(self):
        """
        Returns the database session
        :return: database session
        """
        return self._session

    @staticmethod
    def _create_session():
        """
        Creates a duckdb instance
        :return: DuckDB session
        """
        con = duckdb.connect(":memory:")
        sql='''
CREATE TABLE base_type
  (
    type_id          varchar        NOT NULL,
    type_name        varchar NOT NULL,
    sql_type         varchar NOT NULL)
        '''
        con.sql(sql)
        sql='''
CREATE TABLE other
  (
    other_id          varchar        NOT NULL,
    other_name        varchar NOT NULL,
    type_id         varchar NOT NULL)
        '''
        con.sql(sql)
        return con


