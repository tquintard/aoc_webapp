import streamlit as st
from PIL import Image
from core.app_manager import set_page_settings
import requests

def test():
    url = "https://adventofcode.com/2025/day/1/input"
    response = requests.get(url)
    if response.status_code == 200:
        st.write(response.text)
    else:
        st.error("error")

# Internet Browser tab name
set_page_settings(title="Advent of Code Solver", icon="🎄")
test()
# Homepage section
# Display an image on the homepage
img = Image.open("resources/pictures/aoc24.png")
st.image(img, width = 800)
st.write("This web app aims to share my Python code I used to solve AoC puzzles.")
st.write(
    "You can drop your inputs and run my code to check whether your solution is correct.")
st.write("Select a puzzle from the menu to begin.")


