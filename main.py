import pandas
import glob
import os
import fpdf
filepaths = glob.glob("files/*.xlsx")
print(filepaths)

for filepath in filepaths:
    df = pandas.read_excel(filepath, sheet_name="Sheet 1")

    # print(df)

    base_filepath = os.path.basename(filepath)
    file_parts = base_filepath.split("-")
    file_parts[1] = file_parts[1].strip(".xlsx")
    print(file_parts)

    pdf = fpdf.FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=False, margin=0)
    pdf.add_page()

    pdf.set_font(family="Times", style='B', size=14)
    pdf.set_text_color(0, 0, 0)

    pdf.cell(w=0, h=10, txt=f"Invoice number: {file_parts[0]}", ln=1)
    pdf.cell(w=0, h=10, txt=f"Date: {file_parts[1]}", ln=1)
    pdf.set_font(family='Times', style='B', size=12)
    file_headers = ["Product ID", "Product Name", "Amount", "Price per Unit", "Total Price"]

    pdf.cell(35, h=10, txt=file_headers[0], ln=0, border=1)
    pdf.cell(60, h=10, txt=file_headers[1], ln=0, border=1)
    pdf.cell(35, h=10, txt=file_headers[2], ln=0, border=1)
    pdf.cell(30, h=10, txt=file_headers[3], ln=0, border=1)
    pdf.cell(30, h=10, txt=file_headers[4], ln=1, border=1)

    total_charge = 0.0
    pdf.set_font(family='Times', size=12)
    for index, row in df.iterrows():
        print(f"{row['product_id']} {row['product_name']} {row['amount_purchased']} "
              f"{row['price_per_unit']} {row['total_price']}")
        pdf.cell(35, h=10, txt=str(row['product_id']), ln=0, border=1)
        pdf.cell(60, h=10, txt=str(row['product_name']), ln=0, border=1)
        pdf.cell(35, h=10, txt=str(row['amount_purchased']), ln=0, border=1)
        pdf.cell(30, h=10, txt=str(row['price_per_unit']), ln=0, border=1)
        pdf.cell(30, h=10, txt=str(row['total_price']), ln=1, border=1)
        total_charge = total_charge + row['total_price']

    pdf.ln(15)
    pdf.set_font(family='Times', style='B', size=14)
    pdf.cell(w=0, h=12, txt=f"The total amount due is {total_charge:.2f}", ln=1, border=0)
    pdf.cell(w=0, h=12, txt="By Kyle Galway", ln=1)

    pdf.output(f"{base_filepath}.pdf")



