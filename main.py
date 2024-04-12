import streamlit as st
import keyboard
import subprocess
import os
import psutil
import time

st.set_page_config(page_title="ONLINE FILE MANAGER",
                   page_icon=":file_folder:",
                   layout="centered")
st.title(':blue[FILE MANAGER]')
st.subheader('Select The Task', divider='rainbow')
option = st.selectbox('', ('None', 'List Files', 'Create Directory', 'Delete File', 'Rename File/Directory',
                           'Copy File/Directory', 'Move File/Directory', 'Go to Directory', 'Exit'),
                      placeholder="Choose an option",)
st.write('You selected:', option)

choice = None
source = None
destination = None

if option == 'None':
    pass
elif option in ('List Files', 'Create Directory', 'Delete File', 'Rename File/Directory', 'Go to Directory'):
    st.subheader('Enter The source Path', divider='rainbow')

    if option == 'List Files':
        choice = "1"
    elif option == 'Create Directory':
        choice = "2"
    elif option == 'Delete File':
        choice = "3"
    elif option == 'Rename File/Directory':
        choice = "4"
    elif option == 'Go to Directory':
        choice = "7"

    source = st.text_input("", placeholder="enter the source",)
    if st.button('Enter'):
        with open("choice.txt", 'w') as txt_file:
            txt_file.write(choice)
        with open("source.txt", 'w') as txt_file:
            txt_file.write(f"{source}")
        subprocess.call('powershell.exe -ExecutionPolicy RemoteSigned -File file.ps1', shell=True)


elif option in ('Copy File/Directory', 'Move File/Directory'):
    st.subheader('Enter The source Path', divider='rainbow')

    if option == 'Copy File/Directory':
        choice = "5"
    elif option == 'Move File/Directory':
        choice = "6"

    source = st.text_input("", placeholder="enter the source",)
    st.subheader('Enter The destination Path', divider='rainbow')
    destination = st.text_input("", placeholder="enter the destination",)

    if st.button('Enter'):
        with open("choice.txt", 'w') as txt_file:
            txt_file.write(choice)
        with open("source.txt", 'w') as txt_file:
            txt_file.write(f"{source}")
        with open("destination.txt", 'w') as txt_file:
            txt_file.write(f"{destination}")
        subprocess.call('powershell.exe -ExecutionPolicy RemoteSigned -File file.ps1', shell=True)


elif option == 'Exit':
    choice = "8"
    exit_app = st.button("Enter")
    if exit_app:
        time.sleep(1)
        keyboard.press_and_release('ctrl+w')
        pid = os.getpid()
        p = psutil.Process(pid)
        p.terminate()