import sqlite3
import json

# JSON file name with data
json_file = 'data.json'

# SQLite database name
sqlite_db = 'my_database.db'

# Function to create an SQLite table based on the JSON structure
def create_table_from_json(conn, json_data):
    cursor = conn.cursor()

    # Read the structure from the first item in the list
    if json_data:
        first_item = json_data[0]
        columns = list(first_item.keys())

        # Create an SQL query to create the table
        create_table_sql = f"CREATE TABLE IF NOT EXISTS my_table (id INTEGER PRIMARY KEY, {', '.join([f'{col} TEXT' for col in columns])})"

        # Execute the SQL query to create the table
        cursor.execute(create_table_sql)
        conn.commit()

# Function to insert data from the JSON file into SQLite
def insert_data(conn, json_data):
    cursor = conn.cursor()
    for item in json_data:
        # Create a list of values for each item in the JSON
        values = [item[col] for col in item.keys()]
        placeholders = ', '.join(['?'] * len(values))
        insert_sql = f"INSERT INTO my_table ({', '.join(item.keys())}) VALUES ({placeholders})"
        cursor.execute(insert_sql, values)
    conn.commit()

def main():
    # Open an SQLite connection
    conn = sqlite3.connect(sqlite_db)

    # Read the JSON file
    with open(json_file, 'r') as f:
        json_data = json.load(f)

    # Create the table dynamically based on the JSON structure
    create_table_from_json(conn, json_data)

    # Insert data into SQLite
    insert_data(conn, json_data)

    # Close the connection
    conn.close()

if __name__ == '__main__':
    main()
