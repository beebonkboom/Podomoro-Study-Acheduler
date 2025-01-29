import streamlit as st
import datetime
import pandas as pd
import time
from streamlit_option_menu import option_menu  # This import should work if the package is installed

def main():
    st.set_page_config(page_title="Dukioo", page_icon=":flower_playing_cards:")
    schedule()

def schedule():
    with st.sidebar:
        choice = option_menu(menu_title="Main Menu", options=["Study Schedule", "Contact"])

    if choice == "Study Schedule":
        st.title("Podomoro Study Schedule")
        col1, col2 = st.columns([3, 12], gap=("small"))
        with col1:
            with st.form(key='myform'):
                now_now = datetime.datetime(2023, 1, 1, 12, 0, 0, 0)
                s_time = st.time_input("Start time:", datetime.time(now_now.hour, 0))
                start_time = datetime.datetime(now_now.year, now_now.month, now_now.day, s_time.hour, s_time.minute, s_time.second)
                break_time = st.number_input("Break length (mins):", min_value=5, max_value=15, value=10, step=5)
                length = st.number_input("Length of sessions (mins):", min_value=20, max_value=60, value=25, step=5)
                sessions = st.number_input("Number of studying:", min_value=1, max_value=12, value=1, step=1)
                submit_button = st.form_submit_button(label='Enter')

        # Logic for session creation, table and other UI elements...
            
    elif choice == "Contact":
        contact()

def contact():
    # Your contact form code
    pass

if __name__ == '__main__':
    main()

