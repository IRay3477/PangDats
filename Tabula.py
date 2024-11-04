import camelot
import os

# Path to your PDF file
pdf_path = "FinancialStatement-2024-I-AALI.pdf"

# Create a directory to store the CSV files
output_dir = "extracted_tables"
os.makedirs(output_dir, exist_ok=True)

# Read tables from only the first page
tables = camelot.read_pdf(pdf_path, pages='1', flavor='lattice')

# Check if tables were extracted
if tables:
    # Process only the first 3 tables (or fewer if there are less than 3)
    for i, table in enumerate(tables[:3]):
        print(f"Extracting Table {i+1} on page 1")
        
        # Generate a filename for the CSV
        csv_filename = os.path.join(output_dir, f"table_{i+1}.csv")
        
        # Save the table to a CSV file
        table.to_csv(csv_filename)
        print(f"Table {i+1} saved to {csv_filename}")
        print("\n")
else:
    print("No tables found on page 1")

print("Extraction complete.")