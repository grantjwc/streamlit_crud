"""
This module contains functions to interact with the database.
"""

from backend.duckdb_connection import DuckdbConnection
import streamlit as st

sf_conn = DuckdbConnection()


def get_dataset(table_name):
    """
    Get a dataset from database
    :param table_name:
    :return: pandas dataframe
    """
    df = sf_conn.session.table(table_name).df()
    df.reset_index(drop=True, inplace=True)
    return df


def get_tables():
    """
    Get a list of tables from DuckDB
    :return: pandas dataframe
    """
    sql = f"SELECT table_name FROM information_schema.tables"
    return sf_conn.session.sql(sql).df()

def specific_config():
    column_config={
        "sql_type": st.column_config.SelectboxColumn(
            "SQL Type",
            help="Pick a type",
            width="medium",
            options=[
                "varchar",
                "int",
                "pid_hash",
            ],
            required=True,
        )
    }
    return column_config

