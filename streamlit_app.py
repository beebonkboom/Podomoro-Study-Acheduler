# streamlit run app.py

import streamlit as st
import datetime
from streamlit_option_menu import option_menu
import pandas as pd
import time

import requests

def main ():
    st.set_page_config(page_title = "Podomi", page_icon=":flower_playing_cards:")
    schedule()

    
def schedule():

   with st.sidebar:
    choice = option_menu( menu_title = "Main Menu",options = ["Study Schedule"] )
    # choice = option_menu( menu_title = "Main Menu",options = ["Study Schedule", "Contact"] )
   if choice == "Study Schedule":
        st.title("Podomoro Study Schedule")

        col1, col2= st.columns ([3,12], gap=("small"))
        with col1:
            with st.form(key='myform'):
                now_now = datetime.datetime(2023, 1,1,12,0,0,0)
                s_time = st.time_input("Start time:",datetime.time(now_now.hour, 0))
                start_time = datetime.datetime(now_now.year, now_now.month, now_now.day, s_time.hour, s_time.minute, s_time.second)
                break_time  = st.number_input("Break length (mins):",  min_value = 5, max_value = 15, value = 10, step = 5)
                length = st.number_input("Length of sessions (mins):",  min_value = 20, max_value = 60, value = 25, step = 5)
                sessions = st.number_input("Number of studying:",  min_value = 1, max_value = 12, value = 1,
                step = 1)
                submit_button = st.form_submit_button(label = 'Enter')

                with col2:
                    list_i = []
                    list_t = []
                    list_b = []
                    for i in range (1, sessions + 2):
                        if i == 1:
                            new_time = start_time
                            b_time = datetime.timedelta(minutes = length)
                            b_time = b_time + start_time
                            t = new_time.strftime("%I:%M %p")
                            b = b_time.strftime("%I:%M %p")
                            # t = new_time.time() # for 24 hr clock display instead
                            # b = b_time.time()
                        else:
                            new_time = datetime.timedelta(minutes = length*(i-1) + break_time*(i-1))
                            new_time = start_time + new_time
                            b_time = datetime.timedelta(minutes = length)
                            b_time = b_time + new_time
                            t = new_time.strftime("%I:%M %p")
                            b = b_time.strftime("%I:%M %p")
                            # t = new_time.time()
                            # b = b_time.time()



                        list_i.append(i)
                        list_t.append(t)
                        list_b.append(b)
                    
                    last = list_t.pop() 
                    list_b.pop()
                    table(list_t, list_b, sessions,last)
                    st.markdown('###')
                    st.markdown('###')
                    st.write("-------")
                    video()
                    
            
            timer(break_time, length)
            st.markdown('###')
            st.markdown('###')
            st.markdown('###')
            st.markdown('###')
            st.markdown('###')
            st.write("-------")
            st.markdown("""
            <style>
            .big-font {
                font-size:11px !important;
            }
            </style>
            """, unsafe_allow_html=True)

            st.markdown('<p class="big-font">P.S - if schedule or video content is changed, timer resets!</p>', unsafe_allow_html=True)
            
#    elif choice == "Contact":
#         contact()
    




def table(t, b, sess, last):
    t2 = []
    b2 = []
    d = ''
    for j in range (len(t)):
        p1 = t[j]
        d = str(str(p1) + " - " + str(b[j]))
        t2.append(d)
    for j in range (len(b)):
        if j < len(b) -1:
            p1 = b[j]
            d = str(str(p1) + " - " + str(t[j+1]))
            b2.append(d)
        else:
            p1 = b[j]
            d = str(str(p1) + " - " + str(last))
            b2.append(d)
    df = pd.DataFrame(
    data = [t2,b2], index=['Study ', 'Break '],
    columns= ('Session %d' % i for i in range(1,sess+1)))
    st.dataframe(df)


def timer(breaks, lengths):
    st.subheader("Timer")
    option = st. selectbox('', ('Study', 'Break', 'Enter specific time'), label_visibility="collapsed")
    if option == 'Study':
        secs = lengths *60
    elif option == 'Break':
        secs = breaks *60
    else:
        secs = st.number_input("Set Timer (mins):",  min_value = 0, max_value = 60, value = 0)
        secs = secs * 60
    start = st.button('Start', key = 1)
    stop = st.button('Stop/Clear', key= 2)

    if start:
        if stop:
            count_down(0)
        else:
            count_down(secs)



def count_down(duration):
    if duration != 0 :
        placeholder = st.empty()
        dur = int(duration)
        bar = st.progress(100)
        with placeholder:
            while duration:
                bar.progress( round ((int(duration)/dur)*100) )


                mins, secs = divmod(duration,60)
                time_now = '{:02d}:{:02d}'.format(mins,secs)
                st.header(time_now)
                time.sleep(1)
                duration -= 1

        for k in range (3):
            html_string = """
                    <audio autoplay>
                    <source src="https://www.orangefreesounds.com/wp-content/uploads/2022/04/Small-bell-ringing-short-sound-effect.mp3" type="audio/mp3">
                    </audio>
                    """

            sound = st.empty()
            sound.markdown(html_string, unsafe_allow_html=True)
            time.sleep(2)
            sound.empty()
        st.write("Times up!!")

def video ():
    option = st.selectbox(
        'Please select study music or enter your own youtube video!',
        ('Lofi radio', 'Coffee shop jazz', 'Gentle rain', 'Brown noise', 'Enter own YT link')
    )
    if option == 'Lofi radio':
        st.video("https://www.youtube.com/watch?v=jfKfPfyJRdk&ab_channel=LofiGirl")
    elif option == 'Coffee shop jazz':
        st.video("https://www.youtube.com/watch?v=MYPVQccHhAQ&ab_channel=RelaxingJazzPiano")
    elif option == 'Gentle rain':
        st.video ("https://www.youtube.com/watch?v=q76bMs-NwRk&t=2521s&ab_channel=TheRelaxedGuy")
    elif option == 'Brown noise':
        st.video("https://www.youtube.com/watch?v=Q6MemVxEquE&t=25074s&ab_channel=crysknife007")
    elif option == 'Enter own YT link': 
        yt_link = st.text_input('Link')
        if st.button('Enter', key = 3):
            try:
                st.video(yt_link)
            except:
                st.write("ERROR! LINK NOT FOUND!")
    else:
        st.video("https://www.youtube.com/watch?v=jfKfPfyJRdk&ab_channel=LofiGirl")
            


# def contact():
#     col1, col2 = st.columns([5, 12], gap="large")

#     with col1:
#         with st.container():
#             st.title("Contact Form 💌")
#             st.subheader("Hi! I am the creator of this website")

#             st.write(
#                 """
#                 Please let me know if there are any issues with the website or send in suggestions!
                
#                 -- Dukioo Creator
#                 """
#             )

#     with col2:
#         with st.container():
#             st.markdown("###")
#             st.write("-------")
#             st.subheader("Contact Form here")

#             with st.form("contact_form"):
#                 name = st.text_input("Your Name")
#                 email = st.text_input("Your Email")
#                 message = st.text_area("Your Message")

#                 submitted = st.form_submit_button("Send")

#                 if submitted:
#                     if name and email and message:
#                         response = requests.post(
#                             "http://127.0.0.1:5000/submit",  # Update when deployed
#                             json={"name": name, "email": email, "message": message},
#                         )

#                         if response.status_code == 200:
#                             st.success("Message sent successfully!")
#                         else:
#                             st.error("Error sending message. Please try again.")
#                     else:
#                         st.error("All fields are required!")

#             # Use Local CSS File
#             def local_css(file_name):
#                 with open(file_name) as f:
#                     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
#             local_css("style/style.css")




if __name__ == '__main__':
    main ()
