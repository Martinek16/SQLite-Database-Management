import sqlite3

# SQLite database file name
db_file = "my_database.db"

# Function for executing SQL queries
def execute_sql(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        print("SQL executed successfully")
    except sqlite3.Error as e:
        print(f"Error executing SQL: {e}")

# Create an SQLite connection
connection = sqlite3.connect(db_file)

# SQL query to create a table (if it doesn't already exist)
create_table_sql = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    username TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);
"""

# Execute the SQL query to create the table
execute_sql(connection, create_table_sql)

# SQL query to insert data (data is directly inserted into the SQL statement)
insert_data_sql = """
INSERT INTO users (name, username, email)
VALUES ('Admin', 'Admin', 'admin@admin.com');
"""

# Execute the SQL query to insert data
execute_sql(connection, insert_data_sql)

# Close the connection
connection.close()
