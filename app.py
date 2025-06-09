
import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Birthday App", layout="wide")

# Embed custom font
st.markdown("""
    <style>
    @font-face {
        font-family: 'EduNSWACT';
        src: url('assets/EduNSWACTFoundation-Regular.ttf') format('truetype');
    }
    html, body, [class*="css"]  {
        font-family: 'EduNSWACT', cursive;
        background-color: #ffe6f0;
    }
    .centered {
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Session state
if "page" not in st.session_state:
    st.session_state.page = 1

# Page navigation
def next_page():
    st.session_state.page += 1

# Music
def play_music(filename):
    audio_file = open(f"assets/{filename}", "rb")
    st.audio(audio_file.read(), format="audio/mp3")

# Pages
if st.session_state.page == 1:
    st.markdown('<div class="centered"><h1>🌹 Happieee birthdayyy Samiya 🌹</h1><h2>🎀💗my best friend🙃😉 and my fav person!!😊😏</h2></div>', unsafe_allow_html=True)
    play_music("music1.mp3")
    if st.button("🌹 Start"):
        next_page()

elif st.session_state.page == 2:
    st.markdown('<div class="centered"><h2>Thanku for being my bestfriend for so long and staying with me always* ;). I hope we stay together always, despite all the misunderstanding and fights, u will still be my favourite alwayss samiya!!🥀🥀</h2><p>We had good times and bad times, but still i love our friendship, we may no longer be classmates, we may not have met in a very long time, but u will always b close to me :) Happyyy bdayyy pgllll!!!!🎀🥂🥳🎉🎋🎊🎂🎈🎗🎆</p></div>', unsafe_allow_html=True)
    play_music("music2.mp3")
    if st.button("🐱 Next"):
        next_page()

elif st.session_state.page == 3:
    st.markdown('<div class="centered"><h2>donno until when we r together... but i would love to be here always. But whatever be the destiny, i would still never want to loose you. Hope everything will be fine and we never break our friendship samiya :)</h2></div>', unsafe_allow_html=True)
    play_music("music3.mp3")
    if st.button("🐱🐸 Continue"):
        next_page()

elif st.session_state.page == 4:
    st.image("assets/image1.jpg", caption="🥰😉")
    play_music("music4.mp3")
    if st.button("💐 Open Next"):
        next_page()

elif st.session_state.page == 5:
    st.markdown('<div class="centered"><h2>🎉 Once again wish you a very happy 20th birthdayy pgllll!! 🎊🌹🎀💗🎉🥂🎆🎉🎂😽</h2></div>', unsafe_allow_html=True)
    play_music("music5.mp3")
    if st.button("⭐ Last Page"):
        next_page()

elif st.session_state.page == 6:
    st.image("assets/image2.jpg")
    st.markdown('<div class="centered"><h2>once again happiee bday....nd u will always remain my Billi 😂😽</h2></div>', unsafe_allow_html=True)
    play_music("music6.mp3")
