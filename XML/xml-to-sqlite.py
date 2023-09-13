import sqlite3
import xml.etree.ElementTree as ET

# XML file name with data
xml_file = 'data.xml'

# SQLite database name
sqlite_db = 'my_database.db'

# Function to dynamically create an SQLite table based on the structure of the XML file
def create_table_from_xml(conn, root):
    cursor = conn.cursor()
    
    # Retrieve all tags (elements) from the first entry
    columns = [elem.tag for elem in root[0]]

    # Create an SQL query to create the table
    create_table_sql = f"CREATE TABLE IF NOT EXISTS my_table (id INTEGER PRIMARY KEY, {', '.join([f'{col} TEXT' for col in columns])})"
    
    # Execute the SQL query to create the table
    cursor.execute(create_table_sql)
    conn.commit()

# Function to insert data from the XML file into SQLite
def insert_data(conn, root, columns):
    cursor = conn.cursor()
    
    # Iterate through each element in the root element of the XML file
    for entry in root:
        values = [entry.find(col).text for col in columns]
        placeholders = ', '.join(['?'] * len(values))
        insert_sql = f"INSERT INTO my_table VALUES (NULL, {placeholders})"
        cursor.execute(insert_sql, values)
    
    conn.commit()

def main():
    # Open an SQLite connection
    conn = sqlite3.connect(sqlite_db)
    
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    # Create the table dynamically based on the structure of the XML file
    create_table_from_xml(conn, root)
    
    # Retrieve columns for inserting data
    columns = [elem.tag for elem in root[0]]
    
    # Insert data into SQLite
    insert_data(conn, root, columns)
    
    # Close the connection
    conn.close()

if __name__ == '__main__':
    main()
