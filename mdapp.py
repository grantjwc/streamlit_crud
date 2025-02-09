"""
Metadata editing app. Hardwired for base tables use to define metadata.
"""

import streamlit as st
from backend.data_operations import get_tables, get_dataset, specific_config
from backend.duckdb_connection import DuckdbConnection
from backend.sql_statements import delete_cols, insert_cols, process_cols, select_cols
from frontend.tables import base_type

st.set_page_config(layout="centered", page_title="Metadata Editor", page_icon="🧮")

sf_conn = DuckdbConnection()

st.title("Metadeta Editor")

# Open tables
base_type("base_type")
base_type("other")


with st.expander("Session State"):
    st.json(st.session_state)
