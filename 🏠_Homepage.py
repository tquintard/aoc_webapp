import streamlit as st
from PIL import Image


# Internet Browser tab name
st.set_page_config(page_title="Advent of Code Solver",
                   page_icon="🎄", layout="wide")

# Main title of the app
st.title("🎄Advent of Code 2025 Solver🎄")

# Homepage section
# Display an image on the homepage
img = Image.open("resources/pictures/aoc24.png")
st.image(img, use_container_width=False, width=800)
st.write("This web app aims to share my Python code I used to solve AoC puzzles.")
st.write(
    "You can drop your inputs and run my code to check whether your solution is correct.")
st.write("Select a puzzle from the menu to begin.")

