import streamlit as st
from fpdf import FPDF
from datetime import datetime
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import io

st.set_page_config(page_title="HyperChat Streamer Contract", layout="centered")
st.title("📄 HyperChat Streamer Contract")

# Streamer Info Form
st.header("🎮 Streamer Information")
streamer_name = st.text_input("Full Name")
streamer_email = st.text_input("Email or Channel Handle")
split_x = st.number_input("Streamer Revenue Share (%)", min_value=0, max_value=100, value=80)
split_y = 100 - split_x
agreed = st.checkbox("I agree to the terms and conditions below")

st.header("✍️ Signature")
st.write("Draw your signature below:")

# Signature pad
canvas_result = st_canvas(
    fill_color="rgba(0, 0, 0, 0)",
    stroke_width=2,
    stroke_color="#000000",
    background_color="#FFFFFF",
    height=150,
    drawing_mode="freedraw",
    key="signature",
)

# Capture current date
agreement_date = datetime.now().strftime("%Y-%m-%d")

# Contract Preview
if streamer_name and streamer_email:
    st.header("📜 Contract Preview")
    st.markdown(f"""
    **Agreement Date**: {agreement_date}

    **Parties**:  
    - **HyperChat Technologies Pvt. Ltd.**, Udyam No. **UP29D0047796**, Ghaziabad  
    - **Streamer**: **{streamer_name}** ({streamer_email})

    **Revenue Sharing**:  
    - {split_x}% to Streamer  
    - {split_y}% to HyperChat

    **Key Terms**:  
    1. Use HyperChat to engage fans responsibly.  
    2. Respectful behavior required.  
    3. Agreement can be terminated with 7 days’ notice.  
    4. Governed by Indian law.  

    **Signed by**:  
    - Ankit Kumar, Founder, HyperChat  
    - {streamer_name}
    """)

# Generate PDF
if agreed and st.button("Generate & Download PDF"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.set_auto_page_break(auto=True, margin=15)

    contract_text = f"""
HyperChat Streamer Agreement

Date: {agreement_date}

This Agreement is made between:
HyperChat Technologies Pvt. Ltd., Udyam No. UP29D0047796, Ghaziabad
and
{streamer_name}, identified by {streamer_email}.

Revenue Share:
- {split_x}% to Streamer
- {split_y}% to HyperChat

Streamer agrees to responsible use of HyperChat and the terms above.
Agreement may be terminated with 7 days' notice.
Governing Law: India.

Signed:
Ankit Kumar, Founder, HyperChat Technologies Pvt. Ltd.
Streamer: {streamer_name}
"""

    for line in contract_text.split("\n"):
        pdf.multi_cell(0, 10, line.strip())

    # Add signature if present
    if canvas_result.image_data is not None:
        # Convert canvas image to PIL and save to PDF
        image = Image.fromarray((canvas_result.image_data[:, :, :3]).astype("uint8"))
        img_io = io.BytesIO()
        image.save(img_io, format='PNG')
        img_io.seek(0)

        pdf.image(img_io, x=10, y=pdf.get_y() + 10, w=60)
        pdf.ln(50)

    # Save and offer download
    pdf_file = f"{streamer_name.replace(' ', '_')}_HyperChat_Contract.pdf"
    pdf.output(pdf_file)

    with open(pdf_file, "rb") as f:
        st.download_button("📥 Download Signed Contract", f, file_name=pdf_file)

