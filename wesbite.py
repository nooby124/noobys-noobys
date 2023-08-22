import streamlit as st
import random

def buttonshit():
    if st.button('generate'):
        st.write(str(random_github_project_real))
    else:
        st.write('---')





random_github_project = random_github_project = ['https://github.com/nooby124/Nooby-s-calculator', 'https://github.com/nooby124/Your-mother--game-', 'https://github.com/nooby124/noobys-stuff-2', 'https://github.com/nooby124/noobys-website-for-a-very-specific-purpose', 'https://github.com/nooby124/noobys-fake-nitro-gen', 'https://github.com/nooby124/noobys-noobys', '[https://github.com/noobys-but-off](https://youtu.be/uHgt8giw1LY)']
random_github_project_real = random.choice(random_github_project) #the real version is not an imposter


st.title('random one-of-my-github-projects generator')

if st.button('generate'):
    st.write(str(random_github_project_real))
else:
    st.write('---')