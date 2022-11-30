import streamlit as st
import pandas as pd
import numpy as np

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')


options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])

st.write('You selected:', options)

@st.cache(allow_output_mutation=True)
def get_data():
    return []

user_id = st.text_input("User ID")
foo = st.slider("foo", 0, 100)
bar = st.slider("bar", 0, 100)

if st.button("Add row"):
    get_data().append({"UserID": user_id, "foo": foo, "bar": bar})

st.write(pd.DataFrame(get_data()))
