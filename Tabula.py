import camelot
import pandas as pd
import os

pdf_path = "FinancialStatement-2024-I-AALI.pdf"

output_dir = "extracted_content_page_9"
os.makedirs(output_dir, exist_ok=True)

page_number = '1'

tables = camelot.read_pdf(pdf_path, pages=page_number, flavor='stream')

if tables:
    combined_df = pd.concat([table.df for table in tables])

    csv_filename = os.path.join(output_dir, f"Extracted.csv")

    combined_df.to_csv(csv_filename, index=False, header=False)
    print(f"Content from page 1 saved to {csv_filename}")

    txt_filename = os.path.join(output_dir, f"Extracted.txt")
    with open(txt_filename, 'w', encoding='utf-8') as txt_file:
        for table in tables:
            txt_file.write(table.data_to_string())
            txt_file.write('\n\n')
    print(f"Content from page 1 also saved to {txt_filename}")
else:
    print("No content found on page 1.")

print("Extraction complete.")