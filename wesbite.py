import streamlit as st
import random

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 



random_github_project = ['https://github.com/nooby124/Nooby-s-calculator', 'https://github.com/nooby124/Your-mother--game-',]
random_github_project_real = random.choice(random_github_project) #the real version is not an imposter


st.title('random one-of-my-github-projects generator')


if st.button('generate'):
    st.write(str(random_github_project))
else:
    st.write('---')


