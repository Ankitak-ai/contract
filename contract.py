import streamlit as st
from fpdf import FPDF
from datetime import datetime

# App Title
st.title("📄 HyperChat Streamer Contract")

# Streamer Input Form
st.header("🎮 Streamer Information")
streamer_name = st.text_input("Full Name")
streamer_email = st.text_input("Email or Channel Handle")
split_x = st.number_input("Streamer Revenue Share (%)", min_value=0, max_value=100, value=80)
split_y = 100 - split_x

agreed = st.checkbox("I agree to the terms and conditions below")

# Display contract preview
st.header("📜 Contract Preview")
agreement_date = datetime.now().strftime("%Y-%m-%d")

if streamer_name and streamer_email:
    st.markdown(f"""
    **This Agreement** is made on **{agreement_date}** between:

    **HyperChat Technologies Pvt. Ltd.**, a registered MSME under Udyam Registration No. **UP29D0047796**, with its principal office at **Ghaziabad**,  
    and  
    **{streamer_name}**, identified by email/channel: **{streamer_email}**.

    ---  

    ### Terms & Conditions

    1. **Purpose**  
       HyperChat provides a fan engagement and donation tool for live streamers.

    2. **Access Rights**  
       The Streamer is granted a non-transferable license to use HyperChat during live streams.

    3. **Responsibilities**  
       The Streamer agrees to use HyperChat responsibly and maintain a positive environment.

    4. **Revenue Split**  
       - {split_x}% to the Streamer  
       - {split_y}% to HyperChat (as platform fee)

    5. **Intellectual Property**  
       HyperChat retains rights to its platform and branding. Streamer owns their content.

    6. **Termination**  
       This agreement may be ended by either party with 7 days’ notice.

    7. **Confidentiality**  
       The Streamer will not disclose private information about HyperChat.

    8. **Governing Law**  
       This Agreement is governed by the laws of India.

    ---

    **Signed by:**  
    _Ankit Kumar_, Founder, HyperChat Technologies Pvt. Ltd.  
    **Streamer:** {streamer_name}
    """)

# Generate PDF if agreed
if agreed and st.button("Generate & Download PDF"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    contract = f"""
HyperChat Streamer Agreement

This Agreement is made on {agreement_date} between:

HyperChat Technologies Pvt. Ltd., Udyam Registration No. UP29D0047796,
with its principal office at Ghaziabad,
and
{streamer_name}, identified by {streamer_email}.

1. PURPOSE
HyperChat provides a fan engagement and donation tool for live streamers.

2. GRANT OF ACCESS
Streamer is licensed to use HyperChat’s services during live streams.

3. RESPONSIBILITIES
Streamer agrees to maintain a respectful environment and use HyperChat responsibly.

4. REVENUE SHARING
- {split_x}% to the Streamer
- {split_y}% to HyperChat as platform fee

5. INTELLECTUAL PROPERTY
HyperChat retains all rights to its platform. Streamers retain rights to their content.

6. TERM & TERMINATION
Either party may terminate this agreement with 7 days' notice.

7. CONFIDENTIALITY
Streamer agrees not to disclose confidential information.

8. GOVERNING LAW
This Agreement is governed by the laws of India.

Signed by:
Ankit Kumar, Founder, HyperChat Technologies Pvt. Ltd.
Streamer: {streamer_name}
Date: {agreement_date}
"""

    for line in contract.split("\n"):
        pdf.multi_cell(0, 10, line.strip())

    pdf_file = f"{streamer_name.replace(' ', '_')}_HyperChat_Contract.pdf"
    pdf.output(pdf_file)

    with open(pdf_file, "rb") as f:
        st.download_button("📥 Download Signed PDF", f, file_name=pdf_file)

