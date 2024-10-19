import sqlite3

# Connect to SQLite database (or create it)
conn = sqlite3.connect('rule_engine.db')
cursor = conn.cursor()

# Create users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    age INTEGER NOT NULL,
    department TEXT NOT NULL,
    salary REAL NOT NULL,
    experience INTEGER NOT NULL
);
''')

# Insert sample data
sample_data = [
    (32, 'Sales', 60000, 6),  # Matches: Rule 1
    (28, 'Marketing', 25000, 4), # Matches: Rule 2
    (40, 'Sales', 70000, 8),  # Matches: Rule 1
    (22, 'Marketing', 22000, 3), # Does not match any rule
    (35, 'Sales', 50000, 5),  # Matches: Rule 1
    (30, 'Marketing', 30000, 6) # Matches: Rule 2
]

# Insert data into the users table
cursor.executemany('INSERT INTO users (age, department, salary, experience) VALUES (?, ?, ?, ?)', sample_data)

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database and sample data created successfully.")

