from modules._2024 import Day_24_1, Day_24_2, Day_24_3, Day_24_4, Day_24_5, Day_24_6, Day_24_7, Day_24_8, Day_24_9, Day_24_10, Day_24_11
from modules._2025 import Day_25_1, Day_25_2, Day_25_3
import modules.common as common
from pathlib import Path


def get_markdown_files():

    markdown_dict: dict[str, Path] = {}

    # Recursive scan of markdown files
    for file_path in Path(MD_DIR).rglob("*.md"):
        key = file_path.stem
        markdown_dict[key] = file_path.resolve()
    return markdown_dict


COMMUN_MODULES = common

# Default output directory and file configuration
MD_DIR: str = "assets/markdown"
MKD_FILES: dict[str, Path] = get_markdown_files()

DAYS: dict={
    "2024":{
     "01 - 📍 Historian Hysteria": Day_24_1,
     "02 - ☢️ Red-Nosed Reports": Day_24_2,
     "03 - 👨‍💻 Mull It Over": Day_24_3,
     "04 - 🕵🏻 Ceres Search": Day_24_4,
     "05 - 🖨️ Print Queue": Day_24_5,
     "06 - 💂‍♂️ Guard Gallivant": Day_24_6,
     "07 - 🚧 Bridge Repair": Day_24_7,
     "08 - 📡 Resonant Collinearity": Day_24_8,
     "09 - 💽 Disk Fragmenter": Day_24_9,
     "10 - ⛰️ Hoof It": Day_24_10,
     "11 - 🌑 Plutonian Pebbles": Day_24_11,
    },
    "2025":{
        "01 - 🧱 Secret Entrance": Day_25_1,
        "02 - 🎁 Gift Shop": Day_25_2,
        "03 - 🛎️ Lobby": Day_25_3,
    },
}
