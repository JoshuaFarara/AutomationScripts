# Create a connection to the database
conn = sqlite3.connect('mydatabase.sqlite')

# Create a cursor object
cursor = conn.cursor()

# Execute a query
cursor.execute('SELECT * FROM users')

# Fetch the results
results = cursor.fetchall()

# Close the connection
conn.close()