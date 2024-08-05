import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

# load_data into python
filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # my way of making it
    # filepath = filepath[9:-5]
    # proper way
    filename = Path(filepath).stem
    number = filename.split("-")[0]
    date = filename.split("-")[1].replace(".", "-")

    pdf.set_font(family="Times", size=12, style="B")
    pdf.cell(w=50, h=12, txt=f"invoice number: {number}", align="L", ln=1)
    pdf.cell(w=50, h=12, txt=f"date: {date}",
             align="L", ln=1)
    pdf.output(f"PDFs/{filename}.pdf")

