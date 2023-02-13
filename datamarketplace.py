import streamlit as st
# from PIL import Image
# image = Image.open('sunrise.jpg')
#
# st.image(image, caption='Sunrise by the mountains')import streamlit.components.v1 as components
import streamlit.components.v1 as components


#col1, col2, col3 = st.columns(3)
col1, col2,col3 = st.columns(3)
cols = st.columns(3)
for i, col in enumerate(cols):
    form = "f"+str(i)

    with st.form(key=form):
        cols = st.columns(5)
        for i, col in enumerate(cols):
            col.selectbox(f'Make a Selection', ['click', 'or click'], key=i)
        submitted = st.form_submit_button('Submit')
        # text = "This is a classic Titanic dataset extended with the " \
        #    "features from the Titanic passenger list on Wikipedia available as of February 2019."
        # st.text_area("Titanic dataset",text,height=200,disabled=True,key=i)
        # st.form_submit_button("View")

# with col1:
#     with st.form('Form1'):
#         st.selectbox('Select flavor', ['Vanilla', 'Chocolate'], key=1)
#         st.slider(label='Select intensity', min_value=0, max_value=100, key=4)
#         submitted1 = st.form_submit_button('Submit 1')
#
# with col2:
#     with st.form('Form2'):
#         #components.html(f"""<div style='font-size:15px'><b><u>Titanic Dataset</u></b></div>""")
#         text="This is a classic Titanic dataset extended with the " \
#              "features from the Titanic passenger list on Wikipedia available as of February 2019."
#         st.text_area("Titanic dataset",text,height=200,disabled=True)
#         submitted2 = st.form_submit_button('Submit 2')
#
# with col3:
#     with st.form('Form3'):
#         st.selectbox('Select Topping', ['Almonds', 'Sprinkles'], key=2)
#         st.slider(label='Select Intensity', min_value=0, max_value=100, key=3)
#         submitted3 = st.form_submit_button('Submit 2')
