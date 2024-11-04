import camelot
import mysql.connector
import os
import pandas as pd

# Path to your PDF file
pdf_path = "FinancialStatement-2024-I-AALI.pdf"

# Create a directory to store the extracted content
output_dir = "extracted_content_page_1"
os.makedirs(output_dir, exist_ok=True)

# Specify the page number you want to extract content from
page_number = '1'

# Read content from the specified page using stream mode
tables = camelot.read_pdf(pdf_path, pages=page_number, flavor='stream')

# MySQL database connection
db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'port': '3306',
    'database': 'financial'
}

connection = None
cursor = None

def create_table_if_not_exists(cursor, table_name, df):
    # Create a list of column definitions
    columns = [f"`{col}` TEXT" for col in df.columns]
    columns_string = ", ".join(columns)

    # SQL to create table if it doesn't exist
    create_table_sql = f"""
    CREATE TABLE IF NOT EXISTS `{table_name}` (
        id INT AUTO_INCREMENT PRIMARY KEY,
        {columns_string}
    )
    """
    cursor.execute(create_table_sql)

try:
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    if tables:
        for i, table in enumerate(tables):
            # Convert the table to a DataFrame
            df = table.df
            
            # Ensure all column names are strings and clean them
            df.columns = df.columns.astype(str).str.replace('[^a-zA-Z0-9]', '_', regex=True)
            
            # Create a unique table name for each extracted table
            table_name = f"extracted_table_{i+1}"
            
            # Create the table if it doesn't exist
            create_table_if_not_exists(cursor, table_name, df)
            
            # Prepare the insert SQL
            columns = ", ".join([f"`{col}`" for col in df.columns])
            placeholders = ", ".join(["%s" for _ in df.columns])
            insert_sql = f"INSERT INTO `{table_name}` ({columns}) VALUES ({placeholders})"
            
            # Insert data into MySQL table
            for _, row in df.iterrows():
                cursor.execute(insert_sql, tuple(row))

        # Commit the transaction
        connection.commit()
        print(f"Content from page {page_number} inserted into MySQL tables.")

    else:
        print(f"No content found on page {page_number}.")

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()

print("Extraction and insertion complete.")