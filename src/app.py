import streamlit as st
from utils import get_computer_model

def main():
    st.title("Demystify Environment Variables")
    model = get_computer_model()
    st.write(f"**Computer Model:** {model}")



if __name__ == "__main__":
    main()