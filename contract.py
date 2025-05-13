import streamlit as st
from fpdf import FPDF
from datetime import datetime

st.title("HyperChat Streamer Contract")

name = st.text_input("Full Name")
email = st.text_input("Email or Channel Handle")
split_x = st.number_input("Streamer %", min_value=0, max_value=100)
split_y = 100 - split_x

if st.checkbox("I agree to the terms and conditions"):
    if st.button("Generate Contract"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        contract = f"""
        This Agreement is between HyperChat and {name} ({email}).

        Revenue split:
        - {split_x}% to the Streamer
        - {split_y}% to HyperChat

        Agreed on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        """
        for line in contract.split('\n'):
            pdf.multi_cell(0, 10, line)
        pdf_path = f"contract_{name.replace(' ', '_')}.pdf"
        pdf.output(pdf_path)
        with open(pdf_path, "rb") as file:
            st.download_button("Download Signed Contract", file, file_name=pdf_path)
