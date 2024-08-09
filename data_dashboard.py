import streamlit as st
import pandas as pd


st.title("Data Dashboard")

upload_file = st.file_uploader("Upload a CSV file", type="csv")

if upload_file is not None:
    df = pd.read_csv(upload_file)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_column =  st.selectbox("Select a column to filter by", columns)
    unique_vals = df[selected_column].unique()
    selected_unique = st.selectbox("Select a value", unique_vals)
    filtered_df = df[df[selected_column] == selected_unique]
    st.write(filtered_df)

    st.subheader("Plot Data")
    x_axis = st.selectbox("Select the x-axis column", columns)
    columns.remove(x_axis)
    y_axis = st.selectbox("Select the y-axis column", columns)
    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_axis)[y_axis])
