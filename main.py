import pandas
import glob
import fpdf
filepaths = glob.glob("files/*.xlsx")
print(filepaths)

for filepath in filepaths:
    df = pandas.read_excel(filepath, sheet_name="Sheet 1")
    print(df)
