import streamlit as st
import sqlite3
import pandas as pd

DB_PATH = "/mnt/data/ebf4f7c8-b7b4-4393-84f9-d69bfd9a5dd1.db"

st.title("📊 SQLite Database Viewer & Query Runner")
st.write("Connected to database:")
st.code(DB_PATH)

# ---------- DB CONNECTION ----------
@st.cache_resource
def get_connection():
    return sqlite3.connect(DB_PATH)

conn = get_connection()

# ---------- SHOW TABLES ----------
st.subheader("📁 Available Tables")

tables = pd.read_sql_query(
    "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;",
    conn
)

if len(tables) == 0:
    st.warning("No tables found in the database!")
else:
    st.dataframe(tables)

    table_name = st.selectbox("Select a table to view", tables["name"])

    if table_name:
        st.subheader(f"📌 Table: {table_name}")
        df = pd.read_sql_query(f"SELECT * FROM {table_name} LIMIT 300;", conn)
        st.dataframe(df, use_container_width=True)
        st.caption(f"Total Rows Loaded: {len(df)}")


# ---------- RUN CUSTOM SQL QUERY ----------
st.subheader("📝 Run Custom SQL Query")

default_query = "SELECT name FROM sqlite_master WHERE type='table';"
query = st.text_area("Write SQL Query", default_query, height=120)

if st.button("Run Query"):
    try:
        result = pd.read_sql_query(query, conn)
        st.success("Query executed successfully ✔️")
        st.dataframe(result, use_container_width=True)
        st.caption(f"Rows Returned: {len(result)}")
    except Exception as e:
        st.error(f"Error: {e}")
