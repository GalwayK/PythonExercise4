import os
import glob
import fpdf
import pandas

pdf = fpdf.FPDF(orientation="P", format="A4", unit="mm")
text_files = glob.glob("files/*.txt")
for text_file in text_files:
    text_name = os.path.basename(text_file).strip(".txt").title()

    pdf.add_page()
    pdf.set_font(family="Times", style='B', size=14)
    pdf.cell(w=0, h=12, txt=text_name, ln=1)

    pdf.set_font(family='Times', size=12)

    with open(text_file) as file:
        for line in file:
            pdf.multi_cell(w=0, h=12, txt=line)

pdf.output("output.pdf")

