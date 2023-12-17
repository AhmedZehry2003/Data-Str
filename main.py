import streamlit as st

import json

with open("data/stack.json", "r") as file:
    stack = json.load(file)


push_input_container, push_btn_container = st.columns(2)

with push_input_container:
    push_input = st.number_input("Enter a number:", value=0)

with push_btn_container:
    push_btn = st.button("push")

if push_btn and push_input != "":
    stack.insert(0, push_input)

pop_container, is_empty_btn_container = st.columns(2)

with pop_container:
    dequeue_btn = st.button("pop")

with is_empty_btn_container:
    is_empty_btn = st.button("Is empty")

if dequeue_btn:
    stack.pop(0)

st.write(stack)

if is_empty_btn:
    st.write(f"The stack is {'not empty' if stack else 'empty'}")


with open("data/stack.json", "w") as file:
    json.dump(stack, file)
