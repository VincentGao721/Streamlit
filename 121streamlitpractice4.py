import streamlit as st 
import pandas as pd 
# st.selectbox
st.header('st.selectbox')

option = st.selectbox(
    'What is your favorite color?',
    ('Blue', 'Red', 'Green')
)

st.write('Your favorite color is ', option)

# st.multiselect 
st.subheader('st.multiselect')

options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red']
)

st.write("You selected:", options)

# st.checkbox 

st.subheader('st.checkbox')
st.write('What would you like to order?')

icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if icecream:
    st.write("Great! Here's some mroe 🍦")

if coffee:
    st.write("Okay! Here's some mroe ☕")

if cola: 
    st.write("Here you go 🥤")

# st.latex
st.subheader('st.latex')

st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} = 
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
''')

st.title('Customizing the theme of Streamlit apps')

st.write('Contents of the `.streamlit/config.toml` file of this app')

st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")

number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:', number)




