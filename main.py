import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

# load_data into python
filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # my way of making it
    # filepath = filepath[9:-5]
    # proper way
    filename = Path(filepath).stem
    number = filename.split("-")[0]
    date = filename.split("-")[1].replace(".", "-")

    pdf.set_font(family="Times", size=12, style="B")
    pdf.cell(w=50, h=12, txt=f"Invoice number: {number}", align="L", ln=1)
    pdf.cell(w=50, h=12, txt=f"Date: {date}",
             align="L", ln=1)
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    # add header
    headerinfo = list(df.columns)
    pdf.set_font(family="Times", size=10, style="B")
    pdf.cell(w=30, h=8, txt=headerinfo[0].replace("_", " ").title(), border=1)
    pdf.cell(w=65, h=8, txt=headerinfo[1].replace("_", " ").title(), border=1)
    pdf.cell(w=35, h=8, txt=headerinfo[2].replace("_", " ").title(), border=1)
    pdf.cell(w=30, h=8, txt=headerinfo[3].replace("_", " ").title(), border=1)
    pdf.cell(w=30, h=8, txt=headerinfo[4].replace("_", " ").title(),
             border=1, ln=1)

    # add data rows
    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=65, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=35, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, ln=1)

    pdf.output(f"PDFs/{filename}.pdf")

