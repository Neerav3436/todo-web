import streamlit as sl
from modules.functions import get_todos, write_todos


# sl.set_page_config(layout="wide")

sl.title("This is To-Do App")
sl.subheader("This is to make yourself more productive" )
sl.write("Following are your <b>To-Do's</b>", unsafe_allow_html=True) # false default

todos = get_todos()

def add_todo():
    if len(sl.session_state['new_todo']) > 0:
        todos.append("\n" + sl.session_state['new_todo'])
        write_todos(todos)

sl.text_input(label='Enter your new To-Do',
    placeholder='here goes new Todo..',
    key='new_todo', on_change=add_todo) # order matters for semantic stucture

for index, todo in enumerate(todos):
    todo_check_box = sl.checkbox(f"{index+1}. {todo}", key=f"{index+1}. {todo}")
    if todo_check_box:
        to_be_removed_index = index
        todos.pop(index)
        write_todos(todos)
        sl.rerun()


# sl.text_input(label='Enter your new To-Do',
#                placeholder='here goes new Todo..',
#                key='new_todo', on_change=add_todo)


sl.write(sl.session_state)