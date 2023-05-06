import streamlit as st
from function import readfile, writefile
list2 = readfile()


def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    list2.append(new_todo)
    writefile(list2)


st.title('To-do List')
st.subheader('write what you are going to do today')
for index,list in enumerate(list2):
    checkbox = st.checkbox(list,key=list)
    if checkbox:
        list2.pop(index)
        writefile(list2)
        del st.session_state[list]
        st.experimental_rerun()


st.text_input(label="Write your plans for today",placeholder="Start with an interesting One",
              on_change=add_todo,key="new_todo")


