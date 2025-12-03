"""
CSS and title animation helpers for the Streamlit sidebar.

This module defines the animated application title displayed in the
sidebar using custom CSS injected through `st.sidebar.markdown`.
"""

import streamlit as st
from typing import Dict
from pathlib import Path

def animate_title(title, icon) -> None:
    """
    Render the animated application title in the sidebar.

    The function injects CSS defining a keyframe animation and applies
    it to an icon next to the application name in the sidebar. It must
    be called once during the Streamlit app initialization to display
    the animated title.

    Returns:
        None: This function performs UI rendering only.
    """
    # Inject custom CSS for the moving icon animation and title layout
    st.sidebar.markdown(
        """
        <style>

            ._icon {
                display: inline-block;
                font-size: 1.4em;
                margin-right: 0px;
                margin-left: 0px;
            }
            
            .title-container {
                display: flex;
                align-items: left;
            }
            
            .main-title {
                font-size: 1.7rem;
                font-weight: bold;
                margin-left: 5px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Render the animated icon and application name in the sidebar
    st.markdown(
        f"""
        <div class="title-container">
            <div class="_icon">{icon}</div>
            <span class="main-title">{title}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
