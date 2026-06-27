import sqlite3

# 1. Connect to a database (or create it)
conn = sqlite3.connect("example.db")  # creates example.db in the current directory

# 2. Create a cursor object to execute SQL commands
cur = conn.cursor()

# 3. Create a table
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
)
""")

# 4. Insert data into the table
cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))
cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 30))
cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Charlie", 22))

# 5. Commit changes to save them
conn.commit()

# 6. Query data
cur.execute("SELECT * FROM users")
rows = cur.fetchall()  # fetch all results

# 7. Print results
for row in rows:
    print(row)

# 8. Close the connection
conn.close()

