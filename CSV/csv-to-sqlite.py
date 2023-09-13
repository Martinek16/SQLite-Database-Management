import sqlite3
import csv

# CSV file name with data
csv_file = 'data.csv'

# SQLite database name
sqlite_db = 'my_database.db'

# Function to create an SQLite table dynamically based on the first row of the CSV file
def create_table_from_csv(conn, csv_data):
    cursor = conn.cursor()
    columns = next(csv_data)  # Read the first row to obtain column names

    # Create an SQL query to create the table
    create_table_sql = f"CREATE TABLE IF NOT EXISTS my_table (id INTEGER PRIMARY KEY, {', '.join([f'{col} TEXT' for col in columns])})"

    # Execute the SQL query to create the table
    cursor.execute(create_table_sql)
    conn.commit()

# Function to insert data from the CSV file into SQLite
def insert_data(conn, csv_data):
    cursor = conn.cursor()
    for row in csv_data:
        values = row
        placeholders = ', '.join(['?'] * len(values))
        insert_sql = f"INSERT INTO my_table VALUES (NULL, {placeholders})"
        cursor.execute(insert_sql, values)
    conn.commit()

def main():
    # Open an SQLite connection
    conn = sqlite3.connect(sqlite_db)

    # Open the CSV file for reading
    with open(csv_file, 'r') as f:
        csv_data = csv.reader(f)
        
        # Create the table dynamically based on the structure of the CSV file
        create_table_from_csv(conn, csv_data)

        # Reopen the CSV file for reading since we've already read the first row
        f.seek(0)
        csv_data = csv.reader(f)
        
        # Insert data into SQLite
        insert_data(conn, csv_data)

    # Close the connection
    conn.close()

if __name__ == '__main__':
    main()
