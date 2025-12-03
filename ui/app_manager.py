import streamlit as st
from modules import Day_1, Day_2, Day_3, Day_4, Day_5, Day_6, Day_7, Day_8, Day_9, Day_10, Day_11, Day_12, Day_13, Day_14, Day_15, Day_16, Day_17, Day_18, Day_19, Day_20, Day_21, Day_22, Day_23, Day_24, Day_25
from time import time
import os
import inspect

DAY_MODULES = {"1": Day_1, "2": Day_2, "3": Day_3,
               "4": Day_4, "5": Day_5, "6": Day_6,
               "7": Day_7, "8": Day_8, "9": Day_9,
               "10": Day_10, "11": Day_11, "12": Day_12,
               "13": Day_13, "14": Day_14, "15": Day_15,
               "16": Day_16, "17": Day_17, "18": Day_18,
               "19": Day_19, "20": Day_20, "21": Day_21,
               "22": Day_22, "23": Day_23, "24": Day_24,
               "25": Day_25}

def show_day_ui(file_name, day_module)->None:
    # Recover the title
    file_name = " ".join(file_name.split("_")[1:])[:-3]
    st.title(f"{file_name}")
 # Create tabs for "Solver" and "Code"
    tab1, tab2 = st.tabs(["🧩 Solver", "📜 Code Viewer"])

    # Solver Tab
    with tab1:
        st.subheader("Provide your input data")
        input_method = st.radio(
            "Select a method for provding your data:",
            ("Upload a text file", "Paste your input in the text box")
        )

        # Initialize input_data variable
        input_data = None

        if input_method == "Upload a text file":
            # File uploader for input data
            uploaded_file = st.file_uploader("", type=["txt", "csv"])
            if uploaded_file is not None:
                # Read the uploaded file content
                input_data = uploaded_file.read().decode("utf-8")

        elif input_method == "Paste your input in the text box":
            # Text area for pasting input data
            input_data = st.text_area(
                "", placeholder="Enter your input data...")

        # Button to run the puzzle solution
        if input_data and st.button(f"Run code"):
            with st.spinner("Running your puzzle solution..."):
                try:
                    start = time()
                    sol = day_module.main(input_data)
                    elapsed_time = int((time() - start) * 1000)
                    st.success(f"""
                               **⭐ {sol[0]}**\n
                               **⭐⭐ {sol[1]}**\n
                               **⌛ {elapsed_time} ms**\n
                                """,)
                except Exception as e:
                    st.error(f"An error occurred: {e}")

    # View Code Tab
    with tab2:
        try:
            # Display the content of the corresponding Python module
            # Get the relative path of the day_module
            day_module_path = os.path.relpath(inspect.getfile(day_module), os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
            with open(day_module_path, "r") as f:
                code = f.read()
            st.code(code, language="python")
        except FileNotFoundError:
            st.error(f"Code not available.")