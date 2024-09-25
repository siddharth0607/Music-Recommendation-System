import streamlit as st
import time
import pandas as pd
import numpy as np

st.title("Course")
st.header("Machine Learning")
st.subheader("Linear Regression")
st.subheader("Logistic Regression")
st.info("Practicing basic functions of streamlit")
st.warning("Mind the syntax!")
st.write("Just writing something")
st.write(range(50))
st.error("ValueError")
st.success("Its a win!")
st.markdown("# Deep Learning")
st.markdown("## Deep Learning")
st.markdown("### Deep Learning")
st.markdown("*Deep Learning*")
st.markdown("- Apple")
st.markdown("- Banana")
st.markdown("- Chickoo") 
st.markdown(":fire:")
st.text("Neural Network")
st.caption("This is a caption")
st.latex('''ax^2+bx+c''')
st.image(r"C:\Users\SIDDHARTH\Pictures\PMP_6983lr.jpg")
st.checkbox("Login")
st.button("Click")
st.radio("Pick your gender: ",['Male','Female'])
st.selectbox("Pick your course: ",['ML','RDBMS','CSA'])
st.multiselect("Supervised ML algorithms: ",['Linear Regression','KNN','K-Means'])
st.select_slider("Rating: ",['Bad','Average','Good'])
st.slider("Pick your number: ",0,15)
st.number_input("Choose a number: ",0,100)
st.text_input("Enter your name: ")
st.date_input("Enter a date: ")
st.time_input("What's the time: ")
st.text_area("Tell us something about yourself: ")
st.file_uploader("Upload your file-")
st.color_picker("Select your favourite color: ")
st.progress(90)

with st.spinner("Just Wait"):
    time.sleep(0)

# st.balloons()

st.sidebar.title("Whatsapp")
st.sidebar.text_input("Mail address: ")
st.sidebar.text_input("Password: ")
st.sidebar.button("Enter")

df = pd.DataFrame(np.random.rand(50,2),columns=['x','y'])
st.title("Bar Chart")
st.bar_chart(df)
st.title("Line Chart")
st.line_chart(df)
st.title("Area Chart")
st.area_chart(df)