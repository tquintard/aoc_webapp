import streamlit as st
from time import time
import os
import inspect
from config import DAYS, COMMUN_MODULES

def set_page_settings(title, icon) -> None:
    """
    Apply Streamlit UI configuration and render the animated sidebar title.

    The function sets the page configuration (title, icon, layout) and
    injects a custom animated title in the sidebar.
    """
    st.set_page_config(
        page_title=title,
        page_icon=icon,
        layout="wide",
    )
    st.title(icon + title)


import streamlit as st

def show_day_ui(title: str, day_module) -> None:
    # Tabs
    if day_module == COMMUN_MODULES:
        st.write("📜Code")
        show_code(day_module)
    else:
        tab1, tab2 = st.tabs(["🧩Solver", "📜Code"])

        # Solver Tab
        with tab1:
            cols = st.columns([0.3, 0.7])

            # Text area + Reset button
            with cols[0]:
                #st.subheader("Inputs", help="Paste your input in the text box")

                # Unique keys for session state
                unique_page_key = f"input_data_{title.replace(' ', '_')}"
                
                # Initialize session state if not exists
                input_data = st.session_state.get(unique_page_key, "")

                subcols = st.columns([0.1, 0.1, 0.7, 0.1])
                with subcols[0]:
                    if st.button(label="", 
                                icon="🧪", 
                                type="tertiary",
                                help="Load sample inputs",
                                key= unique_page_key + "_sample",
                                ):
                        st.session_state[unique_page_key] = day_module.sample()
                        st.rerun()
                if input_data:

                    # Run button
                    with subcols[1]:
                        if st.button(label="", 
                                     icon="🚀",
                                     type="tertiary",
                                     help="Run your puzzle solution",
                                     key= unique_page_key + "_run",
                                     ):
                            with cols[1]:
                                run_code(input_data, day_module)

                    # Reset button
                    with subcols[3]:
                        if st.button(label="", 
                                    icon="🔄", 
                                    type="tertiary",
                                    help="Reset your inputs",
                                    key= unique_page_key + "_reset",
                                    ):
                            st.session_state[unique_page_key] = ""
                            st.rerun()
                # Text area
                input_data = st.text_area(
                    label="Paste your input in the text box",
                    placeholder="Paste your input data here",
                    value=st.session_state.get(unique_page_key, ""),
                    height=500,
                    label_visibility="collapsed",
                    key=unique_page_key
                )


        # Code Tab
        with tab2:
            show_code(day_module)



def run_code(input_data, day_module):
    with st.spinner("Running your puzzle solution..."):
        try:
            start = time()
            sol = day_module.main(input_data)
            elapsed_time = int((time() - start) * 1000)
            st.subheader("Results")
            st.success(f"""
                        **⭐ {sol[0]}**\n
                        **⭐⭐ {sol[1]}**\n
                        **⌛ {elapsed_time} ms**\n
                        """,)
        except Exception as e:
            st.error(f"An error occurred: {e}")

def init_day_page(selected_day:str, module_day):
    full_title = selected_day.split(" - ")[1]
    title = " ".join(full_title.split()[1:])
    icon = full_title.split()[0]
    set_page_settings(title=title, icon=icon)
    show_day_ui(title=title, day_module=module_day)

def select_day(year):
    # Display the content of the corresponding Python module
    selected_day = st.sidebar.selectbox("Pick a day", options=DAYS[year].keys())
    return selected_day, DAYS[year][selected_day]

def show_code(day_module):
    try:
        # Display the content of the corresponding Python module
        # Get the relative path of the day_module
        day_module_path = os.path.relpath(inspect.getfile(day_module), os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
        with open(day_module_path, "r") as f:
            code = f.read()
        st.code(code, language="python")
    except FileNotFoundError:
        st.error(f"Code not available.")    