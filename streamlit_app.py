import streamlit as st
import datetime
import pandas as pd
import time

def main():
    st.set_page_config(page_title="Dukioo", page_icon=":flower_playing_cards:")
    schedule()

def schedule():
    # Replacing option_menu with a selectbox for the sidebar menu
    choice = st.sidebar.selectbox("Main Menu", ["Study Schedule", "Contact"])

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

        # Logic for session creation, table, and other UI elements...

    elif choice == "Contact":
        contact()

def contact():
    col1, col2 = st.columns([5, 12], gap=("large"))
    with col1:
        with st.container():
            st.title("Contact Form :love_letter:")
            st.subheader("Hi! I am the creator of this website")

            st.write("""
                Please let me know if there are any issues with the website or send in suggestions!

                -- Dukioo Creator
            """)
    with col2:
        with st.container():
            st.markdown('###')
            st.write("-------")
            st.subheader("Contact Form here")
            contact_form = """
            <form action="236a7896f7347678e83045cee735f0a9" method="POST">
                <input type="hidden" name="_captcha" value="false">
                <input type="text" name="name" placeholder="Your name" required>
                <input type="email" name="email" placeholder="Your email" required>
                <textarea name="message" placeholder="Your message here"></textarea>
                <button type="submit">Send</button>
            </form>
            """

            st.markdown(contact_form, unsafe_allow_html=True)

            # Use Local CSS File
            def local_css(file_name):
                with open(file_name) as f:
                    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

            local_css("style/style.css")

if __name__ == '__main__':
    main()
