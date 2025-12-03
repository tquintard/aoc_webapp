import streamlit as st

st.title("📚Common Modules")
st.write("Find here the common modules used in the puzzles.")
# Display the content of the corresponding Python module
with open(f"modules/common/__init__.py", "r") as f:
    code = f.read()
st.code(code, language="python")