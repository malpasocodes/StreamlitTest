import streamlit as st
import pandas as pd

# make a change to the file


def main():
    st.title("Hello World")
    st.write("This is a simple example of a Streamlit app.")

    # Load data
    data = pd.read_csv("data/accessandmobility.csv")
    df = data.head(10)
    st.write(data)
st.write(df)


if __name__ == "__main__":
    main()